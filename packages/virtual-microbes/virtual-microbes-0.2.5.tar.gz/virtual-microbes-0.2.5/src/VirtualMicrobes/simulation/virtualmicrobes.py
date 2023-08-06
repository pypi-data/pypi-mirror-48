#! /usr/bin/env python
# -*- coding: utf-8 -*-
'''
Command Line Interface to the Virtual Microbes Evolutionary Simulator package.


@copyright:  2014 Theoretical Biology and Bioinformatics. All rights reserved.

@license:    MIT licence

@contact:    thomas.cuypers@gmail.com
@deffield    updated: Updated
'''



from argparse import ArgumentParser, Namespace
import argparse
from setproctitle import setproctitle
import sys, os, inspect
import warnings

import VirtualMicrobes
from VirtualMicrobes.my_tools.utility import GeneTypeNumbers, ParamSpace, MutationRates, \
    ReactionScheme, multifile, PopulationWipe, GridSubDiv, processify, \
    PointMutationRatios, RegulatorytMutationRatios, ugly_globals, errand_boy_server, TracePrints
import cPickle as pickle

#Find the path of the currently invoked virtualmicrobes.py script and put its parent directory on sys.path.
cmd_folder = os.path.realpath(os.path.abspath(os.path.split(inspect.getfile( inspect.currentframe() ))[0]))
sys.path.insert(0,os.path.join(cmd_folder,'..'))


setproctitle('virtualmicrobes')

__author__ = """\n""".join(['Thomas Cuypers (thomas.cuypers@gmail.com)',
                            'Bram van Dijk (bramvandijk88@gmail.com)'])
__all__ = []
__version__ = '0.2.4'
__date__ = '2014-10-07'
__updated__ = '2018-10-08'

DEBUG = 0
TESTRUN = 1
PROFILE = 0

class CLIError(Exception):
    '''Generic exception to raise and log different fatal errors.'''
    def __init__(self, msg):
        super(CLIError).__init__(type(self))
        self.msg = "E: %s" % msg
    def __str__(self):
        return self.msg
    def __unicode__(self):
        return self.msg


def key_value_opt(opt_string, key_type=None, val_type=None):
    'opt_strings should be of the form: "key=val" or "key:val"'
    if '=' in opt_string:
        k,v = opt_string.split('=')
    elif ':' in opt_string:
        k,v = opt_string.split(':')
    else:
        raise Exception, ('option string {0} is not in the format of "key:value" '
                          'or "key=value" format ').format(opt_string)
    if key_type is not None:
        k = key_type(k)
    if val_type is not None:
        v = val_type(v)
    return k,v

class OptionDict(argparse._StoreAction):
    def __init__(self,option_strings,
                 dest=None,
                 nargs='*',
                 default=None,
                 required=False,
                 type=None,
                 metavar=None,
                 help=None,
                 const=None):

        super(OptionDict, self).__init__(
            option_strings=option_strings,
            dest=dest,
            nargs=nargs,
            default=default,
            required=required,
            metavar=metavar,
            type=type,
            help=help)
        self.const = const

    def __call__(self, parser, namespace, values, option_string=None):
        if self.default == argparse.SUPPRESS:
            # This is the case where default values have been repressed when
            # reloading data. Now values is considered to fully specify the the
            # attribute skipping the 'refining' step. Error handling is delegated
            # to post initialization of the attribute.
            super(OptionDict, self).__call__(parser, namespace, dict(values), option_string )
        elif not values:
            setattr(namespace, self.dest, self.const)
        else:
            final_dict = dict()
            try:
                for k,v in values:
                    final_dict[k] = v
            except:
                raise Exception, 'action should be called on a list of (key,value) tuples, not {0}'.format(values)
            setattr(namespace, self.dest, final_dict)


class RefineDefaultDict(OptionDict):
    def __init__(self, *args, **kwargs):
        super(RefineDefaultDict, self).__init__(*args, **kwargs)

    def __call__(self, parser, namespace, values, option_string=None):
        if self.default == argparse.SUPPRESS:
            # This is the case where default values have been repressed when
            # reloading data. Now values is considered to fully specify the the
            # attribute skipping the 'refining' step. Error handling is delegated
            # to post initialization of the attribute.
            super(RefineDefaultDict, self).__call__(parser, namespace, dict(values), option_string )
        else:
            final_dict = self.default.copy()
            try:
                for k,v in values:
                    if k not in final_dict:
                        raise Exception, '{0} is not a valid parameter to set for {1}'.format(k,option_string)
                    final_dict[k] = v
            except:
                raise Exception, 'action should be called on a list of (key,value) tuples, not {0}'.format(values)
            setattr(namespace, self.dest, final_dict)

class DefaultsAndTypesHelpFormatter(argparse.HelpFormatter):
    def _get_help_string(self, action):
        help = action.help
        if '%(default)' not in action.help:
            if action.default is not argparse.SUPPRESS:
                defaulting_nargs = [argparse.OPTIONAL, argparse.ZERO_OR_MORE]
                if action.option_strings or action.nargs in defaulting_nargs:
                    help += ' (default: %(default)s)'
                if action.type:
                    help += ' (type: %(type)s)'
        return help

def tp_rate_change(s):
    try:
        tp, rate =  s.split(',')
        tp, rate = int(tp), float(rate)
        if 1.< rate < 0:
            raise Exception, 'rate should be between 0 and 1, not {0}'.format(rate)
        return tp, rate
    except:
        raise argparse.ArgumentTypeError("Range must be low,high")

def value_or_range(s, type_=int):
    try:
        val = type_(s)
        return val, val
    except ValueError:
        pass
    try:
        low, high = map(type_, s.split(','))
        if high < low:
            raise Exception, 'high:{0} < low:{1}, check input string'.format(high, low)
        return low, high
    except:
        raise argparse.ArgumentTypeError("Value or range must be tuple: int,int or single val: int")

def value_range(s, type_=int):
    try:
        low, high = map(type_, s.split(','))
        if high < low:
            raise Exception, 'high:{0} < low:{1}, check input string'.format(high, low)
        return low, high
    except:
        raise argparse.ArgumentTypeError("Range must be low,high")

def distribution_range(s, type_=float):
    try:
        lower, upper, base = map(type_, s.split(','))
        if upper < lower:
            raise Exception, 'upper:{0} < lower:{1}, check input string'.format(upper, lower)
        return lower, upper, base
    except:
        raise argparse.ArgumentTypeError("Distribution must be lower, upper, base")

def to_population_wipe(s):
    try:
        interval, fraction = s.split(',')
        return PopulationWipe(int(interval), float(fraction))
    except:
        raise argparse.ArgumentTypeError('PopulationWipe should be of the form interval,fraction with and types int,float')

def to_gene_type_numbers(s):
    try:
        d = dict(map(lambda x: key_value_opt(x.strip(), str, int), s.split(',')))
        return GeneTypeNumbers(**d)
    except:
        raise argparse.ArgumentTypeError('gene type numbers are 3-tuples of the form "tf=x,enz=y,pump=z" , where x,y and z are integers')

def to_grid_sub_div(s):
    try:
        d = dict(map(lambda x: key_value_opt(x.strip(), str, int), s.split(',')))
        return GridSubDiv(**d)
    except:
        raise argparse.ArgumentTypeError('grid sub divisions are tuples of the form "row=x,col=y" , where x and y are integers')


def to_reaction_scheme(s):
    try:
        return ReactionScheme( *map(int, s.split(',') ) )
    except:
        raise argparse.ArgumentTypeError('reaction schemes are of the form "n,m" , where n and m are integers')

def float_or_int(s):
    try:
        return int(s)
    except ValueError:
        return float(s)

def str_or_int(s):
    try:
        return int(s)
    except ValueError:
        return s

def abs_path(p):
    return os.path.abspath(p)

#http://stackoverflow.com/a/25536834/4293557
def convert_arg_line_to_args(arg_line):
    '''override method of ArgParser to enable reading options from file as options
    with values on a single line.
    e.g.
    --name test
    --chromosome-sizes 5 5 5
    '''
    for arg in arg_line.split():
        if not arg.strip():
            continue
        yield arg.strip()

def suppress_defaults(actions_container, exclude=[]):
    if not isinstance(actions_container, argparse._ActionsContainer):
        raise Exception, 'not an argparse._ActionsContainer'
    for action in actions_container._actions:
        if action.dest not in exclude:
            action.default = argparse.SUPPRESS

def parse_special_params(args):
    try:
        args.mutation_rates = MutationRates(**args.mutation_rates)
    except AttributeError: # when a simulation is reloaded, default arguments are suppressed and
        # some this parameter may not have been reset on the command line ( its values stored internally in
        # the simulation object )
        pass
    try:
        args.point_mutation_ratios = PointMutationRatios(**args.point_mutation_ratios)
    except AttributeError:
        pass
    try:
        args.regulatory_mutation_ratios = RegulatorytMutationRatios(**args.regulatory_mutation_ratios)
    except AttributeError:
        pass
    try:
        if args.influx_range is not None:
            args.influx_range = ParamSpace(**args.influx_range)
    except AttributeError:
        pass
    try:
        args.rand_gene_params = ParamSpace(**args.rand_gene_params)
    except AttributeError:
        pass
    #try:
    #    if args.init_pop_size is None and args.env_from_file is None:
    #        args.init_pop_size = args.grid_rows * args.grid_cols * args.max_cells_per_locality
    #except AttributeError:
    #    pass

def print_sim_params(args):
    import VirtualMicrobes.simulation.Simulation as simu
    params = simu.load_sim_params(args.pop_save)
    for param, value in params.items():
        print param, ':', value

@processify
def init_and_simulate(sim_mod , lf=None, options={}, debug_write=False):
    if lf is None:
        if options['load_file'] is not None:
            sim = sim_mod.load_simulation(options['load_file'], **options)
        else:
            sim = sim_mod.create_simulation(**options)
    else:
        sim = sim_mod.load_simulation(lf, **options)

    result = None
    with multifile([sim.log_file, sys.stdout]) as sys.stdout, multifile([sim.error_log_file, sys.stderr]) as sys.stderr:

        if debug_write:
            sys.stdout = TracePrints()

        try:
            result = sim.simulate()
        except MemoryError:
            print 'Simulation exceeded upper heap memory bound of {}. Ending simulation'.format(sim.params.mem_limit)
    return result

def start_evo_sim(args):
    try:
        setproctitle(args.proctitle)
    except AttributeError:
        setproctitle('virtualmicrobes')

    import VirtualMicrobes.simulation.class_settings as cs
    # Note: above import should be BEFORE import of Simulation or any of its dependencies!
    # This is so that the parameterization of class code via command
    # line options (e.g. --phylo-types ) can have an effect

    # IMPORTANT ADDITION! IF YOU REMOVE THE LINE BELOW EVERYTHING WILL FAIL!
    print '\n\n                  .///////////////////////////////////////,                    \n              ,////////\033[0;32m*******************************\033[0m////////*                \n            /////\033[0;32m...........................................\033[0m/////              \n          ////\033[0;32m.....................,...........................\033[0m////            \n         ///\033[0;32m,...................,\033[0m/.//*\033[0;32m..............\033[0m/*///\033[0;32m........\033[0m///.          \n        ///\033[0;32m,,,,,,.,,............\033[0m/. ///\033[0;32m.............\033[0m** ,//\033[0;32m,........\033[0m///,         \n       \033[0m///\033[0;32m,,,,,,,,,,,,,,,,,,,,,.\033[0m//////\033[0;32m,............\033[0m//////\033[0;32m,.........\033[0m///         \n      *//*\033[0;32m,,,,,,,,,,,,,,,,,,,,,,,\033[0m////*\033[0;32m,,,..........,\033[0m/////\033[0;32m..........,\033[0m///        \n      ///\033[0;32m,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,........\033[0m///        \n      ///\033[0;32m,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,\033[0m///        \n      ///\033[0;32m,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,\033[0m///        \n      ///\033[0;32m,,,,,,,,,,,,,,,,,,,,,,,,,\033[0m///*\033[0;32m,,,,,,,,,,,,,,\033[0m*////\033[0;32m,,,,,,,,,,,\033[0m///        \n      ///\033[0;32m,,,,,,,,,,,,,,,,,,,,,,,,\033[0m////////////////////////\033[0;32m,,,,,,,,,,,\033[0m///        \n      ///\033[0;32m,,,,,,,,,,,,,,,,,,,,,,,,,,,,,\033[0m*///////////**\033[0;32m,,,,,,,,,,,,,,,,\033[0m///        \n      ///\033[0;32m,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,\033[0m///        \n      *//\033[0;32m**,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,\033[0m///        \n       ///\033[0;32m**********,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,\033[0m///.        \n       ,///\033[0;32m************************,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,\033[0m////         \n        ,///\033[0;32m*************************************,,,,,,,,,,,,,,,,\033[0m////          \n          ////\033[0;32m**************************************************\033[0m///.           \n           ,////\033[0;32m*********************************************\033[0m////*             \n              ///////\033[0;32m***********************************\033[0m///////.               \n                 ,/////////////////////////////////////////,                   \n\n                 ,*****************************************,\n                 ,*************VIRTUALMICROBES*************,                   \n                 ,*****************************************,                   \n'

    if args.load_file is None:
        try:
            cs.phylo_types.update(args.phylo_types)
        except AttributeError:
            raise
    #init matplotlib with backend depending on whether we intend to 'show' the plots
    if not args.show:
        import matplotlib
        matplotlib.use('Agg')
    elif not args.graphs_single_core:
        print 'option --show not possible without --graphs-single-core'
        return 1

    options = vars(args)

    if options.get('profile',False):
        ugly_globals['profile'] = True
    if options.get('monkey_patch_mpl', False):
        from VirtualMicrobes.my_tools.monkey import MyArtist, MyFigure, MyTransformWrapper
        matplotlib.artist.Artist = MyArtist
        matplotlib.figure.Figure = MyFigure
        matplotlib.transforms.TransformWrapper = MyTransformWrapper

    for opt in ['start', 'run_type','load_params', '__dummy', 'monkey_patch_mpl']:
        try:
            del options[opt]
        except KeyError:
            pass

    if options.get('args.graphs_single_core', None) is not None:
        ugly_globals['graphs_as_subprocesses'] = not args.graphs_single_core

    if args.load_file is not None:
        load_file = file(args.load_file, 'r')
        # load the metaclass settings of phylotypes
        saved_phylo_types = pickle.load(load_file)
        cs.phylo_types.update(saved_phylo_types)
        print 'Setting loaded phylo_types:'
        for name, tp in cs.phylo_types.items():
            print name, ':', tp

    if options.get('mem_limit',None) is not None:
        import resource
        rsrc = resource.RLIMIT_AS
        soft, hard = resource.getrlimit(rsrc)
        print 'Memory limit starts as  :', soft

        resource.setrlimit(rsrc, (args.mem_limit, hard)) #limit to one kilobyte
        soft, hard = resource.getrlimit(rsrc)
        print 'Memory limit changed to :', soft


    import VirtualMicrobes.simulation.Simulation as simu
    intermediate_load_file, _options = None, options
    if options.get('errand_boy', False):
        with errand_boy_server() as (errand_server, socket_path):
            if errand_server.is_alive():
                print 'errand-boy server is alive and listening on {}'.format(socket_path)
            else:
                warnings.warn('No subprocess server running, ending simulation.')
                return
            from errand_boy.transports.unixsocket import UNIXSocketTransport
            # This will run a subprocess server that will handle subsequent subprocess.Popen calls
            # by running them on this server process.
            # The benefit of this is that it avoids the (huge) memory overhead when the regular
            # subprocess.Popen call calls os.fork(), effectively doubling memory footprint and which risks
            # running out of memory.
            errand_boy_transport = UNIXSocketTransport(socket_path=socket_path)
            with errand_boy_transport.get_session() as session:
                import subprocess
                subprocess.Popen = session.subprocess.Popen # redefine all subprocess.Popen calls
                while True:
                    result = init_and_simulate(simu, intermediate_load_file, _options)
                    try:
                        intermediate_load_file, _options = result
                    except TypeError:
                        pass
                    if result is None:
                        print 'Done simulating.'
                        break

    else:
        while True:
            result = init_and_simulate(simu, intermediate_load_file, _options)
            try:
                intermediate_load_file, _options = result
            except TypeError:
                pass
            if result is None:
                print 'Done simulating.'
                break

def start_lod_analysis(args):
    setproctitle('virtualmicrobes'+'_ancestry')
    load_fn = args.pop_save
    param_updates = vars(args)

    import VirtualMicrobes.simulation.class_settings as cs
    load_file = file(load_fn, 'r')
    # load the metaclass settings of phylotypes
    saved_phylo_types = pickle.load(load_file)
    cs.phylo_types.update(saved_phylo_types)
    print 'Setting loaded phylo_types:'
    for name, tp in cs.phylo_types.items():
        print name, ':', tp

    if not param_updates.has_key('base_dir'):
        param_updates['base_dir'] = os.path.dirname(load_fn) #this works because we change 'args' by reference
    import matplotlib
    matplotlib.use('Agg')

    options = vars(args)
    del options['start']
    del options['run_type']

    if options.get('monkey_patch_mpl', False):
        from VirtualMicrobes.my_tools.monkey import MyArtist, MyFigure, MyTransformWrapper
        matplotlib.artist.Artist = MyArtist
        matplotlib.figure.Figure = MyFigure
        matplotlib.transforms.TransformWrapper = MyTransformWrapper
        del options['monkey_patch_mpl']

    import VirtualMicrobes.post_analysis.lod as lod
    #sim = simu.load_simulation(args.pop_save, **param_updates)
    with lod.LOD_Analyser(args) as analyser:
        if args.lod_stats: # we have to do this before comparing saves, because the global linker dict of simulations
            # overwrite eachother. This happens when doing compare_to_pops, which loads
            # a sequence of population saves into the analysis.
            analyser.lod_stats()

        if args.lod_network_stats:
            analyser.lod_network_stats()
        if args.lod_cells:
            analyser.lod_cells(runtime=analyser.ref_sim.run_time)
        if args.anc_cells:
            analyser.anc_cells(runtime=analyser.ref_sim.run_time)
        if args.pop_cells:
            analyser.pop_cells(runtime=analyser.ref_sim.run_time)
        if args.lod_bind_cons:
            analyser.lod_binding_conservation()
        if args.lod_graphs:
            analyser.lod_graphs()
        if args.lod_time_courses:
            analyser.lod_time_courses()
        if args.lod_time_course_plots:
            analyser.lod_time_course_plots()
        if args.newick_trees:
            analyser.write_newick_trees()
        analyser.draw_ref_trees()
        # compare_to_pops has to be the last method because it changes the global
        # state of the phylo_linker_dict every time a new pop snapshot is loaded for
        # compare analysis.
        # Therefore, no more PopulationHistory methods should be invoked on the
        # reference simulation.
        if args.compare_saves is not None:
            analyser.compare_to_pops()


def start_competition_sim(args):
    pass


def check_growth_params(args):
    if (args.max_cell_volume is None or args.cell_division_volume or args.cell_growth_rate is None or
        args.cell_shrink_rate is None):
        return
    volume_overshoot = ( args.max_cell_volume - args.cell_division_volume ) / args.cell_division_volume
    shrink_fact = args.cell_shrink_rate / (args.cell_growth_rate - args.cell_shrink_rate)
    can_divide = volume_overshoot > shrink_fact
    if not can_divide:
        max_vol_minimum = (1 + shrink_fact) * args.cell_division_volume
        warnings.warn('Max volume not high enough to reach cell division volume. It should be higher than {}.'.format(max_vol_minimum))


def main(argv=None): # IGNORE:C0111
    '''Command line options.'''

    if argv is None:
        argv = sys.argv
    else:
        sys.argv.extend(argv)

    program_name = os.path.basename(sys.argv[0])
    program_version = "v%s" % __version__
    program_build_date = str(__updated__)
    program_version_message = '%%(prog)s %s (%s)' % (program_version, program_build_date)
    program_shortdesc = __import__('__main__').__doc__.split("\n")[1]
    program_license = '''%s

  Created by thocu on %s.
  Copyright 2014 Theoretical Biology and Bioinformatics. All rights reserved.

  Licensed under the Apache License 2.0
  http://www.apache.org/licenses/LICENSE-2.0

  Distributed on an "AS IS" basis without warranties
  or conditions of any kind, either express or implied.

USAGE
''' % (program_shortdesc, str(__date__))

    # inject the raw command line into the sys.argv as parameter of --command-line-string
    sys.argv[1:1] = ['--command-line-string', '"'+' '.join(sys.argv)+'"']

    # Filter configuration files from the command line options so that they can
    # be injected as an option argument. Now we can copy the files to the save
    # directory of the simulation.
    cfg_file_char = '@'
    cfg_files = filter(lambda s: len(s) > 0 and s[0] == cfg_file_char, sys.argv)

    #print cfg_files

    if len(cfg_files):
        new_opt = ['--config-files']+ map(lambda fn: fn.lstrip(cfg_file_char), cfg_files)
        print new_opt
        sys.argv[1:1] = new_opt

    parser = ArgumentParser(description=program_license, fromfile_prefix_chars=cfg_file_char,
                            formatter_class=DefaultsAndTypesHelpFormatter)
    parser.convert_arg_line_to_args = convert_arg_line_to_args
    pop_par = parser.add_argument_group('population options (shared)')
    env_par = parser.add_argument_group('environment options (shared)')
    sim_par = parser.add_argument_group('simulation options (shared)')

    subparsers = parser.add_subparsers(help='sub-command specific arguments', dest='run_type')
    parser.add_argument('-', dest='__dummy',   # dummy option to parsing of subcommand positional argument
                        action="store_true", help=argparse.SUPPRESS)
    parser.add_argument('--monkey-patch-mpl', action='store_true', help=argparse.SUPPRESS )
    parser.add_argument('--config-files', type=str, nargs='+',help=argparse.SUPPRESS )
    parser.add_argument('--command-line-string', type=str, help=argparse.SUPPRESS)
    parser.add_argument('--profile', action='store_true', help=argparse.SUPPRESS)

    ####  options not implemented in command line parsing ####
    # mem-test
    # shelve-fraction
    # burn-in-time
    ####

    ####  notes on parameter combinations ####

    ## biological interpretation not well defined:
    # combining divide-cell-content and cell-division-volume:
    #    when a cell-division volume is set the volume of parent and offspring cells will be halved
    #    effectively redistributing molecules in the original parent. Choosing divide-cell-content
    #    simultaneously is superfluous.

    # spilling cell contents (spill-conc-factor > 0) without either dividing cell contents or dividing
    # the cell volume is biologically not well defined. In this case matter is created at cell
    # division (effectively doubling the existing molecular content in the parent.
    ####

    ######################## Ancestry options ###########################
    lod_parser = subparsers.add_parser('ancestry', help='analysis of the line of descent',
                            formatter_class=DefaultsAndTypesHelpFormatter)
    lod_parser.set_defaults(start=start_lod_analysis)

    lod_parser.add_argument('pop_save', type=str,
                            help='file with reference population to start ancestor trace'
                            )
    lod_parser.add_argument('--nr-lods', type=int,
                            default=1,
                            help='number of (most diverged) lines of descent to reconstruct and anlyse'
                            )
    lod_parser.add_argument('--name', type=str,
                            default='ancestry',
                            help='name of base save directory for ancestry analysis'
                            )
    lod_parser.add_argument("--test-rand-seed", type=int,
                            default=91,
                            help="ancestry analysis test seed"
                            )
    lod_parser.add_argument('--compare-saves', type=str_or_int, nargs='+',
                            default=None,
                            help=('intermediate population saves for ancestor '
                                  'comparison. Can be either a list of file '
                                  ' names or a list of time points (for which '
                                  ' simulation saves should exist in the simulation'
                                  ' directory.')
                            )
    lod_parser.add_argument('--prune-compare-pop', type=int,
                            default=500,
                            help='how much should the crown of phylogenetic trees be pruned in time steps')
    lod_parser.add_argument('--skip-store', action='store_true',
                            help='skip setting up ancestry store. E.g. when only printing simulation snapshot data'
                            )
    lod_parser.add_argument('--leafs-sample-size', type=int,
                            default=100,
                            help='the (maximum) number of leafs to sample for individual ancestor tracing'
                            )
    mut_ex_group = lod_parser.add_mutually_exclusive_group()
    mut_ex_group.add_argument('--lod-generation-interval', type=int, const=500, nargs='?',
                            help='interval in generations for line of descent data analysis'
                            )
    mut_ex_group.add_argument('--lod-time-interval', type=int, const=10000, nargs='?',
                            help='interval in time points for line of descent data analysis'
                            )
    lod_parser.add_argument('--lod-range', type=lambda s:(value_range(s,float)),
                            help=('Restrict the set of ancestors to a range. Give as lower_fract,upper_fract '
                                  '(e.g. --lod-range 0.2,0.8). This restricts ancestor analysis to '
                                  'the range [lower_fract*len(ancestors):upper_fract*len(ancestors)]'
                                  )
                            )
    lod_parser.add_argument('--time-course-chunk-size', type=int,
                            default=100,
                            help=('Number of generations to concatenate in time course chunks.'
                                  )
                            )
    lod_parser.add_argument('--lod-stats', action='store_true')
    lod_parser.add_argument('--lod-cells', action='store_true')
    lod_parser.add_argument('--anc-cells', action='store_true')
    lod_parser.add_argument('--pop-cells', action='store_true')
    lod_parser.add_argument('--prune-pop-cells',type=int,default=0)
    lod_parser.add_argument('--lod-network-stats', action='store_true')
    lod_parser.add_argument('--lod-bind-cons', action='store_true')
    lod_parser.add_argument('--lod-graphs', action='store_true')
    lod_parser.add_argument('--lod-time-courses', action='store_true')
    lod_parser.add_argument('--lod-time-course-plots', action='store_true')
    lod_parser.add_argument('--newick-trees', action='store_true')
    lod_parser.add_argument('--no-reconstruct-grn', dest='reconstruct_grn', action='store_false',
                            help=argparse.SUPPRESS)
    lod_parser.add_argument('--image-formats', type=str, nargs='+', choices=['png', 'svg'],
                            default=['png'], help='Formats for image plotting. Multiple formats at the same time possible.')

    ######################## Evo simulation options #####################
    evo_parser = subparsers.add_parser('evo', help='evolutionary simulation',
                            formatter_class=DefaultsAndTypesHelpFormatter)
    env_init = evo_parser.add_argument_group('environment initialization')
    pop_init = evo_parser.add_argument_group('population initialization')
    evo_parser.set_defaults(start=start_evo_sim)

    # GENERAL

    evo_parser.add_argument('-d', '--duration', type=int,
                             default=100000,
                             help="duration of simulation in numbers of reproduction steps"
                             )
    evo_parser.add_argument('--evo-grace-time', type=int ,
                             default= 0,
                             help=('time at which mutations will start')
                             )
    evo_parser.add_argument('--mark-time', type=int ,
                            default=100000 ,
                            help='time between applying new (unique) markers to the population'
                            )
    evo_parser.add_argument('--phylo-types', type=lambda x: key_value_opt(x, key_type=str, val_type=str),
                            action=RefineDefaultDict, nargs='+',
                            default= {'Cell':'ancestry',
                                      'GenomicElement':'base',
                                      'Chromosome':'base',
                                      'Sequence':'base',
                                      'Promoter':'base'},
                            help=('phylogeny types for classes. These determine whether'
                                  ' phylogenetic structures and data can be analyzed for the respective classes.'
                                  ' specify as space separated key:value pairs, e.g.'
                                  ' --phylo-types Cell=ancestry Promoter=base overrides the defaults for'
                                  ' Cell and Promoter. choose phylotype from [base, ancestry] ')
                            )
    evo_parser.add_argument('--load-file', type=str,
                            default=None,
                            help='load a population from file (name) containing a population dump'
                            )
    evo_parser.add_argument('--name', type=str ,
                            help='name of simulation. Used as base directory name for simulation data.'
                            )
    evo_parser.add_argument('--store-data-time', type=int,
                            default=100,
                            help='time interval for saving run data')
    evo_parser.add_argument('--less-eco-dat', action='store_true',
                            help='store ecology (grid) data only when plotting (see --plot-time).'
                            )
    evo_parser.add_argument('--no-less-eco-dat', dest='less_eco_dat', action='store_false',
                            help=argparse.SUPPRESS
                            )
    evo_parser.add_argument('--phylo-plot-time', type=int,
                            default=1000,
                            help='plot the phylogenetic tree'
                            )
    evo_parser.add_argument('--living-phylo-units', action='store_true',
                            default=False,
                            help='plot the phylogenetic tree including all the living individuals (mem heavy)'
                            )
    evo_parser.add_argument('--no-living-phylo-units', dest='living_phylo_units', action='store_false',
                            help=argparse.SUPPRESS
                            )
    evo_parser.add_argument('--plot-time', type=int ,
                            default=200,
                            help='frequeny of data plotting in generation steps'
                            )
    evo_parser.add_argument('--print-time', type=int ,
                            default=100,
                            help='frequeny of printing'
                            )
    evo_parser.add_argument('--skip-plots', action='store_true', default=False,
                         help=argparse.SUPPRESS)
    evo_parser.add_argument('--no-skip-plots', dest='skip_plots', action='store_false',
                            default=True,
                         help=argparse.SUPPRESS)
    evo_parser.add_argument('--prune-csv-from-time', type=int,
                            default=0,
                            help='time cutoff to prune CSV files containing simulation data when continueing previous simulation'
                            )
    evo_parser.add_argument('--save-time', type=int ,
                            default=5000,
                            help='interval for creating a dump of the simulation as <name>.sav and reloading (memory release)'
                            )
    evo_parser.add_argument('--store-save-time', type=int ,
                            default=50000,
                            help='interval at which saves should be backed up as <name>_<time>.sav'
                            )
    evo_parser.add_argument('--extra-save-times', type=int , nargs='+',
                            default=[],
                            help='extra times for creating a dump of the simulation'
                            )
    evo_parser.add_argument('--pop-best-save-time', type=int ,
                            default=1000 ,
                            help='interval for creating dumps of the best cell'
                            )

    evo_parser.add_argument('--regscore-clonesize', type=int ,
                            default=100,
                            help='The number of within-clone comparisons to make when calculating regulator score. 0 = skip the calculation of regulator scores'
                            )

    evo_parser.add_argument('--kill-lineage', type=int,
                             default=None,
                             help="lineage to be killed at kill-time"
                             )
    evo_parser.add_argument('--kill-time', type=int,
                             default=None,
                             help="time at which lineage --kill-lineage is killed"
                             )

    evo_parser.add_argument('--pop-snapshot-time',type=int,
                            default=1000000000,
                            help='save a snapshot of the individuals in the current population')
    evo_parser.add_argument('--mem-limit', type=float,
                            default=5e10, # a maximum heap size of 40GB can be allocated for the simulation
                            help=argparse.SUPPRESS)
    evo_parser.add_argument('--no-mem-limit', dest='mem_limit',
                            action='store_const', const=None,
                            help=argparse.SUPPRESS)
    evo_parser.add_argument('--errand-boy', action='store_true', default=False,
                         help=argparse.SUPPRESS)
    evo_parser.add_argument('--no-errand-boy', dest='errand_boy', action='store_false',
                            default=True,
                         help=argparse.SUPPRESS)
    evo_parser.add_argument('--load-cycle', type=int,
                            default=1, # reload a (pickled) save file every n rounds of saving
                            help=argparse.SUPPRESS)
    evo_parser.add_argument('--shelve-fraction', type=float, default=0., help=argparse.SUPPRESS)
    evo_parser.add_argument('--shelve-time', type=int, help=argparse.SUPPRESS)
    evo_parser.add_argument('--min-lineage-marking', type=int, default=1,
                            help=('update markers for lineages when the number of lineages is'
                                  'a minimum number')
                            )

    # ENVIRONMENT INIT
    env_init.add_argument("--env-rand-seed", type=int,
                          default=951,
                          help="environment initialization and changing seed"
                          )
    env_init.add_argument('--building-block-influx', action='store_true',
                          default=False,
                          help='sets influx of building block molecules; off by default'
                          )
    env_init.add_argument('--no-building-block-influx', dest='building_block_influx', action='store_false',
                          help=argparse.SUPPRESS
                          )
    env_init.add_argument('--no-bb-class-influx', action='store_false', dest='bb_class_influx',
                          default=True,
                          help='molecules in the same class as building blocks cannot be influxed')
    env_init.add_argument('--influx-energy-precursor', action='store_true',
                         default=False,
                         help='enabling this makes sure that energy precursors flux in'
                         ' can overrule disabled influx of building-blocks'
                         )
    env_init.add_argument('--no-influx-energy-precursor', dest='influx_energy_precursor', action='store_false',
                         help=argparse.SUPPRESS )
    env_init.add_argument('--energy-influx', action='store_true' ,
                          default=False,
                          help='sets influx of energy molecules into environment; off by default'
                          )
    env_init.add_argument('--fraction-influx', type=float_or_int ,
                          default=0.5 ,
                          help=('the fraction of metabolites that will flux into the environment. These will be sampled '
                                ' from the allowed molucules, depending on building-block-influx and energy-influx params'
                                ' It is also possible to give an integer value, that will be interpreted as the (maximum)'
                                ' number of metabolites that will be influxed (depending on the available metabolites in the'
                                ' metabolic universe). Note: be careful to distinguish the fraction "1." from the number 1'
                                ' (with the floating point).'
                                )
                          )
    env_init.add_argument('--prioritize-energy-rich-influx', action='store_true' ,
                          default=False ,
                          help=('Only the top most energy rich molecules will be selected')
                          )
    env_init.add_argument('--prioritize-energy-poor-influx', action='store_true' ,
                          default=False ,
                          help=('Only the least energy rich molecules will be selected')
                          )
    env_init.add_argument('--high-energy-bbs', action='store_true',
                          default=False,
                          help=('Give priority to high energy molecules as building blocks.'))
    env_init.add_argument('--degradation-variance-shape', type=int,
                          help=('shape parameter for gamma distributed rate of degradation rate of small molecules'
                                ' ; higher values lead to tighter ranges for change. '
                                ' The distribution is centered around the value set for the degr-const parameter.'
                                )

                         )

    env_init.add_argument('--nr-cat-reactions', type=int,
                          default=10,
                          help=('the number of catabolic reactions in the reaction universe'
                                )
                          )
    env_init.add_argument('--nr-ana-reactions', type=int,
                          default=10,
                          help=('the number of catabolic reactions in the reaction universe'
                                )
                          )
    env_init.add_argument('--max-cat-path-conv', type=int,
                          default=8,
                          help=('maximum number of catabolic reactions in which any given metabolite is produced.')
                          )
    env_init.add_argument('--max-ana-path-conv', type=int,
                          default=8,
                          help=('maximum number of anabolic reactions in which any given metabolite is produced.')
                          )
    env_init.add_argument('--max-ana-free-energy', type=int,
                          default=8,
                          help=('maximum free energy loss in anabolic reaction'))
    env_init.add_argument('--max-nr-cat-products', type=int,
                          default=8,
                          help=('maximum number of products, excluding energy molecules, in a catabolic reaction.'
                                )
                          )
    env_init.add_argument('--min-cat-energy', type=value_or_range,
                          default=1,
                          help= ('the minimum energy yield from a catabolic reaction. Can be a value or a range. '
                                 ' When it is a range, the minimum will be randomly drawn from the range '
                                 'for each new reaction that is randomly initialized in the reaction universe.')
                          )
    env_init.add_argument('--max-nr-ana-products', type=int,
                          default=2,
                          help=('maximum number of products in an anabolic reaction. '
                                )
                          )
    env_init.add_argument('--nr-ana-reactants', type=value_or_range,
                          default=(1,8),
                          help=('number of reactants in an anabolic reaction, excluding energy molecules.'
                                ' Can be a value or a range if a different, random number of reactants is'
                                ' desired.'
                                )
                          )
    env_init.add_argument('--consume-range', type=value_range ,
                          default=(1,8),
                          help='stoichiometric value range for substrates in enzymatic reactions'
                          )
    env_init.add_argument('--ene-energy-range', type=value_range ,
                          default=(1,1) ,
                          help='range for energy levels of energy levels; input low,high '
                          )
    env_init.add_argument('--fraction-mol-transports', type=float ,
                          default=0.5 ,
                          help='fraction of transport reactions of all potential reaction, realized in the simulation'
                          )
    env_init.add_argument('--fraction-realized-reactions', type=float ,
                          default=1. ,
                          help=('the fraction of all potentially realizable enzymatic reactions given the set'
                                ' of constraints that will be realized in the simulation')
                          )
    env_init.add_argument('--transport-cost-range', type=value_range ,
                          default=(1,1) ,
                          help='maximum nr energy molecules consumed for every molecular transport'
                          )
    env_init.add_argument('--max-ene-yield', type=int,
                          default=3,
                          help=('maximum yield of energy molecules from reaction')
                          )
    env_init.add_argument('--max-yield', type=int ,
                          default=3 ,
                          help='maximum stoichiometric value for products in enzymatic reactions'
                          )
    env_init.add_argument('--mol-per-ene-class', type=value_or_range ,
                          default=1 ,
                          help=''
                          )
    env_init.add_argument('--mol-per-res-class', type=value_or_range ,
                          default=(1,1) ,
                          help=''
                          )
    env_init.add_argument('--nr-building-blocks', type=int ,
                          default=2 ,
                          help='number of molecular species that will be defined as building blocks'
                          )
    env_init.add_argument('--nr-cell-building-blocks', type=int,
                          default=2,
                          help=('from the building blocks defined in the environment, how many will be'
                                ' randomly chosen for the cells growth function. If not set, then all'
                                ' environmental building blocks are needed for cell growth')
                          )
    env_init.add_argument('--energy-for-growth', action='store_true',
                          help='growth of raw production value includes consumption of energy'
                          )
    env_init.add_argument('--no-energy-for-growth', dest='energy_for_growth', action='store_false',
                          help=argparse.SUPPRESS
                          )
    env_init.add_argument('--nr-energy-classes', type=int ,
                          default=1 ,
                          help=''
                          )
    env_init.add_argument('--nr-resource-classes', type=int ,
                          default=8,
                          help=''
                          )
    env_init.add_argument('--pathway-branching', type=int ,
                          default=8,
                          help=('metabolic pathway branching factor. How often can a metabolite appear in the lhs of '
                            ' a reactions in the metabolic network ')
                          )
    env_init.add_argument('--pathway-convergence', type=int ,
                          default=1 ,
                          help=('metabolic pathway convergence factor. How often can a metabolite appear in the rhs of '
                            ' a reaction in the metabolic network ')
                          )
    env_init.add_argument('--reaction-schemes', type=to_reaction_scheme , nargs='+',
                          default=[ReactionScheme(1,1), ReactionScheme(1,2)] ,
                          help=('specifies the possible types of reactions, where n,m (n,m integers)'
                                ' are reactions from n different substrates to m products')
                          )
    env_init.add_argument('--res-energy-range', type=value_range,
                          default=(2,15) ,
                          help='range for energy levels of resources; input low,high '
                          )
    env_init.add_argument('--diff-energy-prop', action='store_true',
                          help='diffusion rate of a molecule over the membrane is inversely proportional to its energy_level')
    ## toxicity
    env_init.add_argument('--toxicity', type=float ,
                         default=0.5 ,
                         help=('internal concentration of any molecule above which it becomes toxic to the cell.'
                               'Toxicity can build up during the lifetime of a cell increases its chance of dying.')
                         )
    env_init.add_argument('--inherit-toxicity', action='store_true' ,
                         default=False ,
                         help=('Divide toxicity between parent and offspring.')
                         )
    env_init.add_argument('--toxicity-variance-shape', type=float ,
                         default=15 ,
                         help=('shape parameter of gamma distributed toxicity levels used at random initialization of'
                               ' different molecule species (see influx-variance-shape for more info)')
                         )
    env_init.add_argument('--no-toxicity-variance-shape', dest='toxicity_variance_shape',
                          action='store_const', const=None,
                         help=argparse.SUPPRESS)
    env_init.add_argument('--toxicity-scaling', type=float,
                         default=25.,
                         help='scaling parameter for toxic effect Hill function'
                         )
    env_init.add_argument('--product-toxicity', type=float ,
                         default=5. ,
                         help='level at which accumultated "raw_production" becomes toxic'
                         )
    # POPULATION INIT

    pop_init.add_argument('--chromosome-compositions', nargs='+', type=to_gene_type_numbers,
                          default=[GeneTypeNumbers(tf=5,enz=3,pump=2)] ,
                          help=('list of chromosome compositions for construction of cell genomes.'
                                ' gene type numbers for each chromosome can be specified as comma'
                                ' separated triples, for each chromosome as:'
                                ' tf=x,enz=y,pump=z with x,y,z the number of those type that will'
                                ' be encoded on on the chromosome. '
                                )
                          )
    pop_init.add_argument('--cell-files-query', type=str,
                         default=None,
                         help='Query to search for cell files (e.g. entire directory)'
                         )
    pop_init.add_argument('--cells-from-files', nargs='+', type=str,
                         help='List of ".cell" files used to initialize the population'
                               'Note: cell IDs, unique_keys, as well as the IDs of genes are NOT'
                               'maintained when continueing from cell-files. Just so you know :)'
                         )
    pop_init.add_argument('--circular-chromosomes', action='store_true',
                          help=('simulates circular chromosomes. When chromosomes are circular'
                                ' stretch mutations are not bounded by an end or start of the'
                                ' chromosome. They apply equally at all positions.')
                          )
    pop_init.add_argument('--better-tf-params', action='store_true', default=False,
                          help=('generate better params for randomly generated tfs (binding Ks and apo/bound more in good ballpark)'
                                 'NOTE: Assumes as least 1 order of magnitude difference in the param space')
                          )
    pop_init.add_argument('--operator-seq-len', type=int, default=10,
                          help='length of the operator sequence.')
    pop_init.add_argument('--binding-seq-len', type=int, default=10,
                          help='length of the binding sequence of tfs.')
    pop_init.add_argument('--tf-binding-cooperativity', type=float, default=1,
                          help='binding cooperativity (hill constant) of tfs')
    pop_init.add_argument('--ligand-binding-cooperativity', type=float, default=1,
                          help='binding cooperativity (hill constant) of ligands')
    pop_init.add_argument('--prioritize-influxed-metabolism', action='store_true',
                            default=True,
                          help='prioritize metabolic reactions using influxed molecules during genome initialization.')
    pop_init.add_argument("--pop-rand-seed", type=int,
                          default=41,
                          help="population initialization seed"
                          )
    pop_init.add_argument('--single-clone-init', action='store_true',
                          default=False,
                          help='start the population from a single clone'
                          )
    # internal dynamics
    pop_init.add_argument('--building-block-stois', type=value_range,
                          default=(1,1),
                          help='stoichiometry of building blocks in the growth function'
                          )
    pop_init.add_argument('--reproduce-neutral', action='store_true',
                          help='no selection whatsoever when reproducing. Cell volumes are maintained indefinitely to avoid inf. shrinking.')
    pop_init.add_argument('--no-reproduce-neutral', dest='reproduce_neutral',action='store_false',
                          help=argparse.SUPPRESS)
    pop_init.add_argument('--reproduce-size-proportional', action='store_true',
                          help='selection is based on cell size.')
    pop_init.add_argument('--no-reproduce-size-proportional', dest='reproduce_size_proportional',action='store_false',
                          help=argparse.SUPPRESS)
    pop_init.add_argument('--cell-init-volume', type=float ,
                          default=1. ,
                          help='volume of a cell'
                          )
    pop_init.add_argument('--cell-division-volume', type=float,
                          default=2.,
                          help=('set a minimum volume that cell must reach before it can divide. Note that '
                          ' it must be lower than max-cell-volume, otherwise cells can never divide.'
                          )
                          )
    pop_init.add_argument('--max-cell-volume', type=float ,
                          default=5. ,
                          help='determines the maximum overshoot of the cell volume.'
                          )
    pop_init.add_argument('--min-cell-volume', type=float,
                          default=0.2,
                          help='the minimum volume for viability. Cells that are smaller die.')
    pop_init.add_argument('--cell-growth-rate', type=float,
                          default=0.4,
                          help='maximum rate of cell volume increase.'
                          )
    pop_init.add_argument('--cell-shrink-rate', type=float,
                          default=0.02,
                          help='rate of cell volume decrease which results in continous upkeep for cell volume'
                          )
    pop_init.add_argument('--cell-growth-cost', type=float,
                          default=0.5,
                          help=("cost of cell growth. The rate at which the `production' variable is"
                           " spent when the cell volume increases. This is in addition to the `dilution'"
                           " of the `production' (and other internal metabolite concentrations) during"
                           " cell growth." )
                          )
    pop_init.add_argument('--uptake-dna', type=float,
                          default=1.0,
                          help=("Rate of eDNA uptake. Defaults to 1.0, meaning that the rate for cells to "
                          " accept HGT from a donor is equal to the parameter given in --mutation-rates (internal_hgt)"
                          " the rate of uptake evolves with rate given in --mutation-rates (uptake_mutrate), which is"
                          "0.0 by default.")
                          )

    pop_init.add_argument('--init-pop-size', type=int,
                            default=None,
                          help="initial population size"
                          )
    pop_init.add_argument('--toxic-building-blocks', action='store_true' ,
                          help='toxic levels for building blocks'
                          )
    pop_init.add_argument('--no-toxic-building-blocks', dest='toxic_building_blocks', action='store_true' ,
                          help=argparse.SUPPRESS
                          )
    pop_init.add_argument('--init-prot-mol-conc', type=float ,
                         default=0.001 ,
                         help='concentration of internal proteins when cells are initialized'
                         )
    ######################## SHARED OPTIONS #####################

    #SIMULATE PARAMETERS
    sim_par.add_argument('--proctitle', type=str,
                         default='virtualmicrobes',
                         help="sets a different program title (i.e. appearance in top or ps commands)"
                        )
    #sim_par.add_argument('--log-file', type=str, action='append', nargs='+',
    #                     help='write the simulation output to a set of different files in addition to stdout'
    #                     )
    sim_par.add_argument('--load-params', type=str,
                         default=None,
                         help='load parameters from file (name) containing a population dump'
                         )
    # integrator params
    sim_par.add_argument('--absolute-error', type=float ,
                         default=0. ,
                         help='sets the absolute error parameter for integrator'
                         )
    #=========================================================================== OBSOLETE
    # sim_par.add_argument('--between-diffusion-reports', type=float ,
    #                      default=.25 ,
    #                      help='number of time points that should be recorded during physiology updating on the grid'
    #                      )
    #===========================================================================
    sim_par.add_argument('--report-frequency', type=int ,
                         default=1 ,
                         help='number of time points that should be recorded during physiology updating on the grid'
                         )
    sim_par.add_argument('--delta-t-between-diff', type=float ,
                         default=0.10 ,
                         help='time between every diffusion step for within local grid cell physiological reactions'
                         )
    sim_par.add_argument('--diffusion-constant', type=float ,
                         default=0.01 ,
                         help='per diffusion step rate of small molecule diffusion in the external environment'
                         )
    sim_par.add_argument('--diffusion-steps', type=int ,
                         default=1 ,
                         help=('how many diffusion steps should take place on the grid. Together with'
                               ' "delta_t_between_diff" determines the physiological time scale for'
                               ' lives of cells')
                         )
    sim_par.add_argument('--init-step-size', type=float ,
                         default=1e-5 ,
                         help='sets initial step size that should be attempted by the integrator during grid updating'
                         )
    sim_par.add_argument("-n", "--num-threads", type=int,
                         default=8,
                         help="number of threads/cores to use in the integration step"
                         )
    sim_par.add_argument('--relative-error', type=float ,
                         default=1e-2 ,
                         help=('sets the relative error parameter for the integrator. Note that error rates < 1e-3'
                               ' are not recommended as they are likely to lead the integrator to get stuck on an integration'
                               ' step when the system equations are stiff.')
                         )
    sim_par.add_argument('--step-function', type=str , choices=['rk2', 'rk4', 'rkf45', 'rk8pd', 'rkck' ,'msadams'] ,
                         default='rk8pd' ,
                         help='sets stepper function for integration'
                         )
    # path options
    sim_par.add_argument('--base-dir', type=abs_path ,
                         default='.' ,
                         help='root of the simulation directory structure'
                         )

    sim_par.add_argument('--source-path', type=str ,
                         default=os.path.dirname(os.path.realpath(VirtualMicrobes.__file__)),
                         help='path where helper files/dirs can be found (e.g. utility_dir)'
                         )
    sim_par.add_argument('--utility-dir', type=str ,
                         default='utility_files' ,
                         help='directory with utility files needed for simulation'
                         )
    sim_par.add_argument('-e','--clean-save-path', action='store_true' ,
                         default=False,
                         help='clean the base directory of the simulation (removes population saves and param files)'
                         )
    # competition
    sim_par.add_argument('--competition', type=str, choices=['global', 'local'] ,
                         default='local' ,
                         help='sets competition between cells to be global or locally on the grid'
                         )
    # general
    sim_par.add_argument('--graphs-single-core', action='store_true',
                         default=True ,
                         help='do plotting in the main simulation thread'
                         )
    sim_par.add_argument('--graphs-multi-core', dest='graphs_single_core',action='store_false',
                         help='do plotting in (forked) multiprocess threads'
                         )
    sim_par.add_argument('--graphs-video', action='store_true',
                     default=True ,
                     help='whether to make videos of PNG output. Uses FFMPEG version 2 or higher.'
                     )
    sim_par.add_argument('--grid-graph-data-range', type=lambda s:(value_range(s,float)),
                     default=None,
                     help='sets grid-graph axes limits to 10^<value_range>'
                     )
    sim_par.add_argument('--no-graphs-video', dest='graphs_video',action='store_const', const=None,
                     help=argparse.SUPPRESS)
    sim_par.add_argument('--show', action='store_true',
                         default=False,
                         help='show matplotlib figures online'
                         )
    sim_par.add_argument('--tree-prune-depth', type=int,
                         default=1000,
                         help='time cutoff to prune back tree phylogenetic tree from the leafs.'
                         )
    sim_par.add_argument('--auto-restart', type=lambda x: key_value_opt(x, key_type=str, val_type=float), nargs='*',
                         action=OptionDict, default=None,
                         const={'evo_rand_seed':1.1},
                         help=('When a population goes extinct, restart the simulation from the last simulation save with '
                               'modified parameters. '
                               'Specify (multiple) parameters that should be modified, using a chosen (multiplicative) factor '
                               'as : "--auto-restart param1:factor1 param2:factor2"  . If no parameters are specified, by default '
                               'the evo_rand_seed will change with a factor "1.1" (will be rounded when actually seeding '
                               'RNG).'
                               )
                         )
    sim_par.add_argument('--no-auto-restart', dest='auto_restart', action='store_const', const=None,
                         help=argparse.SUPPRESS)
    #ENVIRONMENT PARAMETERS
    # grid
    env_par.add_argument('--env-from-file', type=str, default=None,
                         help='composes an environment from a file, instead of procedurally generating it')
    env_par.add_argument('--upgrade-environment', action='store_true', default=False,
                         help='use to upgrade the reaction universe with new reactions'
                         )
    env_par.add_argument('-c', '--grid-cols', type=int ,
                         default=32 ,
                         help=''
                         )
    env_par.add_argument('-r', '--grid-rows', type=int ,
                         default=32 ,
                         help=''
                         )
    env_par.add_argument('-v', '--per-grid-cell-volume', type=float,
                         default=8.,
                         help="volume in every grid cell of the environment"
                         )
    env_par.add_argument('--wrap-ew', type=str, choices=['diffusion', 'competition','hgt'], nargs='*' ,
                         default=['diffusion','competition', 'hgt'] ,
                         help=('wrap around the grids east-west direction. This can be indpendently chosen'
                               ' for cell-cell reproductive competition and diffusion of metabolites, respectively')
                         )
    env_par.add_argument('--wrap-ns', type=str, choices=['diffusion', 'competition','hgt'] , nargs='*',
                         default=['diffusion','competition', 'hgt'] ,
                         help='wrap around north-south direction'
                         )
    env_par.add_argument('--cells-grid-diffusion', type=float,
                         help=('cells diffuse on the grid to neighboring grid points (in the '
                               ' competition neighborhood) with a given probability. They may diffuse to'
                               ' grid points that are already occupied by other cells.'
                               )
                         )
    env_par.add_argument('--perfect-mix', type=int,
                         help='perfect mix the cells on the grid at a regular interval. Also perfectly mixes all metabolites.'
                         )
    env_par.add_argument('--no-perfect-mix', dest='perfect_mix', action='store_const', const=None,
                         help=argparse.SUPPRESS)
    # influx
    env_par.add_argument('--influx', type=float ,
                         default=None,
                         help='influx rate per volume unit into the environment')
    env_par.add_argument('--no-influx', dest='influx', action='store_const', const=None,
                         help=(
                               'Set no influx. Note: the two options --influx and --no-influx '
                               ' set the same options. The last parsed option will take precedence. '
                               '(More --no-OPTION-NAME options exist but are suppressed in this help. '
                               'Refer to virtualmicrobes.py to see which other options exist.) '
                               )
                         )
    env_par.add_argument('--influx-range', type=lambda x: key_value_opt(x, key_type=str, val_type=float),
                         action=RefineDefaultDict,  nargs='*',
                         default={'base':10, 'lower':-5, 'upper':-4} ,
                         help=('base, upper and lower bound on exponentially distributed influx values at resource fluctuation.'
                               ' specify as space separated key:value pairs')
                          )
    env_par.add_argument('--no-influx-range', dest='influx_range',action='store_const', const=None,
                         help=argparse.SUPPRESS)
    env_par.add_argument('--influx-variance-shape', type=float ,
                         default=None ,
                         help=('shape parameter for gamma distributed rate of influx when environment fluctuates'
                         ' of 0, influx will not change; otherwise higher values lead to tighter ranges for change'
                         ' ; the distribution will have a equal to the initial value set for the "influx" parameter')
                         )
    env_par.add_argument('--no-influx-variance-shape', dest='influx_variance_shape',action='store_const', const=None,
                         help=argparse.SUPPRESS)
    env_par.add_argument('--fluctuate-frequencies', type=tp_rate_change, nargs='+',
                         default=[(0,0.0)] ,
                         help=('frequency given as either number of generation steps or a probability'
                         ' of changing the environment. In the case of a probability, it is a per timestep'
                         ' probability for any influxed variable to change influx rate.')
                         )
    env_par.add_argument('--no-fluctuate-frequencies', dest='fluctuate_frequencies',action='store_const', const=None,
                         help=argparse.SUPPRESS
                         )
    sim_par.add_argument('--fluctuate-extremes', action='store_true',
                         default=False ,
                         help='only use max and minimum of influx range'
                         )
    sim_par.add_argument('--no-fluctuate-extremes', dest='fluctuate_extremes',action='store_const', const=None,
                         help=argparse.SUPPRESS)
    #    dynamics
    env_par.add_argument('--ene-ext-degr-const', type=float ,
                          default=1e-2 ,
                          help='degradation constant for energy molecules'
                          )
    env_par.add_argument('--bb-ext-degr-const', type=float ,
                          default=1e-3 ,
                          help='degradation constant for energy molecules'
                          )
    env_par.add_argument('--small-mol-ext-degr-const', type=float ,
                         default=1e-4,
                         help='rate of small molecule degradation within cells'
                         )
    env_par.add_argument('--init-external-conc', type=float ,
                         default=0.,
                         help=('concentration at which external molecules are initialized; molecules for which influx is off'
                               ' will not be set to this initial concentration, but instead to a near zero concentration')
                         )
    env_par.add_argument('--equilibrium-external-conc', dest='init_external_conc' ,action='store_const', const=None,
                         help=('set concentration at which external molecules are initialized to the equilibrium value'
                               ' according to influx and degradation rate.')
                         )
    env_par.add_argument('--init-external-conc-vals', type=lambda x: key_value_opt(x, key_type=str, val_type=float), nargs='*',
                         action=OptionDict, default=None,
                         help=('when resetting the environemntal grid concentrations, you can set specific values per metabolite with'
                                ' this parameter. e.g.: --init-external-conc 0.1 --init-external-conc-vals a.0:0.5 c.1:0.7 '
                                ' In this example, it resets all metabolites to 0.1 (e.g. during resource cycling), but will set '
                                'a.0 and c.1 to 0.5 and 0.7 respectively ')
                        )
    env_par.add_argument('--microfluid', type=lambda x: key_value_opt(x, key_type=str, val_type=str), nargs='*',
                         action=OptionDict, default=None,
                         help=('Apply a microfluid controlled external metabolite concentration that follow a set of'
                              'concentrations. E.g. --microfluid metabolites:a.0,c.0 cylelength:100 concs:\'0.1 0.5,0.5 0.5,0.1 0.1\''
                              'will cycle through 100 steps of a.0,c.0=0.1,0.5 --> a.0,c.0 =0.5,0.5 --> etc..'
                              'Adviced in combination with the following options: '
                              'no influx AND no fluctuations --> envfile and --no-fluctuate-frequencies'
                              '1x1 grid (single cell) --> envfile'
                              'no death --> --no-stochastic-death'
                              'if pre-evolved WT, set correct selection pressure --> --reset-historic-max 0.1'
                              '                   and --> --selection-pressure historic_fixed'
                            )
                        )
    env_par.add_argument('--chemostat', action='store_true',
                         default=False ,
                         help='allow cells on grid to grow on top of eachother, replacing the resident cell'
                        )



    env_par.add_argument('--resource-cycle', type=int,
                         help=('put fixed resource concentrations on the grid in a cyclic manner. '
                               'At the chosen cycle length, resource concentrations will be reset to the initial '
                                ' resource concentration. Typically, leave "fluctuate-frequencies" and '
                                '"influx-variance-shape" un-set (None). ' )
                         )
    env_par.add_argument('--no-resource-cycle', dest='resource_cycle', action='store_const', const=None,
                         help=argparse.SUPPRESS
                         )

    # toxicity

    # general

    env_par.add_argument('--frac-horizontal-bar', type=float ,
                         default=0. ,
                         help='fraction of rows that contains a horizontal barrier')
    env_par.add_argument('--max-frac-horizontal', type=float ,
                         default=0. ,
                         help='maximum fraction of field width that a horizontal barrier extends')
    env_par.add_argument('--frac-vertical-bar', type=float ,
                         default=0. ,
                         help='fraction of columns that contains a vertical barrier')
    env_par.add_argument('--max-frac-vertical', type=float ,
                         default=0. ,
                         help='maximum fraction of field heigth that a vertical barrier extends')
    env_par.add_argument('--barrier-neighborhoods', type=str ,nargs='*', choices=['diffusion', 'competition'],
                         default=['diffusion', 'competition'],
                         help='neighborhoods to apply grid barriers')
    env_par.add_argument('--influx-rows', type=int, nargs='+',
                         help='restrict influx to given rows on the grid'
                         )
    env_par.add_argument('--influx-cols', type=int, nargs='+',
                         help='restrict influx to given columns on the grid'
                         )
    env_par.add_argument('--grid-sub-div', type=to_grid_sub_div,
                         default=GridSubDiv(row=1,col=1),
                         help=('subdivide the grid into separate sub-environments. Specify the number of subdivisions'
                               ' in the total row height and column width as row=2,col=3 .'
                               )
                         )
    env_mut_ex_group = env_par.add_mutually_exclusive_group()
    env_mut_ex_group.add_argument('--sub-env-part-influx', type=float,
                         default=None,
                         help=('Only a fraction of each influxed molecule appears in each of the sub-environments.'
                               ' The set of influxed molecules per sub-environment is determined and fixed at the '
                               ' initialization of the environment.'
                               )
                         )
    env_mut_ex_group.add_argument('--sub-env-influx-combinations', type=str, choices=['richest_first', 'sparsest_first'],
                         default=None,
                         help=('Systematic combinations of influxed molecule appear in a sequence of sub-environments.'
                               ' The set of influxed molecules per sub-environment is determined and fixed at the '
                               ' initialization of the environment.'
                               )
                         )


    #POPULATION PARAMETERS
    # mutation
    pop_par.add_argument("--evo-rand-seed", type=int,
                         default=11,
                         help="evolutionary seed"
                         )
    pop_par.add_argument('--mutation-param-space', type=lambda x: key_value_opt(x, key_type=str, val_type=float),
                         action=RefineDefaultDict, nargs='+',
                         default={'base':2,
                                  'lower':-0.5,
                                  'upper':0.5,
                                  'min':0.05,
                                  'max':10.,
                                  'uniform':True,
                                  'randomize':0.1})
    pop_par.add_argument('--mutation-rates', type=lambda x: key_value_opt(x, key_type=str, val_type=float),
                         action=RefineDefaultDict, nargs='+',
                         default={'chrom_dup'             : 0.00,
                                  'chrom_del'             : 0.00,
                                  'chrom_fiss'            : 0.00,
                                  'chrom_fuse'            : 0.00,
                                  'point_mutation'        : 0.01,
                                  'tandem_dup'            : 0.1,
                                  'stretch_del'           : 0.1,
                                  'stretch_invert'        : 0.1,
                                  'stretch_translocate'   : 0.1,
                                  'stretch_exp_lambda'    : 0.3,
                                  'external_hgt'          : 0.00001,
                                  'internal_hgt'          : 0.00005,
                                  'regulatory_mutation'   : 0.01,
                                  'reg_stretch_exp_lambda': 0.2,
                                  'uptake_mutrate'        : 0.0},
                         help=('mutation rates; specify as space separated key:value pairs, e.g.'
                               '--mutation-rates chrom_del=0.1 point_mutation=.2 ')
                         )
    pop_par.add_argument('--point-mutation-ratios', type=lambda x: key_value_opt(x, key_type=str, val_type=float),
                         action=RefineDefaultDict, nargs='+',
                         default={
                                  'v_max'          : 1,
                                  'ene_ks'         : 1,
                                  'subs_ks'        : 1,
                                  'exporting'      : 1,
                                  'promoter'       : 1,
                                  'operator'       : 1,
                                  'eff_bound'      : 1,
                                  'eff_apo'        : 1,
                                  'ligand_ks'      : 1,
                                  'k_bind_op'      : 1,
                                  'ligand_class'   : 1,
                                  'bind'           : 1,
                                  'sense_external' : 1
                                  },
                         help='set the ratio of point mutation types.'
                               ' choose any from:'
                               '\n\t v_max: maximum enzyme rate'
                               '\n\t ene_ks: binding affinity for energy molecules'
                               '\n\t subs_ks: binding affinity for substrate molecules'
                               '\n\t exporting: direction of transport'
                               '\n\t promoter: promoter strength of gene'
                               '\n\t eff_apo: regulatory effect in ligand-free state'
                               '\n\t eff_bound: regulatory effect in ligand-bound state'
                               '\n\t k_bind_op: binding affinity for operator sequence'
                               '\n\t operator: operator sequence'
                               '\n\t bind: binding sequence'
                               '\nNote that rates of individual types of point mutations are'
                               ' fractions of the total point mutation rate. Therefore, decreasing (increasing)'
                               ' some point mutation types causes the rates of other point mutation'
                               ' types for a specific gene type to effectively increase (decrease).'
                         )
    pop_par.add_argument('--regulatory-mutation-ratios', type=lambda x: key_value_opt(x, key_type=str, val_type=float),
                         action=RefineDefaultDict, nargs='+',
                         default={
                                  'translocate' : 1,
                                  'random_insert': 1
                                  },
                         help='set the ratio of point mutation types.'
                               ' choose any from:'
                               '\n\t translocate: translocate and insert a regulatory sequence stretch '
                               '\n\t random_insert: insert a random sequence stretch into regulatory region '
                               '\nNote that rates of individual types of regulatory mutations are'
                               ' fractions of the total regulatory mutation rate. Therefore, decreasing (increasing)'
                               ' some regulatory mutation types causes the rates of other regulatory mutation'
                               ' types for a specific gene type to effectively increase (decrease).'
                         )
    pop_par.add_argument('--exclude-gene-from-mutation', nargs='+', type=str,
                     help='List of gene types to NOT mutate'
                     )
    pop_par.add_argument('--universal-mut-rate-scaling', type=float,
                         default=1.,
                         help=argparse.SUPPRESS)
    pop_par.add_argument('--hgt-at-div-only', action='store_true', default=False,
                         help='HGT events are not during life-time (default), but only at birth of new cells'
                         )
    pop_par.add_argument('--hgt-self', action='store_true', default=False,
                      help='HGT events are not REALLY hgt event, since you self-donate. (same as dupls, but timing may be different)'
                      )
    pop_par.add_argument('--no-hgt-at-div-only', action='store_false', dest='hgt_at_div_only',
                         help=argparse.SUPPRESS
                         )
    pop_par.add_argument('--hgt-donor-scaling', action='store_true', default=False, # Alright this option should maybe be renamed
                        help='Donors with many genes are more likely to contribute (as though theres a local gene pool)'
                        )
    pop_par.add_argument('--no-hgt-donor-scaling', action='store_false', dest='hgt_donor_scaling',
                         help=argparse.SUPPRESS
                         )
    pop_par.add_argument('--hgt-acceptor-scaling', action='store_true', default=False,
                         help='Acceptors with many genes increase chance of HGT'
                         )
    pop_par.add_argument('--no-hgt-acceptor-scaling', action='store_false', dest='hgt_acceptor_scaling',
                         help=argparse.SUPPRESS
                         )
    pop_par.add_argument('--rand-gene-params', type=lambda x: key_value_opt(x, key_type=str, val_type=float),
                         action=RefineDefaultDict,  nargs='+',
                         default={'base':10, 'lower':-0.5, 'upper':0.5} ,
                         help=('base, upper and lower bound on exponentially distributed parameter values at genome initialization.'
                               ' specify as space separated key:value pairs')
                         )
    # genome

    pop_par.add_argument('--init-small-mol-conc', type=float ,
                         default=0.,
                         help='concentration of internal small molecules when cells are initialized'
                         )
    pop_par.add_argument('--min-bind-score', type=float ,
                         default=0.85 ,
                         help=''
                         )
    pop_par.add_argument('--product-degradation-rate', type=float ,
                         default=0.07,
                         help='rate at which accumulated "raw_production" is degraded'
                         )
    pop_par.add_argument('--prot-degr-const', type=float ,
                         default=1. ,
                         help='rate of protein degradation within cells'
                         )
    pop_par.add_argument('--prot-diff-const', type=float ,
                         default=None,
                         help=argparse.SUPPRESS
                         )
    pop_par.add_argument('--small-mol-degr-const', type=float ,
                         help=('rate of small molecule degradation within cells; default value is the '
                               'external degradation rate'
                               )
                         )
    pop_par.add_argument('--small-mol-diff-const', type=float,
                         default=0.01,
                         help='diffusion constant of small molecules over cell membranes'
                         )
    pop_par.add_argument('--ene-degr-const', type=float ,
                         help=('rate of energy molecule degradation within cells; by default is set to '
                               'the external degradation rate of energy molecules'
                               )
                         )
    pop_par.add_argument('--bb-degr-const', type=float ,
                         help=('rate of building block molecule degradation within cells; by default is set to '
                               'the external degradation rate of building block molecules'
                               )
                         )
    pop_par.add_argument('--ene-diff-const', type=float,
                         default=0.01,
                         help='diffusion constant of energy molecules over cell membranes'
                         )
    pop_par.add_argument('--transporter-membrane-occupancy', type=float,
                         default=0.1,
                         help='scales the fraction of transporter concentration that can fit on a unit area'
                            ' of the cell membrane. It is used in calculating the effective rate of transport'
                            ' of a transporter enzyme as follows:'
                            ' rate_scaling = membrane_area / ( membrane_area + transporter_membrane_occupancy * total_transporter_concentration)'
                            ' meaning that if the total concentration of transporters increases, the per capita'
                            ' transport rate of transporters will tend to 0. transporter-membrane-occupancy'
                            ' determines the speed of the saturation. A value of 0. (default) means no saturation'
                            ' will occur.'
                         )
    pop_par.add_argument('--enzyme-volume-occupancy', type=float,
                         default=8.0,
                         help=('scales how the effeciency of enzymes scales with total concentration of enzymes (tfs not incl)'
                               'This crowding is scaled with a declining hill function: occupancy^2 / (occupancy^2 + total-prot-conc^2) '
                               'When the protein concentration is equal to this occupancies, the rate of metabolism is halved'
                               'In other words: low values will give a lot of crowding (e.g. 1.0/(1.0+1.0) = half of max rate)'
                               'While 9+(9+1) gives 90%% of max rates at the same protein concentration.'
                               'Note: setting the parameter to zero will exclude crowding alltogether'
                               )
                         )
    pop_par.add_argument('--v-max-growth', type=float,
                         default=1. ,
                         help=('max rate of the growth function; determines the rate at which'
                               ' building blocks are converted into "raw_production"')
                         )
    # population dynamics
    pop_par.add_argument('--base-death-rate', type=float ,
                         default=0.05,
                         help='mimimum death rate for cells per generation; may increase with accumulating toxicity'
                         )
    pop_par.add_argument('--stochastic-death', type=bool ,
                         default=True,
                         help='cells die due to stochasticit (but also when resources are limited and they cannot maintain themselves)'
                         )
    pop_par.add_argument('--no-stochastic-death', dest='stochastic_death', action='store_false',
                         help='disable stochastic death'
                         )
    pop_par.add_argument("-s", "--max-cells-per-locality",
                         type=int,
                         default=1,
                         help="maximum population size"
                         )
    pop_par.add_argument('--max-die-off-fraction', type=float ,
                         default=1.,
                         help='caps the maximum fraction of the population that dies per generation'
                         )
    pop_par.add_argument('--non', type=float ,
                         default=1.0 ,
                         help='lower bound of non-event based on accumulated "raw_production" of a cell'
                         )
    pop_par.add_argument('--competition-scaling', type=float ,
                         default=1. ,
                         help='raise the production to this power when cells compete to reproduce'
                         )
    pop_par.add_argument('--growth-rate-scaling', type=float,
                         default=1.,
                         help=('scales production dependent relative growth rate with a power "s" '
                               ' as follows:'
                               ' growth_rate ~ pow(prod, s) / ( pow(prod, s) + pow(global_scaling, s) )'
                               )
                         )
    pop_par.add_argument('--product-spending-fraction', type=float ,
                         default=0. ,
                         help=argparse.SUPPRESS#'fraction of production spent during reproduction; used when reproduction_cost is None'
                         )

    pop_par.add_argument('--reproduction-cost', type=float ,
                         default=None ,
                         help=('cost for cell to reproduce; this threshold for "raw_production"'
                               ' should be before a cell can reproduce; when set to None, no threshold is used'
                               ' and reproduction rate is proportional to production (see also "non")'
                               )
                         )
    pop_par.add_argument('--wipe-population' , type=to_population_wipe,
                         help=('wipe a fraction of the population at a certain time interval. '
                               ' format: "interval","fraction" where "interval" an int and "fraction" a float'
                               )
                        )

    pop_par.add_argument('--no-wipe-population', dest='wipe_population', action='store_const', const=None,
                         help=argparse.SUPPRESS)
    pop_par.add_argument('--min-wipe-survivors', type=int,
                         default=None,
                        help=('when wiping, number of cells that are at least surviving')
                         )
    pop_par.add_argument('--wipe-poisson', action='store_true', default=False,
			             help=('wiping is a poisson process, where lambda = 1/wiping-interval')
			             )
    pop_par.add_argument('--no-wipe-poisson', action='store_false', dest='wipe_poisson',
                         help=argparse.SUPPRESS
                         )
    pop_par.add_argument('--life-time-prod', action='store_true', default=False,
                         help='for raw production values of cell, take its life time average' )
    pop_par.add_argument('--no-life-time-prod', action='store_false', dest='life_time_prod',
                         help=argparse.SUPPRESS)
    pop_par.add_argument('--selection-pressure', type=str, choices=['historic_scaled', 'constant', 'current_scaled', 'historic_window_scaled',
                                                                    'historic_fixed'],
                         default='historic_window_scaled',
                         help=('scaling of reproductive competition: '
                               '\n"constant": "non" param is interpreted as a constant value, scaling the competition to reproduce'
                               '\n"current_scaled": "non" scales current median population production used in the competition function'
                               '\n"historic_scaled": a historic production maximum of the population is recorded;'
                               ' "non" now is the weight of this historic maximum in the competition function'
                               '\n"historic_window_scaled": same as historic scaled, but the historic production maximum'
                               ' is recorded over a time window (see historic-production-window)'
                               '\n"historic_fixed": can be used when reloading a population to retain the last value of the'
                               ' historic production maximum. The historic value will no longer be updated.'
                         )
                         )
    pop_par.add_argument('--historic-production-weight', type=float,
                         default=1.,
                         help=('when scaling selection, this is the weight of the historic maximum when'
                               ' determining the new scaling factor. The higher this weight, the slower'
                               ' the historic-production-maximum will increase when there is a current'
                               ' higher production medium in the population. '
                               ' It is only functional when'
                               ' selection-pressure is set to "historic_scaled"')
                         )
    pop_par.add_argument('--historic-production-window', type=int,
                         default=1000,
                         help=('when scaling selection, the this is the sliding window length for calculating'
                               ' the historic population production. Only functional in combination with'
                               ' selection-pressure is set to "historic_window_scaled"')
                         )
    pop_par.add_argument('--reset-historic-max', type=float,
                     default=0.0,
                     help=('resets the historic production max to a given value, as if '
                           'it never happened :)')
                     )
    pop_par.add_argument('--max-historic-max', type=float,
                     default=None,
                     help=('stop the historic production max at a given value')
                     )
    pop_par.add_argument('--start-scaling-selection-pressure', type=int,
                     default=0,
                     help=('start the historic production tracking (for cranking up selection) at a given time')
                     )
    pop_par.add_argument('--scale-prod-hist-to-pop', action='store_true', default=True,
                         help=('scale the average population production that is stored in the production '
                               ' history with the population density. In effect, when the population densitie is low, '
                               ' a high median production value in the population will be scaled down.'
                               )
                         )
    pop_par.add_argument('--no-scale-prod-hist-to-pop', dest='scale_prod_hist_to_pop', action='store_false',
                         help=argparse.SUPPRESS
                         )
    pop_par.add_argument('--divide-cell-content', type=bool ,
                         default=False ,
                         help='How to divide concentrations during reproduction'
                         )
    pop_par.add_argument('--no-death-frac', type=float ,
                         default=None,
                         help='Fraction of max_pop_size where stochastic death is disabled, avoiding extinction'
                         'Best combined with constant scaling of NON (see above option --selection-pressure)'
                         )
    pop_par.add_argument('--deathrate-density-scaling', type=float ,
                         default=None,
                         help='Power with which to increase death rate on top of normal death rate (None = disabled)'
                         )
    pop_par.add_argument('--spill-conc-factor', type=float ,
                         default=1. ,
                         help='the fraction internal metabolites released to the environment upon cell death'
                         )
    pop_par.add_argument('--spill-product-as-bb', action='store_true',
                        default=True,
                        help='Spill product as bbs, proportional to the bb -> product stochiometry'
                        )
    pop_par.add_argument('--no-spill-product-as-bb', dest='spill_product_as_bb', action='store_false',
                            help=argparse.SUPPRESS)
    pop_par.add_argument('--transcription-cost', type=float,
                         default=0.005,
                         help='cost in production of transcibing and translating a gene'
                         )
    pop_par.add_argument('--energy-transcription-cost', type=float,
                         default=0.0,
                         help='cost in energy molecules of transcibing and translating a gene'
                         )
    pop_par.add_argument('--energy-transcription-scaling', type=float,
                         default=0.001,
                         help='scaling factor for energy'
                         ' dependent transcription (energy concentration of half'
                         ' maximal transcriptoin rate'
                         )
    pop_init.add_argument('--homeostatic-bb-scaling', type=float,
                          default = 0,
                          help=('scaling of penalty on production rate for the absolute difference in internal building block concentration.'
                                ' When the penalty is 0 (default) no penalty is applied on production. When non zero production rate is adjusted '
                                'according to  rate = rate / (1 + h-bb-scaling * sum_i( abs( bb_conc_i - bb_conc_avrg)).'
                                )
                            )
    #===========================================================================
    # sim_par.add_argument('--', type='' ,
    #                      default='' ,
    #                      help='')
    # sim_par.add_argument('--', type='' ,
    #                      default='' ,
    #                      help='')
    # sim_par.add_argument('--', type='' ,
    #                      default='' ,
    #                      help='')
    #===========================================================================
    #=======================================================================
    # pop_par.add_argument('--', type='' ,
    #                      default='' ,
    #                      help='')
    #=======================================================================
    #===========================================================================
    # env_par.add_argument('--', type='' ,
    #                      default='' ,
    #                      help='')
    #===========================================================================


    #simulation options

    args = parser.parse_args()
    #modify special args
    if not args.run_type=='evo' or args.load_file is not None:
        # Suppress default arguments, because options have already been set when
        # this simulation was created. New options supplied on the command line
        # will still be handled. Then parse again and give non-defaulted args to
        # simulation initialization.
        suppress_defaults(parser, exclude=['clean_save_path'])
        suppress_defaults(evo_parser)
        args = parser.parse_args()
        if not hasattr(args, 'show') :
            setattr(args, 'show', False)
    elif args.load_params is not None:
        loaded_params = pickle.load(args.load_params)
        del loaded_params['base_dir']
        del loaded_params['name']
        args = parser.parse_args(namespace=Namespace(**loaded_params))

    if args.run_type=='evo' and args.load_file is None:
        check_growth_params(args)
        if  not args.name:
            parser.error('A simulation name should be specified (--name my_sim_name ).')

    if args.clean_save_path and args.load_file and not (args.name or args.base_dir):
        parser.error('Not allowed to clean the orignal run directory when reloading. Set a new save path first'
                     ' by specifying "--name" and/or "--base-dir" option(s).')

    if getattr(args,'resource_cycle', None) and getattr(args,'init_external_conc','dummy') is None:
        parser.error('When choosing resource cycle, init-external-conc should also be set ('
                     'this will be the resource concentration at the start of the new cycle).')
    parse_special_params(args)
    args.start(args)

    return 0

if __name__ == "__main__":
    if DEBUG:
        sys.argv.append("-h")
        sys.argv.append("-v")
        sys.argv.append("-r")
    if TESTRUN:
        import doctest
        doctest.testmod()
    if PROFILE:
        import cProfile
        import pstats
        profile_filename = 'simulation.start_sim_profile.txt'
        cProfile.run('main()', profile_filename)
        statsfile = open("profile_stats.txt", "wb")
        p = pstats.Stats(profile_filename, stream=statsfile)
        stats = p.strip_dirs().sort_stats('cumulative')
        stats.print_stats()
        statsfile.close()
        sys.exit(0)
    if '--optimize' in sys.argv:
        sys.argv.remove('--optimize')
        os.execl(sys.executable, sys.executable, '-O', *sys.argv)
    else:
        sys.exit(main())
