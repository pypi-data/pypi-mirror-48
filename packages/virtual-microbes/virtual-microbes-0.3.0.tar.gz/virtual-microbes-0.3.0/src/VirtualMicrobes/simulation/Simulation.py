# -*- coding: utf-8 -*-
''''
Top level Simulation class that contains all objects and parameters of the
simulation. Has a simulate method that executes the simulation loop, methods to
save and reload, as well as initiate data storage and plotting.
'''

from blessings import Terminal
from multiprocessing.queues import SimpleQueue
import subprocess
import sys, os, time, itertools, collections, shutil, json, psutil
import warnings

import VirtualMicrobes
from VirtualMicrobes.cython_gsl_interface import integrate
from VirtualMicrobes.data_tools.store import DataStore
from VirtualMicrobes.environment.Environment import Environment
import VirtualMicrobes.my_tools.utility as util
from VirtualMicrobes.plotting.Graphs import Graphs
from VirtualMicrobes.readwrite import write_obj
from VirtualMicrobes.virtual_cell.Population import Population
import cPickle as pickle
import class_settings
import multiprocessing as mp


# from pycallgraph import PyCallGraph
# from pycallgraph.output import GraphvizOutput
#runtime profilomg @UnusedImport
# import guppy #memory profiler
#import pickle
#import dill as pickle
sys.setrecursionlimit(50000000)
PICKLE_PROTOCOL = pickle.HIGHEST_PROTOCOL


class Simulation(object):
    '''
    Base class for Simulation objects.

    Stores the simulation parameters.

    Initializes output and storage paths and file for stdout and stderr logging.


    Initializes a data store class for storing data points and time series.

    Initializes a graphs class for output graphing, that will be fed with data points from the data store.

    Has method for the main simulation loop.

    Stores simulation snapshots that can be reloaded for further simulation or post analysis.
    '''

    class_version = '2.4'

    def __init__(self, params):
        '''
        The Simulation is fully defined by the `params` dictionary. Parameters
        that are not explicitly chosen on the command line or in a config file
        are initialized to a default value. These are necessary and sufficient
        to:

        * create a simulation directory and log files
        * initialize the evolutionary `system` containing the :class:`VirtualMicrobes.environment.Environment.Environment`
        and :class:`VirtualMicrobes.population.Population.Population` objects.


        Parameters
        ----------
        params : dict
            dict with *all* settable simulation parameters

        '''

        self.version = self.__class__.class_version
        self.params = params
        self.utility_path = os.path.join(self.params.source_path, self.params.utility_dir)
        self.init_save_dir()
        self.init_log_files()
        self.write_params_to_file()
        self.init_phylo_linker_dict()
        self.init_unique_phylo_key()
        self.init_unique_gene_key()
        self.system = EvoSystem(self.params)  # initilizes Environment and Population
        print 'Initializing graphs.'
        self.init_graphs()
        print 'Initializing movies.'
        self.init_ffmpeg()
        print 'Initialising data store.'
        self.init_data_store()
        self.params.clean_save_path = False # so we do not clean when reloading
        self.subprocesses=[]
        self.run_time = 0
        self.simulation_time = 0
        self.current_dump_name = ''
        self.simulation_saves = []
        self.sim_saves_retry_list = []

    @property
    def save_dir(self):
        '''
        Return the simulation save path.
        '''
        return os.path.abspath(os.path.join(self.base_dir,
                                            self.name))

    #@profile()
    def simulate(self):
        '''
        The main simulation loop.

        Clear the population changes from previous iteration.
        Run the ode system.
        Apply HGT.
        Calculate death rates, determine deaths.
        Compete and reproduce.
        Mutate the offspring.
        Update the phylogeny.
        Store data and plot.
        '''

        consumers = None
        term = Terminal(force_styling=False)
        if not self.params.load_file and self.params.burn_in_time:
            self.simulation_burn_in()
        self.init_spatial_integrator()

        # create first simulation save, and object dumps
        if self.run_time == 0:
            dump_file_name = self.save()
            write_obj.write_env(self.system.environment, os.path.join(self.save_dir,
                                                                  'environment.env'))
        save_and_quit = False
        # hold dynamically updated parameters of the integrator
        diffusion_steps, delta_t_between_diff, release_delay, relative_error = None,None,None,None
        # repeat until the end of the simulation, or other exit event
        while self.run_time <= self.params.duration:

            V = self.run_time % self.params.print_time == 0  # Determine whether or not to print output to stdout

            if V: start = time.time() # Profiling temporary code
            # print out some current parameters of the systems
            if self.run_time % self.params.plot_time == 0:
                print '\nEnvironmental state parameters:'
                self.print_system_details()

            if V: print "\nTime:", self.run_time, time.strftime("{t.blue}\t[%H:%M:%S] [%m-%d]{t.normal}".format(t=term))

            # clear population changes from the previous simulation step, (make new_offspring list empty, etc)
            self.system.population.clear_pop_changes()
            self.system.population.update_stored_variables()

            # lineages will be remarked, depending on current # of markers in
            # population and lineage marking rule
            self.system.population.update_lineage_markers()
            if V: print 'Running ODEs.'


            # compute ODE dynamics of the system
            (self.simulation_time,
             diffusion_steps,
             delta_t_between_diff,
             release_delay,
             relative_error,
             errors) = self.simulation_step(global_time=self.simulation_time,
                                            diffusion_steps=diffusion_steps,
                                            delta_t_between_diff=delta_t_between_diff,
                                            release_delay=release_delay,
                                            update_relative_error=relative_error,
                                            verbal=V)
            if errors:
                print 'cannot recover from errors in integration after maximum number of tries'
                print 'try using a different step_function for integration'
                print 'ending simulation, it is for the best'
                break


            # reset update flag on spatial grid points to False
            self.system.environment.grid_toggle_update()

            # reset flag for external updates to localities to False
            self.system.environment.reset_locality_updates()

            # apply spatially explicit Horizontal Gene Transfer by iterating
            # over the grid points
            if V: print 'Applying HGT.'


            if self.params.wipe_population is not None:
                if self.params.wipe_poisson:
                    if self.run_time != 0 and (self.system.environment.env_rand.uniform(0.,1.)
                                               < 1./self.params.wipe_population.interval):
                        self.system.population.wipe_pop(self.params.wipe_population.fraction,
                                                        min_surv=self.params.min_wipe_survivors,
                                                        time=self.run_time)
                elif self.run_time % self.params.wipe_population.interval == 0:
                    print 'Applying bottleneck!'
                    self.system.population.wipe_pop(self.params.wipe_population.fraction,
                                                min_surv=self.params.min_wipe_survivors,
                                                time=self.run_time) # Don't kill more than this number

            # Killing a lineage from the command line
            if self.params.kill_time == self.run_time:
                if self.params.kill_lineage != None:
                    print 'Killing lineage ' + str(self.params.kill_lineage)
                    self.system.population.kill_cells_lineage([self.params.kill_lineage], self.run_time, 1.0)

            # calculate death rates, according to toxicity levels
            self.system.population.calculate_death_rates()

            # microbes die from natural causes (including toxicity)
            cells_to_kill = self.system.population.mark_for_death()

            #print 'Marked {t.yellow}{}{t.normal} cells.'.format(cells_to_kill,t=term)
            if self.system.population.current_pop_size == cells_to_kill:
                print 'Total Extinction detected, skipping simulation step and plotting and saving directly.'
                save_and_quit = True
            # randomly remove (a fraction of) microbes


            #start = time.time() # Profiling temporary code
            #end = time.time()
            #print 'Step took {t.red}{0:.9g}s{t.normal}.'.format(end-start,t=term)
            if not save_and_quit:
                cells_died = self.system.population.die_off(self.run_time)
                if V: print 'Killed {t.yellow}{}{t.normal} cells.'.format(cells_died,t=term)
                # remove dead microbes from the grid
                self.system.environment.clear_dead_cells_from_grid()

                # reset flag indicating microbe divided in previous simulation step
                self.system.population.reset_divided()

                # competition between microbes to reproduce in available space
                # microbes that are large enough and win competition, reproduce
                if self.params.competition == 'local':
                    if V: print 'Reproducing to max', self.params.max_cells_per_locality, 'cells per grid point.'
                    if V: print "Population before reproduction is {t.green}{}{t.normal}.".format(self.system.population.current_pop_size,t=term)
                    new_offspring_grid_point_dict = self.system.population.reproduce_on_grid(grid=self.system.environment.grid,
                                                                                             max_pop_per_gp=self.params.max_cells_per_locality,
                                                                                             time=self.run_time)
                    self.system.environment.add_new_cells_to_grid(new_offspring_grid_point_dict)
                    if V: print 'Created {t.blue}{}{t.normal} new offspring.'.format(len(self.system.population.new_offspring),t=term)
                elif self.system.population.reproduction_cost != None:
                    self.system.population.reproduce_at_minimum_production(time=self.run_time)
                else:
                    self.system.population.reproduce_production_proportional(time=self.run_time)

                # the new offspring from the reproduction step is mutated
                if self.run_time > self.params.evo_grace_time:
                    self.system.population.mutate_new_offspring(time=self.run_time,
                                                            gp_dict=new_offspring_grid_point_dict,
                                                            environment=self.system.environment)

            ''' Apply HGT during lifetime of cells, rather than a mutation at birth '''
            if not self.params.hgt_at_div_only and self.run_time > self.params.evo_grace_time:
                hgt_grid_point_dict = self.system.population.horizontal_transfer(time=self.run_time,
                                                   grid=self.system.environment.grid,
                                                   environment=self.system.environment)
                # set update flags on grid points if an resident microbe had HGT
                self.system.environment.update_cells_on_grid(hgt_grid_point_dict)

            ''' A neat little trick to accurately control the environment '''

            if self.params.microfluid is not None:
                self.system.environment.microfluid_chemostat(self.run_time)

            ''' Perfectly mix all microbes + Perfectly mix all metabolites. '''
            if self.params.perfect_mix and self.run_time % self.params.perfect_mix == 0:
                self.system.environment.perfect_mix()

            ''' Diffusion of cells on grid (note to user: not extensively tested yet!) '''
            if self.params.cells_grid_diffusion:
                self.system.environment.cells_grid_diffusion()

            if self.params.chemostat:
                cells_died = self.system.population.die_off(self.run_time)
                if V: print 'Chemostat has washed out {t.yellow}{}{t.normal} cells.'.format(cells_died,t=term)
                # remove dead microbes from the grid
                self.system.environment.clear_dead_cells_from_grid()

            assert len(self.system.population.cells) == sum( map(lambda gp: len(gp.content.cells), self.system.environment.grid.gp_iter))

            self.system.population._update_current_ancestors() # add new offspring to the set of all ancestors
            self.system.population._clear_extinct_lineages()# prunes extinct lineages


            if V: end = time.time()
            if V: print "Population after is {t.green}{}{t.normal}.".format(self.system.population.current_pop_size,t=term)
            if V: print 'Simulation step took {t.red}{0:.9g}s{t.normal}.'.format(end-start,t=term)

            # set markers on the microbes to visualise and count their metabolic type
            self.system.population.store_pop_characters()

            # Data is stored into a DataStore object. Writing to a data file is
            # postponed until plots have been drawn. Plotting uses the data in
            # the DataStore object. After plotting functions have started, data
            # is written to file and the written time points are purged from the
            # DataStore.

            if not save_and_quit and self.run_time % self.params.store_data_time == 0 and self.system.population.current_pop_size > 0:
                print 'Storing new data point.'
                self.system.population.update_phylogeny()

                self.data_store.add_pop_data_point(self.system, self.run_time)
                if not self.params.less_eco_dat:    # Adding less data: only add at store time (see below*)
                    self.data_store.add_eco_data_point(self.system, self.run_time)
                    self.data_store.add_expression_data_point(self.system, self.run_time)
                if (self.params.plot_time is not None
                    and self.run_time % self.params.plot_time < self.params.store_data_time):
                    if not self.params.skip_plots:
                        print 'Starting plotting functions.'
                    if self.params.less_eco_dat:    # * If not added at store_time, ad it at plot time :)
                        self.data_store.add_eco_data_point(self.system, self.run_time)
                        self.data_store.add_expression_data_point(self.system, self.run_time)
                    self.add_graphs_data(self.run_time)
                    self.data_store.save_phylo_tree(self.system.population, self.run_time)
                    self._clean_up_processes(consumers)
                    jobs = []
                    if not self.params.skip_plots:
                        jobs += self.plot_and_save_graphs(self.run_time)
                    if self.run_time % self.params.save_time == 0:         # Dirty patch for missing data at save_time.
                        self.add_graphs_data(self.run_time)
                        if not self.params.skip_plots:
                            jobs += self.plot_and_save_graphs(self.run_time)

                    consumers = self._start_parallel_jobs(jobs)
                    print 'Writing stored data and purging.'
                    self.write_data()

            # vary the influx rates of metabolites on the grid
            if self.params.influx_variance_shape is not None or self.params.influx_range is not None:
                self.system.environment.fluctuate(self.run_time)

            # reset concentrations of metabolites on the grid
            if (self.params.resource_cycle is not None and
                self.run_time % self.params.resource_cycle == 0 and
                self.params.wipe_population is not None and
                self.run_time > 0):
                self.system.environment.reset_grid_concentrations()

            # increment simultion steps count
            if len(self.system.population.cells) == 0:
                self._clean_up_processes(consumers)

                if self.params.auto_restart is not None:
                    print 'Total Extinction, auto-restarting.'
                    load_file, param_updates = self.auto_restart_opts()
                    return load_file, param_updates
                else:
                    print 'Total Extinction, ending simulation.'
                    break

            if save_and_quit:
                print 'Save and quit.\nStoring new data point.'
                self.data_store.add_pop_data_point(self.system, self.run_time)
                self.data_store.add_eco_data_point(self.system, self.run_time)
                self.data_store.add_expression_data_point(self.system, self.run_time)
                self.data_store.add_eco_data_point(self.system, self.run_time)
                self.data_store.add_expression_data_point(self.system, self.run_time)
                self.add_graphs_data(self.run_time)
                self._clean_up_processes(consumers)
                if not self.params.skip_plots:
                    jobs = self.plot_and_save_graphs(self.run_time)
                    print 'Starting plotting functions.'
                    consumers = self._start_parallel_jobs(jobs)
                    print 'Writing stored data and purging.'
                self.write_data()
                self.save()
                break

            self.run_time += 1

            # (obsolete) writing a fraction of the objects in the phylogenetic tree to disk
            if self.params.shelve_time is not None and self.run_time % self.params.shelve_time == 0:
                self.phylo_linker_dict.partial_sync(self.params.shelve_fraction, select=lambda x: not x.alive)

            # save the current population to a file
            if self.run_time % self.params.pop_snapshot_time == 0 and self.run_time != 0:
                print 'Saving population snapshot.'
                dump_file_name = save_pop_cells(self, labels=[self.run_time])

            # save the best individual in the population to a file
            if self.run_time % self.params.pop_best_save_time == 0:
                pop_best, _ = self.system.population.most_offspring()
                save_single_cell(self, pop_best )

            # Store a snapshot of the population to a file. This snapshot can be
            # can used to restart and continue the simulation or to perform post
            # analysis.

            if self.run_time % self.params.save_time == 0 or self.run_time in self.params.extra_save_times:
                print 'Writing stored data and purging.'
                self.write_data()
                print 'Cleaning up subprocesses.'
                self._clean_up_processes(consumers)
                print 'Saving simulation.'
                dump_file_name = self.save(store=self.run_time % self.params.store_save_time == 0)

                self.init_spatial_integrator(global_time=self.run_time) # Added by brem to avoid non-determinism because of integrator drivers resetting

                if self.params.load_cycle and len(self.simulation_saves) % self.params.load_cycle == 0 and self.run_time > 0:
                    print 'Exiting for load cycle of % {}.'.format(self.params.load_cycle)
                    return dump_file_name, {}

                if self.params.load_test: #for testing purposes
                    self = load_sim(dump_file_name)
                    self.init_spatial_integrator()



        # save a snapshot before exiting
        if self.run_time % self.params.save_time != 0 and not save_and_quit: # we haven't saved last time point, save and quit means it's is already called upon for extinction
            print 'Writing stored data and purging.'
            self.write_data()
            print 'Cleaning up subprocesses.'
            self._clean_up_processes(consumers)
            print 'Saving simulation.'
            self.save()
        self.close_phylo_shelf()

    def auto_restart_opts(self, retry_list=None, time=None):
        '''
        Automatically restart the simulation after the population became extinct.

        A simulation can be automatically restarted from a previous save point.
        The save points to retry from in the `retry_list` are updated such that
        the most recent point is retried first and removed from this list. This
        ensures that a subsequent restart will not be attempted from the same
        save point, but will instead skip back to a preceding save point. When
        restarting the simulation, new parameter values will be chosen for a
        selected set of parameters, by applying a scaling factor `v`.

        Parameters
        ----------
        retry_list : list
            list of population snapshots that can still be retried for restart

        Returns
        -------
        (population save to retry, new parameter settings for retry)
        '''

        if retry_list is None:
            retry_list = self.sim_saves_retry_list
        if time is None:
            time = self.run_time

        param_updates = {'extinction':True}
        for k,v in self.params.auto_restart.items():
            try:
                prev_val = self.params[k]
                try:
                    param_updates[k] = prev_val * v
                except ValueError:
                    warnings.warn('Parameter "{}" cannot be scaled with constant "{}"'.format(k,v))
            except KeyError:
                warnings.warn('"{}" is not an existing parameter. Scaling value "{}" ignored.'.format(k,v))
        try:
            sim_save = retry_list.pop()
        except IndexError:
            sim_save = self.current_dump_name
        return sim_save, param_updates

    def __del__(self):
        print 'closing phylo shelf on exit'
        self.close_phylo_shelf()

    def save(self, time=None, store=False):
        '''Save the simulation state as a snapshot.

        Parameters
        ----------
        time : simulation time point

        Returns
        -------
        filename of simulation save
        '''
        if time is None:
            time = self.run_time

        if store:
            name = "_".join(self.params.name.split()+ map(str,[self.run_time]))
        else:
            name = "_".join(self.params.name.split())

        dump_file_name = os.path.join(self.save_dir, name) + '.sav'

        self.current_dump_name = dump_file_name
        if time > 0:
            self.simulation_saves.append(self.current_dump_name)
        self.sim_saves_retry_list.append(self.current_dump_name)
        try:
            print 'Creating simulation save file', self.current_dump_name
            save_sim(self, labels=[self.run_time])
            print 'Done saving.'
        except Exception:
            warnings.warn('Exception in save_sim')
            raise
        return dump_file_name

    def _start_parallel_jobs(self, jobs, num_procs = None):
        '''Start a number of jobs in parallel.

        Put a set of (plotting) jobs in a queue, to be run by parallel 'consumer'
        processes. Start the Consumer threads, that read from the jobs queue.

        Parameters
        ----------
        jobs: list
            Processes or tuples of (object, method) to initialize a :class:`VirtualMicrobes.my_tools.utility.Task`
            num_procs: number of parallel consumer processes

        Returns
        -------
        tuple with the new tasks queue and consumers assigned to the jobs in the queue
        '''

        #tasks_queue = mp.Manager().Queue()  -> this makes it very very slow to put jobs in the queue
        if not any(jobs):
            return []
        new_tasks_queue = SimpleQueue() # changed 2-9-2015 because still the queue is not effectively emptied by _clean_up_processes
        print 'distributing', len(jobs), 'jobs'
        for job in jobs:
            if isinstance(job, mp.Process):
                self.subprocesses.append(job)
                job.start()
            elif isinstance(job, tuple):
                time.sleep(.01)
                print 'putting a job in queue'
                new_tasks_queue.put(util.Task(*job))
            print '.',
        if num_procs is None:
            num_procs = self.params.num_parallel_plot_proc

        for _ in range(num_procs):
            print 'putting a poison pill on queue'
            time.sleep(.01)
            new_tasks_queue.put(None) # add 'poison pills' for consumer processes
        new_consumers = [util.Consumer(new_tasks_queue, None) for _ in range(num_procs) ]
        for p in new_consumers:
            p.start()
        return new_consumers

    def _clean_up_consumers(self, consumers, time_out=.5):
        '''Terminate consumer processes and their associated process trees.

        Parameters
        ----------
        consumers : list of consumer :class:multiprocessing.Process
        time_out : timeout before terminating long running
        '''
        for p in consumers:
            #p.join()
            p.join(timeout=0)       #Remove the timeout argument to make the program wait for every plot
            time_ = 0
            dt = .1
            print 'terminating long running tasks',
            while p.is_alive():
                parent = util.kill_proc_tree(p.pid, including_parent=False)
                print '.',
                time.sleep(dt)
                time_+= dt
                if time_ > time_out:
                    print 'terminating long running consumer processes', p
                    p.terminate()
                    try:
                        parent.kill()
                    except psutil.NoSuchProcess:
                        pass
                    break
            else:
                print 'consumer with pid' , p.pid, 'done'
            print

    def _clean_up_processes(self, consumers=None):
        for p in self.subprocesses[:]:
            p.join(timeout=0)    #Remove the timeout argument to make the program wait for every plot
            if p.is_alive():
                parent = util.kill_proc_tree(p.pid, including_parent=False)
                print 'terminating long running plot processes', p
                p.terminate()
                parent.kill()
            else:
                print 'process with pid', p.pid, 'done'
            self.subprocesses.remove(p)
        if consumers is not None:
            self._clean_up_consumers(consumers)

    def update_sim_params(self, params_dict):
        '''
        Update simulation parameters with values in an update dict.

        Parameters
        ----------
        params_dict : dict
            dict with updated parameter values
        '''
        self.params.update(params_dict)

    def init_save_dir(self, clean=None,
                      remove_globs=['*.txt','*.sav', '*.pck', '*.log', '*.err']):
        if clean is None:
            clean = self.params.clean_save_path
        self.base_dir = os.path.abspath(self.params.base_dir)
        self.name = self.params.name
        remove_globs = remove_globs if clean else []
        util.ensure_dir(self.save_dir, remove_globs=remove_globs)
        print 'Saving simulation data in', self.save_dir

    def write_params_to_file(self, save_dir=None, name='params', suffix='.txt', labels=[]):
        if save_dir is None:
            save_dir = self.save_dir
        name = "_".join(name.split()+ map(str,labels))

        param_file_path = os.path.join(save_dir, name + time.strftime("%Y-%m-%d %H:%M") +suffix)
        print 'Writing simulation parameters to file', param_file_path
        with open(param_file_path, 'w') as fp:
            json.dump(self.params, fp, default=util.as_attrdict)

        param_file_path = os.path.join(save_dir, name +suffix) # also write without date
        with open(param_file_path, 'w') as fp:
            json.dump(self.params, fp, default=util.as_attrdict)

    def copy_config_files(self):
        if self.params.config_files is not None:
            for cfg in self.params.config_files:
                try:
                    shutil.copy2(cfg, os.path.join(self.save_dir, os.path.basename(cfg) ))
                except:
                    print 'Could not copy', cfg, 'to save dir', self.save_dir

    def store_command_line_string(self, fn='command_line_string.txt'):
        if self.params.command_line_string is not None:
            print 'Saving command line string in file', fn
            with open(os.path.join(self.save_dir, fn), 'a') as fp:
                fp.write('\n{time} : {cl}\n'.format(time=time.strftime("[%H:%M:%S] [%m-%d]"),
                                                    cl=self.params.command_line_string)
                         )

    def init_log_files(self):
        self.init_log_file()
        self.init_error_log_file()

    def init_log_file(self, save_dir=None, name='log', suffix='.out', labels=[]):
        if save_dir is None:
            save_dir = self.save_dir
        name = "_".join(name.split()+ map(str,labels)) + suffix
        self.log_file = self.open_log_file(os.path.join(save_dir, name))
        self.log_file_name = self.log_file.name

    def init_error_log_file(self, save_dir=None, name='log', suffix='.err', labels=[]):
        if save_dir is None:
            save_dir = self.save_dir
        name = "_".join(name.split()+ map(str,labels)) + suffix
        self.error_log_file = self.open_log_file(os.path.join(save_dir, name))
        self.error_log_file_name = self.error_log_file.name

    def open_log_file(self, name):
        return util.FormatMessageFile(name, 'a')

    def open_phylo_shelf(self, name, flag):
        '''
        Open a Shelf like database object that can store (part of) phylogenetic
        units (PhyloUnit) to disk.
        '''
        return util.open_fifolarder(name, flag=flag, protocol=pickle.HIGHEST_PROTOCOL) #shelve.open(name, flag, protocol=pickle.HIGHEST_PROTOCOL, writeback=True)#

    def reopen_phylo_shelf(self, save_file=None):
        # else, phylo_linker opens the remembered db_file
        self.phylo_linker_dict.reopen_db(save_file=save_file, flag='c')
        util.ugly_globals['PhyloLinkerDict'] = self.phylo_linker_dict

    def reload_unique_phylo_count(self):
        util.ugly_globals['UniquePhyloKey'] = self.unique_phylo_key

    def reload_unique_gene_count(self):
        try:
            util.ugly_globals['UniqueGeneKey'] = self.unique_gene_key
        except AttributeError:
            util.ugly_globals['UniqueGeneKey'] = itertools.count()

    def close_phylo_shelf(self):
        self.phylo_linker_dict.close()

    def save_phylo_shelf(self, name=None, labels=[], suffix='.pck'):
        '''
        Save a snapshot of the phylo_shelf, the global store of PhyloUnit objects.

        Creating the snapshot enables reloading simulation saves with a correct
        state of the phylo_shelf.
        '''
        if name is None:
            name = self.phylo_shelf_name.rstrip(suffix)
        file_name = "_".join(name.split()+ map(str,labels)) + suffix
        self.phylo_shelf_save = os.path.join(self.save_dir, file_name)
        current_phylo_shelf = os.path.join(self.save_dir, self.phylo_shelf_name)
        shutil.copy2(current_phylo_shelf, self.phylo_shelf_save )

    def set_phylo_shelf_file_name(self, name=None,suffix='.pck', labels=[] ):
        if name is None:
            name = self.params.phylo_shelf
        self.phylo_shelf_name = "_".join(name.split()+ map(str,labels))  + suffix

    def update_shelf_location(self, current_save_path=None):
        if current_save_path is not None:
            old_shelf_save = os.path.join(current_save_path, os.path.basename(self.phylo_shelf_save) )
        else:
            old_shelf_save = self.phylo_shelf_name
        print old_shelf_save
        self.set_phylo_shelf_file_name()
        new_phylo_shelf_path = os.path.join(self.save_dir, self.phylo_shelf_name)
        shutil.copy2(old_shelf_save, new_phylo_shelf_path)

    def init_phylo_linker_dict(self):
        '''
        Create a linker dict that maps phylogenetic units (PhyloUnit) to unique
        indices. This linker dict is used to mediate parent-child relations,
        while preventing that pickling recurses (heavily) on the phylogeny (no
        direct references to the objects)
        '''
        self.set_phylo_shelf_file_name()
        self.phylo_linker_dict = self.open_phylo_shelf(os.path.join(self.save_dir, self.phylo_shelf_name), flag='n')
        util.ugly_globals['PhyloLinkerDict'] = self.phylo_linker_dict

    def init_unique_phylo_key(self):
        '''
        Initialize a generator for unique keys for use in the linker dict (see
        above).
        '''
        self.unique_phylo_key = itertools.count()
        util.ugly_globals['UniquePhyloKey'] = self.unique_phylo_key

    def init_unique_gene_key(self):
        '''
        Initialize a generator for unique keys for use in the linker dict (see
        above).
        '''
        self.unique_gene_key = itertools.count()
        util.ugly_globals['UniqueGeneKey'] = self.unique_gene_key

    def init_data_store(self, clean=True, create=True):
        '''
        Initialize a DataStore object for storage of simulation data.

        Data are kept in storage for retrieval by plotting functions until a
        call is made to write the raw data to a file (write_data).
        '''
        self.data_store = DataStore(base_save_dir=self.save_dir, name='data', utility_path=self.utility_path,
                                    n_most_frequent_metabolic_types=5,
                                    n_most_frequent_genomic_counts=10,
                                    species_markers=range(*self.system.population.markers_range_dict['lineage']),
                                    reactions_dict=self.system.environment.reactions_dict,
                                    small_mols=self.system.environment.internal_molecules,
                                    clean=clean, create=create)

    def upgrade_graphs(self):
        self.graphs.init_pop_stats(range(self.system.population.max_pop_size * 2),
                                    self.system.environment.reactions_dict,
                                    self.system.environment.mols_per_class_dict,
                                    create=False)
        self.graphs.init_grid_graphs(self.system.environment.mols_per_class_dict,
                                     self.params.marker_names, create=False)

    def init_ffmpeg(self):
        self.ffmpeg = None
        if self.params['graphs_video']:
            try: # First check if ffmpeg-static is installed (true for machines at TBB-UU)
                proc = subprocess.Popen(["ffmpeg-static","-version"],stdout=subprocess.PIPE,
                                        stdin=subprocess.PIPE, stderr=subprocess.PIPE)
                proc.communicate()
                self.ffmpeg = 'ffmpeg-static'
                print '\033[1m\033[01;36mFFMPEG: set to ffmpeg-static \033[00m'
            except Exception as exc:
                print str(exc), 'occurred'
                try: # Then check if ffmpeg v>2 is installed, will also work
                    proc = subprocess.Popen(["ffmpeg","-version"],stdout=subprocess.PIPE,
                                            stdin=subprocess.PIPE, stderr=subprocess.PIPE)
                    out, _err = proc.communicate()
                    print out
                    version = out.split('\n')[0].split()[1].split('-')[0].split('.')[0]
                    print 'ffmpeg version {} found'.format(version)
                    if int(version) < 2:
                        print '\033[1m\033[01;31mYour version of FFMPEG is outdated.\, Please upgrade to ffmpeg version 2 or higher if you want mp4-video output in the webapplication.\033[00m'
                    else:
                        self.ffmpeg = 'ffmpeg'
                        print '\033[1m\033[01;36mFFMPEG: set to ffmpeg v2, hoping for the best \033[00m'
                except Exception as exc: # Throw a final exception if none of these work.
                    print str(exc), 'occurred'

    def init_graphs(self, show=None, clean=True, create=True):
        '''
        Initialize a Graphs object that contains simulation graphs.

        :param show: plot graphs on the X (blocking)
        '''
        if show is None:
            show = self.params.show

        self.graphs = Graphs(base_save_dir=self.save_dir, name="plots",
                             utility_path=self.utility_path,
                             mol_class_dict=self.system.environment.mols_per_class_dict,
                             reactions_dict=self.system.environment.reactions_dict,
                             population_markers=self.params.marker_names,
                             species_markers=range(self.system.population.max_pop_size * 2), # cell_markers('lineage'),
                             show=show, clean=clean, create=create)

    def plot_and_save_graphs(self, time_point):
        '''
        Depending on the initialization parameter 'graphs_single_core' this will
        either run all plotting in functions in sequence (appending None to
        processes) or construct a list of job processes/ task tuples, to be run
        in parallel batch processes, separate from the main thread. These
        processes will be either put in a job queue or separately started by
        '_start_parallel_jobs'.

        :param time_point: simulation time point
        '''
        processes = []
        processes += self.plot_time_course(time_point)
        #processes += self.plot_pop_stats() -> Use browser to see population data now
        processes += self.plot_grid_graphs(time_point)      #Zero padding added by Brem
        processes += self.plot_best_genome_structure(time_point)
        processes += self.plot_networks(time_point)         #Zero padding added by Brem
        return processes

    #def plot_and_save_phylo_graphs(self, max_tree_depth, time_point):
    #    return self.plot_phylo_tree(max_tree_depth, labels=[time_point])

    #def plot_phylo_tree(self, max_tree_depth, labels):
    #    process = self.graphs.plot_phylo_tree(pop=self.system.population,
    #                                          env=self.system.environment,
    #                                          max_depth=max_tree_depth,
    #                                          labels=labels, save=True)
    #    return [process]

    def plot_time_course(self, time_point):
        labels=[format(time_point,'010')]
        pop = self.system.population
        most_fecundant, _nr = pop.most_offspring()
        per_type_time_courses = most_fecundant.get_gene_type_time_course_dict()
        internal_res_conc_dict = most_fecundant.get_mol_time_course_dict()
        external_res_conc_dict = self.system.environment.localities[0].get_mol_time_course_dict()
        toxicity_time_course =  most_fecundant.get_toxicity_time_course()
        raw_production_time_course = most_fecundant.get_raw_production_time_course()
        cell_size_time_course = most_fecundant.get_cell_size_time_course()

        process = self.graphs.plot_time_course(internal_res_conc_dict,
                                               external_res_conc_dict,
                                               per_type_time_courses,
                                               cell_size_time_course,
                                               toxicity_time_course,
                                               raw_production_time_course,
                                               labels=labels,
                                               save_no_labels=True)
        return [process]

    def plot_pop_stats(self):
        process = self.graphs.plot_pop_stats()
        return [process]

    def plot_grid_graphs(self, time_point):
        labels=[format(time_point,'010')]
        title=format(time_point,'010')

        process = self.graphs.plot_grid_graphs(map(str,self.system.environment.internal_molecules),
                                               self.system.environment.reactions_dict,
                                               self.system.population.markers_range_dict.keys(),
                                               video=self.ffmpeg, data_range = self.params.grid_graph_data_range,
                                               labels=labels, save_no_labels=True,
                                               title=title)
        return [process]

    def write_data(self):
        self.data_store.write_data()

    def add_graphs_data(self, time_point):
        pop = self.system.population

        most_fecundant, _nr = pop.most_offspring()
        mf_death_rate = pop.death_rates([most_fecundant])[0]
        mf_production = pop.production_rates([most_fecundant])[0]
        affix = 'fecundant'
        self.graphs.add_pop_stats_data(time_point, mf_death_rate, mf_production,
                                       self.data_store)
        self.data_store.add_best_data_point(most_fecundant,
                                    self.graphs.attribute_mapper, time_point, affix)

        oldest_cell = pop.oldest_cell()


        affix = 'old'
        self.data_store.add_best_data_point(oldest_cell,
                                    self.graphs.attribute_mapper, time_point, affix)


        halfway_l_index = len(self.system.environment.localities)/2
        external_res_conc_dict = self.system.environment.localities[halfway_l_index ].get_mol_concentration_dict()
        self.graphs.add_mol_evo_time_course_data(time_point, external_res_conc_dict)

        markers_range_dict = self.system.population.markers_range_dict

        #print markers_range_dict.keys() = lineage and metabolic dict
        pop_grid_data_dict = self.system.environment.population_grid_data_dict(markers_range_dict.keys(),
                                                                               self.system.population.most_abundant_marker)

        min_cell_vol = min(self.params.cell_init_volume,
                           self.params.cell_division_volume / 2.) if self.params.cell_division_volume else self.params.cell_init_volume
        scaling_dict_updates = {'death_rate_min':0.0,
                                'cell_size_min': min_cell_vol,
                                'cell_size_max': self.params.max_cell_volume,
                                'crossfeed_max' : len(self.system.environment.molecule_classes)
                                }
        self.graphs.add_grid_graphs_data(time_point, pop_grid_data_dict,
                                         map(str, self.system.environment.internal_molecules),
                                         self.data_store, scaling_dict_updates, markers_range_dict)
        self.graphs.add_prot_grid_graphs_data(time_point, map(str, self.system.environment.internal_molecules),
                                              self.system.environment.reactions_dict, self.data_store)

    def plot_networks(self, time_point):
        labels = [format(time_point,'010')]
        title = format(time_point,'010')
        pop = self.system.population
        most_fecundant, _nr = pop.most_offspring()
        oldest_cell = pop.oldest_cell()
        processes = []
        marker = most_fecundant.marker_dict['lineage']
        building_blocks = most_fecundant.building_blocks_dict.keys()
        no_labels = []
        fig_dict = {'png': [ no_labels, labels ],
                    'svg': [ no_labels, labels] }
        write_dict = {'.gml': [labels],
                      '.dot': [labels]}
        processes.append(self.graphs.plot_binding_network(cell=most_fecundant,
                                                          fig_ext_label_dict=fig_dict,
                                                          text_ext_label_dict=write_dict,
                                                          prog='dot',
                                                          video = self.ffmpeg,
                                                          write=True,
                                                          title=title)
                                                        )
        no_labels.append('old')
        labels.append('old')
        processes.append(self.graphs.plot_binding_network(cell=oldest_cell,
                                                          fig_ext_label_dict=fig_dict,
                                                          text_ext_label_dict=write_dict,
                                                          prog='dot',
                                                          video=self.ffmpeg,
                                                          write=False,
                                                          title=title)
                                                )
        labels = [format(time_point,'010')]
        no_labels = []
        fig_dict = {'png': [ no_labels, labels ],
                    'svg': [ no_labels, labels] }
        write_dict = {'.gml': [labels],
                      '.dot': [labels]}

        processes.append(self.graphs.plot_metabolic_network(fig_ext_label_dict=fig_dict,
                                                            text_ext_label_dict=write_dict,
                                                            reactions_dict=most_fecundant.reaction_set_dict,
                                                            building_blocks=building_blocks,
                                                            self_marker=marker,
                                                            video=self.ffmpeg,
                                                            title=title))
        labels.append('pan')
        no_labels.append('pan')
        processes.append(self.graphs.plot_metabolic_network(fig_ext_label_dict=fig_dict,
                                                            text_ext_label_dict=write_dict,
                                                            reactions_dict=pop.pan_reactome_dict(),
                                                            video=self.ffmpeg,
                                                            title=title,
                                                            video_frame_name='Metabolome_pan.png'))
        return processes

    def plot_best_genome_structure(self, time_point):
        labels=[format(time_point,'010')]
        pop = self.system.population
        most_fecundant, _nr = pop.most_offspring()
        processes = []
        processes.append(self.graphs.plot_genome_structure(most_fecundant, labels, video=self.ffmpeg))
        return processes

    def describe_environment(self):
        processes = []
        imports = ([ (i, True) for i in self.system.environment.reactions_dict['import'] ] +
                [ (i, False) for i in self.system.environment.reactions_dict['import'] ] )
        conversions = [ (c,True) for c in self.system.environment.reactions_dict['conversion'] ]
        proc = self.graphs.plot_metabolic_network({'import':imports, 'conversion':conversions},
                                           with_labels_suffix='_env.png',
                                           save_no_labels=False)
        processes.append(proc)
        for process in processes:
            if isinstance(process, mp.Process):
                self.subprocesses.append(process)
                process.start()
                print '.',
        print 'done'

    def store_previous_save_dir(self):
        '''
        Save the location for data storage presently used in the simulation.

        Useful to keep a history of save locations when simulations are reloaded
        and run with different data storage locations.
        '''
        if hasattr(self, 'old_save_dirs'):
            self.old_save_dirs.append(self.save_dir)
        else:
            self.old_save_dirs = [self.save_dir]

    def update_data_location(self, save_dir=None, graphs_name='plots',
                             data_name='data', clean=False, copy_data=True,
                             create=True, current_save_path=None):
        '''
        Moves existing data to a new location (e.g. when name of project has
        changed after propagating an existing population)
        '''
        if save_dir is None:
            save_dir = self.save_dir
        self.graphs.change_save_location(base_save_dir=save_dir,
                                         name=graphs_name,
                                         clean=clean,
                                         create=create)
        self.data_store.change_save_location(base_save_dir=save_dir,
                                             name=data_name,
                                             clean=clean,
                                             copy_orig=copy_data,
                                             create=create,
                                             current_save_path=current_save_path)

    def prune_data_store_files(self):
        self.data_store.prune_data_files_to_time(self.params.prune_csv_from_time, self.run_time)

    def backup_pop_stats(self):
        self.graphs['population stats'].backup_plots()

    def print_system_details(self):
        self.system.environment.print_values()

    def upgrade(self, odict):
        '''
        Upgrading from older pickled version of class to latest version. Version
        information is saved as class variable and should be updated when class
        invariants (e.g. fields) are added. (see also __setstate__)

        Adapted from recipe at http://code.activestate.com/recipes/521901-upgradable-pickles/
        '''
        version = float(self.version)
        if version < 1.:
            self.base_dir, self.name = os.path.split(odict['save_dir'])
            del self.__dict__['save_dir']
        if version < 2.:
            self.init_graphs(clean=False)
        if version < 2.1:
            self.simulation_time = self.run_time * self.params.delta_t_between_diff * self.params.diffusion_steps
        if version < 2.2:
            self.simulation_saves = [self.current_dump_name]
            self.sim_saves_retry_list = self.simulation_saves[:]
        if version < 2.6:
            try:
                self.data_store.copy_utility_files()
            except IOError:
                warnings.warn('Could not copy new utility files. Perhaps the save path is not recognized during loading.')
            self.params.energy_transcription_cost = 0.0
        #print self.class_version
        #self.save_dir , self.name = os.path.split(odict['save_dir'])
        self.version = self.class_version
        if version > float(self.class_version):
            print 'upgraded class',
        else:
            print 'reset class',
        print self.__class__.__name__, ' from version', version ,'to version', self.version

    def __getstate__(self):
        odict = self.__dict__.copy()
        del odict['graphs']
        del odict['subprocesses']
        del odict['log_file']
        del odict['error_log_file']
        del odict['spatial_integrator']
        return odict

    def __setstate__(self, d):
        self.__dict__ = d
        self.subprocesses = []
        # upgrade class if it has an older version
        if not hasattr(self, 'version'):
            self.version = '0.0'
        if self.version != self.class_version:
            self.upgrade(d)

    def __getitem__(self, key):
        return self.params[key]

def save_single_cell(sim, cell, name=None, save_dir=None, labels=[], suffix='.sav'):
    if name is None:
        name = sim.params.gen_best_save_name
    name = "_".join(name.split()+ map(str,labels))
    if save_dir is None:
        save_dir = sim.save_dir
    sim.close_phylo_shelf()
    dump_file_name = os.path.join(save_dir, name)+suffix
    dump_file = open(dump_file_name, 'w')
    pickle.dump(cell, dump_file, protocol=PICKLE_PROTOCOL)
    write_obj.write_cell(cell, filename=os.path.join(save_dir,
                                                     'data/best_dat/',
                                                     name+str(sim.run_time)+'.cell'))
    dump_file.close()
    sim.reopen_phylo_shelf()
    return dump_file_name


def save_pop_cells(sim, name=None, save_dir=None, labels=[], suffix='.sav'):
    if name is None:
        name = sim.params.pop_save_name
    name = "_".join(name.split()+ map(str,labels))
    if save_dir is None:
        save_dir = sim.save_dir
    sim.close_phylo_shelf()
    dump_file_name = os.path.join(save_dir, name)+suffix
    dump_file = open(dump_file_name, 'w')
    #first save the number of cells that will be stored
    pickle.dump(len(sim.system.population.cells), dump_file, protocol=PICKLE_PROTOCOL)
    for cell in sim.system.population.cells:
        pickle.dump(cell, dump_file, protocol=PICKLE_PROTOCOL)
    dump_file.close()
    sim.reopen_phylo_shelf()
    return dump_file_name

#@util.subprocessor(as_subprocess=False)
@util.processify
def save_sim(sim, dump_file_name=None, labels=[]):
    '''
    Make a pickled save state of the simulation.

    It (nearly) completely creates a pickle representation of the
    simulation, from which the simulation can be reloaded and continued,
    with parameters and state fully restored. Because a global linker dict
    with database functionality is used to store phylogenetic elements such
    as Genes, Chromosomes and Cells, a snapshot of this database needs to be
    created simultaneously. The snapshot of the DB is remembered within the
    simulation, to allow it to be reloaded when the saved simulation state
    is reloaded.
    '''
    if dump_file_name is None:
        dump_file_name = sim.current_dump_name
    #: sync and close the phylo shelf to prepare it for pickling
    sim.close_phylo_shelf()
    # take snapshot of the phylo shelf
    sim.save_phylo_shelf(labels=labels)
    dump_file = open(dump_file_name, 'w')

    #First dump the parameters, so when loading these can be retrieved
    #first. This is necessary to dynamically initialize the Graphs class
    #with the correct decorator parameter for optionally subprocessed
    #functions (see Graphs class)

    pickle.dump(class_settings.phylo_types, dump_file, protocol=PICKLE_PROTOCOL)
    pickle.dump(sim.params, dump_file, protocol=PICKLE_PROTOCOL) #pickle.HIGHEST_PROTOCOL)
    pickle.dump(sim, dump_file, protocol=pickle.HIGHEST_PROTOCOL)

    dump_file.close()
    sim.reopen_phylo_shelf()

def load_sim_params(file_name):
    file_name = os.path.abspath(file_name)
    load_file = file(file_name,'r')
    params = pickle.load(load_file)
    return params

#@util.processify
def load_sim(file_name, verbose=False, **param_updates):
    '''
    Load a pickled representation of a saved simulation state.

    Complementary method to :save_sim: to load and restore a simulation
    state. There is a possibility to update simulation parameters. The first
    stage of unpickling will reload the simulation parameters. This is
    necessary, because we need to set the 'as_subprocess' parameter for
    decorating Graph methods to be set before class initialization, by
    retrieving the 'graphs_single_core' parameter from the simulation
    'temp_params' prior to reloading and recreating the pickled Graphs instance
    in the simulation object.
    '''
    import matplotlib.pyplot as plt
    plt.close('all')
    file_name = os.path.abspath(file_name)
    load_file_path = os.path.dirname(file_name)
    print 'loading sim from', file_name
    with open(file_name, 'r') as load_file:
        _phylo_types = pickle.load(load_file)
        temp_params = pickle.load(load_file)
        _param_updates = dict()
        for k,v in param_updates.items():
            o_val = temp_params.get(k, '**NOT FOUND**')
            if o_val == '**NOT_FOUND**' or o_val != v:
                _param_updates[k] = v
        param_updates = _param_updates
        print 'updating parameters:'
        for k,v in param_updates.items():
            print k, v
        # If a new name (or basedir) is given for the simulation, a new base_dir will be made for file storage
        change_location = False
        copy_data = False
        create = False
        if ( (param_updates.has_key('name') and param_updates['name'] != temp_params.name ) or
            (param_updates.has_key('base_dir') and param_updates['base_dir'] != temp_params.base_dir)
            ):
            change_location = True
            create = True
            copy_data = True

        # overwrite simulation parameters by values explicitly set on command line
        temp_params.update(param_updates)
        print 'done updating params'
        util.ugly_globals['graphs_as_subprocesses'] = not temp_params.graphs_single_core

        # Use a custom unpickler so that we can map pickles using the old
        # package structure to the new (VirtualMicrobes) package structure and
        # allowing to return the correct class definitions for the pickle
        # objects.
        unpickler = pickle.Unpickler(load_file)
        unpickler.find_global = util.map_old_package_path
        sim = unpickler.load()

    # detect if the folder containing the simulation has been moved/copied before loading or
    # its path changed from relative to absolute specification



    current_save_path = sim.save_dir
    path_name_change, different_content = util.detect_sim_folder_move(sim.save_dir, load_file_path)
    if path_name_change:
        change_location = True
        current_save_path = load_file_path
        #rel_path_change = util.detect_rel_path_change(sim.save_dir, file_name)
        if different_content or different_content is None: # We do not know the original save_path
            # assume that the simulation dir is the parent of the load_file
            copy_data = True
            create = True
            if different_content:
                warnings.warn('Path content changed after copying the save path.\n'
                              'Assuming that the load path ({}) contains simulation data.\n'
                              'Continuing loading...'.format(current_save_path))
            elif different_content is None:
                warnings.warn('Cannot compare load path content with original simulation path ({}).\n'
                              'Assuming that the load path ({}) contains simulation data.\n'
                              'Continuing loading...'.format(current_save_path, sim.save_dir))

    if not param_updates.has_key('base_dir') and path_name_change:
        print 'detected simulation data move, updating internal paths'
        if not param_updates.has_key('name'):
            new_base_dir, new_save_dir = os.path.split(load_file_path)
            param_updates['name'] = new_save_dir
        else:
            new_base_dir = load_file_path
            print 'setting base_dir to', new_base_dir
            param_updates['base_dir'] = new_base_dir
            create = True

    sim.store_previous_save_dir()

    if param_updates.get('extinction', None): # when reloading after extinction, remove last retry save
        try:
            sim.sim_saves_retry_list.pop()
        except IndexError:
            pass
        del param_updates['extinction']

    # update the simulation parameters
    sim.update_sim_params(param_updates)

    # don't clean, because we may be continuing a simulation in the original simulation directory
    sim.init_save_dir(clean=False)
    sim.init_log_files()
    sim.set_phylo_shelf_file_name()
    sim.write_params_to_file()



    if change_location: # Change location, data location will be updated and files will be copied
        sim.init_graphs(clean=True, create=True) # init graphs here after detecting a potential change in save path
        clean = param_updates.get('clean_save_path',False) # only clean when not loading in original run path
        sim.update_data_location(clean=clean,
                                 copy_data=copy_data,
                                 create=create,
                                 current_save_path=current_save_path)
    else:
        sim.init_graphs(clean=False, create=False) # init graphs here after detecting a potential change in save path

    shutil.copy2(os.path.join(sim.save_dir, 'params.txt'),  os.path.join(sim.save_dir, 'data'))
    #prune the data files to the current run_time of the simulation
    sim.prune_data_store_files()
    sim.update_shelf_location(current_save_path=current_save_path)

    sim.reopen_phylo_shelf(os.path.join(sim.save_dir, sim.phylo_shelf_name))
    # Below sets the unique ID for phylo units and genomic elements to correct value again
    sim.reload_unique_phylo_count()
    # Below sets the unique ID for genomic units to correct value again
    sim.reload_unique_gene_count()

    sim.backup_pop_stats()
    sim.system.reinit_system_params(sim.params, **param_updates)                                # CHECK FOR LOADCYCLE OKAY

    sim.params.upgrade_environment = False
    sim.params.env_from_file = None

    if param_updates.get('reset_historic_max', None) is not None:
        if sim.params.selection_pressure != 'historic_fixed':
            print 'Warning: if you reset the historic max, but dont fix the selection pressure, it will immediatly bump back to its previous value!'
        print 'resetting historic max to ', str(sim.params.reset_historic_max)
        sim.system.population.historic_production_max = sim.params.reset_historic_max

    return sim

class ODE_simulation (Simulation):
    '''
    Set up a simulation. Initialize an EvoSystem and an Integrator. EvoSystem
    consists of a Population and Environment that are co-dependent. This is
    because a Cell in a Population can only choose its Reactions once the
    environment is set up and the reaction space is ready, while the reaction
    space can only be fully known, when all internal molecules have been defined
    in relation to Cells in the Population. To circumvent the problem, internal
    molecules will only exist as 'ideal' type molecules and then every Cell will
    contain a mapping from 'ideal' molecules to actual variables of the system.
    '''

    def __init__(self, params):
        '''
        Initialize the EvoSystem, defining all parameters of the model
        :param duration: evolutionary time steps/generations
        '''
        super(ODE_simulation, self).__init__(params)
        self.init_time_course_lengths()


    def init_time_course_lengths(self):
        max_len = self.max_time_course_length()
        self.system.population.resize_time_courses(max_len)
        self.system.environment.resize_time_courses(max_len)


    def init_spatial_integrator(self, diffusion_steps=None, report_frequency=None,
                                step_function=None, init_step_size=None, absolute_error=None,
                                relative_error=None, global_time=0.):
        if diffusion_steps is None:
            diffusion_steps = self.params.diffusion_steps
        if report_frequency is None:
            report_frequency = self.params.report_frequency
        if step_function is None:
            step_function = self.params.step_function
        if init_step_size is None:
            init_step_size = self.params.init_step_size
        if absolute_error is None:
            absolute_error = self.params.absolute_error
        if relative_error is None:
            relative_error = self.params.relative_error

        self.system.environment.map_variables()
        product_scaling = self.system.population.historic_production_max
        self.spatial_integrator = integrate.SpatialIntegrator(self.system.environment.grid, # @UndefinedVariable
                                                              step_function,
                                                              hstart=init_step_size,
                                                              epsabs=absolute_error,
                                                              epsrel=relative_error,
                                                              time=global_time,
                                                              product_scaling=product_scaling)

    def max_time_course_length(self):
        tps = 1
        if hasattr(self.params, 'report_frequency'):
            tps = ( self.params.diffusion_steps * self.params.delta_t_between_diff) * self.params.report_frequency
        return max(int(tps * (1/self.params.base_death_rate) * 4 ), 1)

    def simulation_burn_in(self, burn_in_time=None, simulation_steps=1):
        if burn_in_time is None:
            burn_in_time = self.params.burn_in_time
        diffusion_steps = burn_in_time / self.params.delta_t_between_diff

        self.init_spatial_integrator(diffusion_steps, report_frequency=0)

        for _ in range(simulation_steps):
            self.simulation_step(global_time=0,
                                 diffusion_steps=diffusion_steps,
                                 report_frequency=0)
        self.system.population.reset_production_toxicity_volume()

    #@profile
    def simulation_step(self, global_time=None, diffusion_steps=None,
                        delta_t_between_diff=None, report_frequency=None,
                        release_delay=None, update_relative_error=None, verbal=False):
        '''
        A simulation step will run the integration of
        cycle of a cell's life:

        * setup the variables_map needed
        * simulate internal dynamics
        * save variables states back to python objects (if no errors occured or > maxtries)
        '''
        if global_time is None:
            global_time = self.simulation_time
        if diffusion_steps is None:
            diffusion_steps = self.params.diffusion_steps
        if report_frequency is None:
            report_frequency = self.params.report_frequency
        if delta_t_between_diff is None:
            delta_t_between_diff = self.params.delta_t_between_diff
        if update_relative_error is None:
            update_relative_error = self.params.relative_error

        self.system.environment.map_variables()

        errors, start = False, True
        tries = 0
        while (errors or start):
            if release_delay:
                if verbal: print 'Release delay: Waiting', release_delay, 'more steps to lower diffusion steps.'
            # if necessary grow the arrays to hold the time course data
            self.system.population.grow_time_course_arrays()

            product_scaling = self.system.population.historic_production_max
            if verbal: print 'Production scaling:', product_scaling
            if verbal: print 'Updating spatial integrator.'
            #start = time.time()
            self.spatial_integrator.update_integrators(product_scaling=product_scaling,
                                                       time=global_time,
                                                       reset=errors,
                                                       )
            tries += 1
            start = False
            errors = self.spatial_integrator.run_spatial_system(diffusion_steps, delta_t_between_diff,
                                                                self.params.diffusion_constant,
                                                                report_frequency,
                                                                self.params.num_threads)
            if not errors:
                if diffusion_steps > self.params.diffusion_steps: # diffusion_steps have been increased previously
                    if release_delay is not None and release_delay > 0:
                        release_delay -= 1
                    else:
                        diffusion_steps /= self.params.retry_steps_factor
                        delta_t_between_diff *= self.params.retry_steps_factor
                        if self.params.relative_error is not None and self.params.rel_err_incr_fact is not None:
                            update_relative_error /= self.params.rel_err_incr_fact
                            self.spatial_integrator.update_drivers(epsrel=update_relative_error)
                        if diffusion_steps > self.params.diffusion_steps:
                            release_delay = self.params.wait_release_t_diff

            elif self.params.max_retries is not None and tries == self.params.max_retries + 1:
                warnings.warn('Still errors after ' + str(self.params.max_retries + 1) + ' tries. Saving state and hoping for the best.')
                break
            else:
                diffusion_steps *= self.params.retry_steps_factor
                delta_t_between_diff /= self.params.retry_steps_factor
                warnings.warn('Errors in integration, increasing the number of '
                              'diffusion steps to ' + str(diffusion_steps) + ' at smaller '
                              'interval ' + str(delta_t_between_diff))
                if update_relative_error is not None and self.params.rel_err_incr_fact is not None:
                    update_relative_error *= self.params.rel_err_incr_fact
                    warnings.warn('Reducing allowed relative error to ' + str(update_relative_error))
                    self.spatial_integrator.update_drivers(epsrel=update_relative_error)

                release_delay = self.params.wait_release_t_diff # set release delay for returning to less diffusion_steps
                warnings.warn('Setting release delay for reverting to smaller step size to ' + str(release_delay) )

        self.spatial_integrator.store_nr_time_points_py()
        global_time += diffusion_steps * delta_t_between_diff
        #end = time.time()
        #print 'Step took ' + str(end-start) + ' seconds.'
        return ( global_time, diffusion_steps, delta_t_between_diff,
                 release_delay, update_relative_error, errors )

class EvoSystem(object):
    '''
    Sets up the Environment and the Population.
    '''
    def __init__(self, params):
        self.environment = Environment(params)
        self.population = Population(params,  self.environment)
        self.setup_environment()

    def setup_environment(self):
        self.environment.populate_localities(self.population)

    def reinit_system_params(self, params, **param_updates):

        if (param_updates.has_key('influx_range') or
            param_updates.has_key('influx') or
            param_updates.has_key('influx_frequencies')):
            self.environment.reset_grid_influx()
        if param_updates.get('resource_cycle', None) is not None:
            self.environment.reset_grid_concentrations()
        if param_updates.has_key('env_rand_seed'):
            self.environment._init_rand_gens(param_updates['env_rand_seed'])
        if param_updates.has_key('evo_rand_seed'):
            self.population.init_evo_rand_gens(param_updates['evo_rand_seed'])
        if param_updates.has_key('small_mol_ext_degr_const'):
            print 'updating dgr dict' + str(params.small_mol_ext_degr_const)
            self.environment.init_degradation_dict(params.small_mol_ext_degr_const,
                                   params.ene_ext_degr_const,
                                   params.bb_ext_degr_const,
                                   degradation_variance_shape=params.degradation_variance_shape)

            self.environment.func_on_grid(lambda l: l.update_small_mol_degradation_rates(self.environment.degradation_dict))

        if param_updates.has_key('small_mol_diff_const'):
            print 'updating diff dict to' + str(params.small_mol_diff_const)
            self.environment.init_membrane_diffusion_dict()

            for cell in self.population.cells:
                cell.update_small_molecules_diff(self.environment)
        if param_updates.has_key('per_grid_cell_volume'):
            self.environment.update_volume(param_updates['per_grid_cell_volume'])
        if hasattr(params, 'env_from_file'):                                            # Compatibility with old version of Vmicrobes
            if params.env_from_file is not None and params.upgrade_environment:
                self.environment.update_reaction_universe(params.env_from_file) # updates reaction universe, currently only supports ADDING reactions/molecules, not substracting them


def mut_func_single_param(val, rand_g, mut_par_space, up):
    #step = val + val * mut_par_space.base** (rand_g.uniform(mut_par_space.lower, mut_par_space.upper)) - val
    if(up):
        step = val + rand_g.uniform(mut_par_space.lower, mut_par_space.upper)
    else:
        step = val - rand_g.uniform(mut_par_space.lower, mut_par_space.upper)
    return max(min(val+step,mut_par_space.max),mut_par_space.min)

def mut_func_single_param_step_uniform(val, rand_g, mut_par_space, up):
    if (rand_g.uniform(0.0,1.0) < mut_par_space.randomize):
        return rand_g.uniform(mut_par_space.min, mut_par_space.max)
    else:
        if(up):
            step = rand_g.uniform(mut_par_space.lower, mut_par_space.upper)
        else:
            step = -1.0*rand_g.uniform(mut_par_space.lower, mut_par_space.upper)
        return max(min(val+step,mut_par_space.max),mut_par_space.min)


def partial_mut_func_single_param(val, rand, mut_par_space, up=True):
    if mut_par_space.uniform:
        return mut_func_single_param_step_uniform(val, rand, mut_par_space, up)
    else:
        return mut_func_single_param(val, rand, mut_par_space, up)

def mut_ks_dict_func(kss, rand_gen, mut_par_space, mutate_single_param, up):
        single_ks = rand_gen.choice(kss.keys())
        kss[single_ks] = mutate_single_param(kss[single_ks], rand_gen, mut_par_space, up)
        return kss

def partial_mut_ks_dict_func(val, rand, mut_par_space, up=False):
    return mut_ks_dict_func(val, rand, mut_par_space, partial_mut_func_single_param, up)

def pump_exporting_mut_func(val):
    return not val

def tf_ext_sense_mut_func(val):
    return not val

def default_params():
    simulate_params, env_params, pop_params = dict(), dict(), dict() # NOTE: unordered ok
    point_mutation_dict = {
                           "pump" : collections.OrderedDict([
                                                             ("v_max", partial_mut_func_single_param),
                                                             ("ene_ks", partial_mut_ks_dict_func),
                                                             ("subs_ks",partial_mut_ks_dict_func),
                                                             ("exporting",pump_exporting_mut_func),
                                                             ("promoter",partial_mut_func_single_param),
                                                             ("operator",1)]
                                                             ),
                           "tf" : collections.OrderedDict([
                                                           ("eff_apo", partial_mut_func_single_param),
                                                           ("eff_bound", partial_mut_func_single_param),
                                                           ("ligand_ks", partial_mut_ks_dict_func),
                                                           ("promoter", partial_mut_func_single_param),
                                                           ('k_bind_op', partial_mut_func_single_param),
                                                           ("operator", 1),
                                                           ('ligand_class', None),
                                                           ("bind", 1),
                                                           ('sense_external', tf_ext_sense_mut_func)
                                                           ]
                                                          ),
                           "enz" : collections.OrderedDict([
                                                            ("v_max", partial_mut_func_single_param),
                                                            ("subs_ks", partial_mut_ks_dict_func),
                                                            ("promoter", partial_mut_func_single_param),
                                                            ("operator", 1)]
                                                            )
                           }
    simulate_params['point_mutation_ratios'] = util.PointMutationRatios(
                                                                        v_max = 1,
                                                                        ene_ks = 1,
                                                                        subs_ks = 1,
                                                                        exporting = 1 ,
                                                                        promoter = 1,
                                                                        operator = 1,
                                                                        eff_bound = 1,
                                                                        eff_apo = 1,
                                                                        ligand_ks = 1,
                                                                        k_bind_op = 1,
                                                                        ligand_class = 0,
                                                                        bind = 1,
                                                                        sense_external=1
                                                                        )

    regulatory_mutation_dict = {
                           "pump" : collections.OrderedDict([
                                                             ('translocate',None),
                                                             ('random_insert',None)]
                                                             ),
                           "tf" : collections.OrderedDict([
                                                           ('translocate',None),
                                                             ('random_insert',None)]
                                                          ),
                           "enz" : collections.OrderedDict([
                                                            ('translocate',None),
                                                            ('random_insert',None)]
                                                            )
                                  }
    simulate_params['regulatory_mutation_ratios'] = util.RegulatorytMutationRatios(
                                                                                   translocate=1,
                                                                                   random_insert=1
                                                                        )
    #SIMULATE PARAMETERS
    # integrator params
    simulate_params['burn_in_time'] = 0
    simulate_params['postpone_mutate'] = 0
    simulate_params['absolute_error'] = 0.
    simulate_params['report_frequency'] = 2
    simulate_params['delta_t_between_diff'] = 0.1
    simulate_params['diffusion_constant'] = 0.008
    simulate_params['diffusion_steps'] = 10
    simulate_params['init_step_size'] = 1e-5
    simulate_params['max_retries'] = None
    simulate_params['wait_release_t_diff'] = 100
    simulate_params['num_threads'] = 4
    simulate_params['relative_error'] = 1e-2
    simulate_params['step_function'] = 'rk8pd' #'rkck' #
    simulate_params['retry_steps_factor'] = 2
    simulate_params['rel_err_incr_fact'] = 1.2
    # path options
    simulate_params['base_dir'] = '.'
    simulate_params['load_file'] = None
    simulate_params['source_path'] = os.path.dirname(os.path.realpath(VirtualMicrobes.__file__))
    simulate_params['utility_dir'] = 'utility_files'
    simulate_params['clean_save_path'] = False
    simulate_params['config_files'] = None
    simulate_params['command_line_string'] = None
    # competition
    simulate_params['competition'] = 'local'
    # general
    simulate_params['profile'] = False
    simulate_params['duration'] = 100000
    simulate_params['kill_lineage'] = None  # jeroen
    simulate_params['kill_time'] = None
    simulate_params['proctitle'] = 'virtualmicrobes'
    simulate_params['fluctuate_frequencies'] = [ (0, 0.1), (5000,0.05),(10000,0.01) ]
    simulate_params['fluctuate_extremes'] = False
    simulate_params['evo_grace_time'] = 0
    simulate_params['graphs_single_core'] = True
    simulate_params['graphs_video'] = True
    simulate_params['grid_graph_data_range'] = None
    simulate_params['num_parallel_plot_proc'] = 2
    simulate_params['mark_time'] = 2000
    simulate_params['name'] = 'dummy'
    simulate_params['pop_save_name'] = 'population_snapshot'
    simulate_params['gen_best_save_name'] = 'generation_bests'
    #simulate_params['phylo_plot_time'] = 1000  # DEPRECATED
    simulate_params['living_phylo_units'] = False
    simulate_params['tree_prune_depth'] = 500
    simulate_params['prune_csv_from_time'] = 0
    simulate_params['phylo_types'] = {'Cell':'ancestry', 'GenomicElement':'ancestry', 'Sequence':'base',
                                      'Promoter':'base', 'Chromosome':'ancestry'}
    simulate_params['store_data_time'] = 100
    simulate_params['less_eco_dat'] = False
    simulate_params['plot_time'] = 200
    simulate_params['print_time'] = 100
    simulate_params['skip_plots'] = False
    simulate_params['save_time'] = 5000
    simulate_params['store_save_time'] = 50000
    simulate_params['extra_save_times'] = []
    simulate_params['pop_snapshot_time'] = 1000000000
    simulate_params['pop_best_save_time'] = 100
    simulate_params['regscore_clonesize'] = 100
    simulate_params['show'] = False
    simulate_params['auto_restart'] = None
    # hidden
    simulate_params['mem_limit'] = None # maximum heap memory of this (including children) process 20 GB!
    simulate_params['mem_test'] = False
    simulate_params['load_test'] = False
    simulate_params['marker_names'] = ['lineage', 'metabolic_type']
    simulate_params['phylo_shelf'] = 'phylo_shelf'
    simulate_params['shelve_fraction'] = 0.0
    simulate_params['shelve_time'] = 100000
    simulate_params['environment_stats'] = False
    simulate_params['load_cycle'] = 1
    simulate_params['errand_boy'] = False

    #ENVIRONMENT PARAMETERS
    # grid
    env_params['env_from_file'] = None
    env_params['upgrade_environment'] = False
    env_params['grid_cols'] = 50
    env_params['grid_rows'] = 50
    env_params['per_grid_cell_volume'] = 10.
    env_params['wrap_ew'] = ['diffusion','competition']
    env_params['wrap_ns'] = ['diffusion','competition']
    # influx
    env_params['building_block_influx'] = False
    env_params['bb_class_influx'] = True
    env_params['energy_influx'] = False
    env_params['influx_energy_precursor'] = False
    env_params['fraction_influx'] = 1.
    env_params['prioritize_energy_rich_influx'] = False
    env_params['prioritize_energy_poor_influx'] = False
    env_params['high_energy_bbs'] = False
    env_params['influx'] = None
    env_params['influx_range'] =  util.ParamSpace(base=10, lower=-4.5,upper=-3) # setting influx_range excludes the 'influx' and 'influx_variance_shape' options
    env_params['influx_variance_shape'] = None  #higher shape values give tighter distributions
    env_params['resource_cycle'] = None
    env_params['min_lineage_marking'] = 1
    # metabolismsimu
    #    reaction space
    env_params['nr_cat_reactions'] = 20
    env_params['nr_ana_reactions'] = 30
    env_params['max_cat_path_conv'] = 10
    env_params['max_ana_path_conv'] = 10
    env_params['max_nr_cat_products'] = 2
    env_params['min_cat_energy'] = 1
    env_params['nr_ana_reactants'] = 2
    env_params['max_nr_ana_products'] = 1
    env_params['max_ana_free_energy'] = 1
    env_params['consume_range'] = (1,2)
    env_params['ene_energy_range'] = (1,1)
    env_params['fraction_mol_transports'] = 1.
    env_params['fraction_realized_reactions'] = 1.
    env_params['transport_cost_range'] = (1,1)
    env_params['max_ene_yield'] = 5
    env_params['max_yield'] = 3
    env_params['mol_per_ene_class'] = 2
    env_params['mol_per_res_class'] = 2
    env_params['nr_building_blocks'] = 2
    env_params['nr_cell_building_blocks'] = 2
    env_params['nr_energy_classes'] = 1
    env_params['nr_resource_classes'] = 8
    env_params['pathway_branching'] = 3
    env_params['pathway_convergence'] = 4
    env_params['reaction_schemes'] = [ #ReactionScheme(2,1),
                                      util.ReactionScheme(1,1),
                                      util.ReactionScheme(1,2)] #, ReactionScheme(2,2)]
    env_params['res_energy_range'] = (3,6)
    env_params['prioritize_energy'] = False
    #    dynamics
    env_params['ene_ext_degr_const'] = 0.05
    env_params['bb_ext_degr_const'] = 0.05
    env_params['small_mol_ext_degr_const'] = 0.005
    env_params['degradation_variance_shape'] = 15
    env_params['init_external_conc'] = None
    env_params['init_external_conc_vals'] = None
    env_params['microfluid'] = None
    env_params['chemostat'] = False
    env_params['diff_energy_prop'] = False
    # toxicity
    env_params['toxicity'] = 0.1 # concentration above which the molecule becomes toxic
    env_params['inherit_toxicity'] = False # concentration above which the molecule becomes toxic
    env_params['toxicity_variance_shape'] = 1.5
    # general
    env_params['env_rand_seed'] = 90
    env_params['frac_horizontal_bar'] = 0.
    env_params['max_frac_horizontal'] = 0.
    env_params['frac_vertical_bar'] = 0.
    env_params['max_frac_vertical'] = 0.
    env_params['barrier_neighborhoods'] = ['diffusion', 'competition']
    env_params['influx_rows'] = None #range(5, 50, 10)
    env_params['influx_cols'] = None #range(5, 50, 10)
    env_params['grid_sub_div'] =  util.GridSubDiv(row=1, col=1)
    env_params['sub_env_part_influx'] = None
    env_params['sub_env_influx_combinations'] = None
    env_params['cells_grid_diffusion'] = 0.
    env_params['perfect_mix'] = None
    #POPULATION PARAMETERS
    # mutation
    pop_params['cells_from_files'] = None
    pop_params['cell_files_query'] = None
    pop_params['evo_rand_seed'] = 42
    pop_params['mutation_param_space'] = util.MutationParamSpace(base=None, lower=-0.5,
                                                            upper=0.5, min=0.05, max=10.,
                                                            uniform=True,randomize=0.1)
    pop_params['mutation_rates'] = util.MutationRates(chrom_dup=0.05,
                                                     chrom_del=0.05,
                                                     chrom_fiss=0.02,
                                                     chrom_fuse=0.02,
                                                     point_mutation=0.01,
                                                     tandem_dup=0.001,
                                                     stretch_del=0.001,
                                                     stretch_invert=0.001,
                                                     stretch_translocate=0.001,
                                                     stretch_exp_lambda=0.5,
                                                     external_hgt=0.00001,
                                                     internal_hgt=0.00005,
                                                     regulatory_mutation=0.01,
                                                     reg_stretch_exp_lambda=0.02,
                                                     uptake_mutrate=0.0)
    pop_params['exclude_gene_from_mutation'] = []
    pop_params['universal_mut_rate_scaling'] = 1.
    pop_params['hgt_at_div_only'] = False
    pop_params['hgt_donor_scaling'] = False
    pop_params['hgt_self'] = False
    pop_params['hgt_acceptor_scaling'] = False
    pop_params['point_mutation_dict'] = point_mutation_dict
    pop_params['regulatory_mutation_dict'] = regulatory_mutation_dict
    pop_params['rand_gene_params'] = util.ParamSpace(base=10, lower=-.5 ,upper=.5)
    # genome
    pop_params['chromosome_compositions'] = [util.GeneTypeNumbers(tf=10, enz=10, pump=10)]
    pop_params['circular_chromosomes'] = False
    pop_params['prioritize_influxed_metabolism'] = True
    pop_params['pop_rand_seed'] = 414
    pop_params['operator_seq_len'] = 50
    pop_params['better_tf_params'] = False #Only use when you know what this does ;D See virtualmicrobes.py
    pop_params['binding_seq_len'] = 10
    pop_params['tf_binding_cooperativity'] = 1
    pop_params['ligand_binding_cooperativity'] = 1
    pop_params['min_bind_score'] = 0.85
    # internal dynamics
    pop_params['building_block_stois'] = (1,1)
    pop_params['cell_init_volume'] = 1.
    pop_params['max_cell_volume'] = 5
    pop_params['min_cell_volume'] = 0.2
    pop_params['cell_growth_rate'] = 0.4
    pop_params['cell_shrink_rate'] = 0.1
    pop_params['cell_growth_cost'] = 0.5
    pop_params['uptake_dna'] = 1.0              # = multiplier of native HGT rate. Can be evolvable
    pop_params['cell_division_volume'] = 2.
    pop_params['growth_rate_scaling'] = 1.
    pop_params['transcription_cost'] = 0.001
    pop_params['energy_transcription_cost'] = 0.001
    pop_params['energy_transcription_scaling'] = 0.001
    pop_params['homeostatic_bb_scaling'] = 0
    pop_params['init_prot_mol_conc'] = 1.# 1.
    pop_params['gene_product_conc_cutoff'] = 1e-6
    pop_params['init_small_mol_conc'] = 0. #.005
    pop_params['product_degradation_rate'] = 0.07
    pop_params['prot_degr_const'] = 1.
    pop_params['prot_diff_const'] = None
    pop_params['small_mol_degr_const'] = None # when None, it is the same as external degradation rate
    pop_params['small_mol_diff_const'] = 0.005
    pop_params['ene_degr_const'] = None # when None, it is the same as external energy degradation rate
    pop_params['bb_degr_const'] = None
    pop_params['ene_diff_const'] = 0.005
    pop_params['v_max_growth'] = 10
    pop_params['energy_for_growth'] = False
    pop_params['divide_cell_content'] = False
    pop_params['no_death_frac'] = None
    pop_params['deathrate_density_scaling'] = None
    #pop_params['divide_conc_factor'] = 1. # deprecated; if divide_cell_content == True, divide equally between parent and offspring
    pop_params['spill_conc_factor'] = 0.
    pop_params['spill_product_as_bb'] = False
    pop_params['transporter_membrane_occupancy'] = 0.
    pop_params['enzyme_volume_occupancy'] = 0.
    # population dynamics
    pop_params['base_death_rate'] = 0.01
    pop_params['stochastic_death'] = True
    pop_params['init_pop_size'] = None
    pop_params['max_cells_per_locality'] = 1
    pop_params['max_die_off_fraction'] = None #1.
    pop_params['wipe_population'] = None
    pop_params['min_wipe_survivors'] = None
    pop_params['wipe_poisson'] = False
    #pop_params['measured_non_scaling'] = 1.5
    pop_params['non'] = 1
    pop_params['competition_scaling'] = 1 # raise production to this power when computing competition values of competing cells
    pop_params['life_time_prod'] = False
    pop_params['product_spending_fraction'] = 0.
    pop_params['product_toxicity'] = 5.
    pop_params['reproduction_cost'] = None
    pop_params['reproduce_size_proportional'] = None
    pop_params['reproduce_neutral'] = None
    pop_params['historic_production_weight'] = 1.
    pop_params['reset_historic_max'] = 0.
    pop_params['max_historic_max'] = None
    pop_params['start_scaling_selection_pressure'] = 0  # Default = always, but for initialisation period you can skip the first n timesteps
    pop_params['scale_prod_hist_to_pop'] = False
    pop_params['historic_production_window'] = 1000
    pop_params['selection_pressure'] = 'historic_window_scaled' # 'constant' ; 'current_scaled' , historic_window_scaled
    pop_params['toxic_building_blocks'] = True
    pop_params['toxicity_scaling'] = 10.
    # general params
    pop_params['single_clone_init'] = False

    return simulate_params, env_params, pop_params

def load_simulation(file_name, **param_updates):
    param_updates['load_file'] = file_name
    sim = load_sim(file_name, **param_updates)
    keep_unrecognized = False
    if param_updates.has_key('run_type') and param_updates['run_type'] == 'ancestry':
        keep_unrecognized = True
    sim.update_sim_params(update_default_params(keep_unrecognized=keep_unrecognized, **sim.params))
    sim.system.population.update_cell_params()
    sim.store_command_line_string()
    return sim

def update_default_params(keep_unrecognized=False, verbose=False, **kwargs):
    '''
    Use simulate_params, pop_params and env_params as defaults and overwrite
    them with kwargs to construct a parameter dictionary. Warn for all kwargs
    that have not been consumed. ( default_params() generates all default
    parameters )

    :param simulate_params: dictionary with general simulation parameters
    :param pop_params: dictionary with population specific parameters
    :param env_params: dictionary with environment specific params
    '''

    simulate_params, env_params, pop_params = default_params()

    params=dict() # NOTE: unordered ok
    for (param, default) in pop_params.iteritems():
        params[param] = kwargs.pop(param, default)
        if verbose:
            print param, params[param]
    for (param, default) in env_params.iteritems():
        params[param] = kwargs.pop(param, default)
        if verbose:
            print param, params[param]
    for (param, default) in simulate_params.items():
        params[param] = kwargs.pop(param, default)
        if verbose:
            print param, params[param]

    if params['init_pop_size'] is None and params['env_from_file'] is None:
        params['init_pop_size'] = params['grid_rows'] * params['grid_cols'] * params['max_cells_per_locality']

    for k,v in kwargs.items():
        if keep_unrecognized:
            params[k] = v
        else:
            warnings.warn('unrecognized option {0}={1}'.format(k,v))

    params_dict = util.pickles_adict(params, recursive=False)
    return params_dict

def create_simulation(**param_updates):
    params_dict = update_default_params(**param_updates)
    sim = ODE_simulation(params_dict)
    sim.copy_config_files()
    sim.store_command_line_string()
    return sim
