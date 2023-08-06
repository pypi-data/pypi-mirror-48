from abc import abstractmethod
from collections import OrderedDict
from copy import copy

from VirtualMicrobes.event.Molecule import MoleculeClass, Molecule
import VirtualMicrobes.simulation.class_settings as cs
from VirtualMicrobes.virtual_cell.GenomicElement import GenomicElement
from VirtualMicrobes.virtual_cell.PhyloUnit import AddInheritanceType
from VirtualMicrobes.virtual_cell.Sequence import Operator, BindingSequence
import matplotlib as mpl


def randomized_param(rand_gene_params, rand_generator):
    return rand_gene_params.base ** rand_generator.uniform(rand_gene_params.lower, rand_gene_params.upper)

class Promoter:
        '''
        A promoter sequence object.

        A promoter is exclusively associated with a genomic element.
        It encodes a basal promoter strength that is a factor in the gene
        expresion level.
        '''
        __metaclass__ = AddInheritanceType
        __phylo_type = cs.phylo_types['Promoter']
        __slots__ = ['strength']
        uid = 0

        def __init__(self, pr_str, time_birth=0, **kwargs):
            super(Promoter, self).__init__(time_birth=time_birth, **kwargs)
            self.strength = pr_str

        def randomize(self, rand_gene_params, rand_generator):
            '''
            Randomize the promoter parameters.

            Parameters
            ----------
            rand_gene_params : dict
                parameters for the randomization function
            rand_generator : RNG
            '''
            self.strength = randomized_param(rand_gene_params, rand_generator=rand_generator)

        def mutate(self, mut_modifier, rand_gen):
            '''
            Mutates the promoter.

            Parameters
            ----------
            mut_modifier : func
                a function that changes the promoter parameters.
            rand_gen :RNG
            '''
            self.strength = mut_modifier(self.strength, rand_gen)

        def _mutation_copy(self):
            '''
            Creates a mutated copy of the promoter.

            Returns
            -------
            Returns the mutated copy.
            '''
            mutant = super(Promoter, self)._copy(new_id=True)
            mutant.strength = self.strength
            return mutant

        def _hgt_copy(self):
            '''
            Creates a copy that is horizontally transferred.

            Returns
            -------
            Returns the HGT copy.
            '''
            copied = super(Promoter, self)._copy(new_id=True)
            copied.strength = self.strength
            return copied

        def toJSON(self, attr_mapper, *args, **kwargs):
            '''
            Creates JSON representation of promoter.

            Parameters
            ----------
            attr_mapper : dict
                mapping from attributes to colors

            Returns
            -------
            A JSON dictionary.
            '''
            d = {'name': 'Promoter',
                 'description': 'Promoter <br>Strength: ' + str(self.strength),
                 'size':1,
                 'colour': mpl.colors.rgb2hex(mpl.colors.colorConverter.to_rgba('red',
                                                                                alpha=1.))
                 }
            return d

        def __str__(self):
            return "Prom_str:" + str(self.strength)

gene_types = ['enz', 'pump', 'tf']

class Gene (GenomicElement):
    '''
    Representation of gene in the genome.

    Gene is the base class for various types of genes in the genome. A gene has
    * a set of type specific parameters
    * a promoter that determines basal gene expression level
    * an operator that allows interaction and expression modulation by
        transcription factors

    Parameters
    ----------
    type : string
        type of gene
    pr_str : float
        promoter strength
    operator_seq_len : int
        sequence length of operator
    operator : iterable
        operator sequence as bitstring
    fixed_length : bool
        if false, operator length can change
    is_enzyme : bool
        if true, is an enzyme type
    '''

    __slots__ = ['params', 'operator', 'is_enzyme', 'promoter']
    def __init__(self, type_, pr_str=1.,
                 operator_seq_len=10, operator=None, fixed_length=None,
                 is_enzyme=False, promoter_phylo_type='base',
                 operator_phylo_type='base', **kwargs):

        super(Gene, self).__init__(**kwargs)
        self.params = OrderedDict()
        self.params["type"] = type_
        self.promoter = Promoter(pr_str, **kwargs)  # also pass on kwargs to other phylo_units
        self.operator = Operator(sequence=operator, length=operator_seq_len, **kwargs)
        self.params["fixed_length"] = fixed_length
        self.is_enzyme = is_enzyme

    @abstractmethod
    def randomize(self, rand_gene_params, rand_gen, better_tfs=False, **kwargs):
        '''
        Randomizes gene properties.

        Parameters
        ----------
        rand_gene_params : dict
            parameters of randomization function
        rand_gen : RNG
        '''
        self.operator.randomize(rand_gen)
        self.promoter.randomize(rand_gene_params, rand_gen)
        if better_tfs and self.params["type"] in ['tf']:
            self.randomize_good_params(rand_gene_params, rand_gen, **kwargs)
        else:
            self.randomize_params(rand_gene_params, rand_gen, **kwargs)

    @abstractmethod
    def randomize_params(self, rand_gene_params, rand_generator):
        pass

    def mutated(self, param, new_val, time, verbose=False):
        '''
        Mutates a parameter of the gene.

        To maintain a full ancestry, the mutation should be applied to a
        (shallow) copy of the gene and this copy reinserted in the original
        ancestral position. The shallow copy will however have a new deepcopied
        version of the parameter dictionary so that the mutation will not affect
        the ancestral gene state.

        Parameters
        ----------
        param : string
            parameter to mutate
        new_val : new parameter value

        Returns
        -------
        Returns the mutated copy of the gene.
        '''
        if verbose:
            print "mutating", param, "to:", new_val
        mutant = self._mutation_copy(time=time)  # handles setting the parent copy relationship
        if param == "bind":
            mutant.binding_sequence = new_val
        elif param == "operator":
            mutant.operator = new_val
        elif param == 'promoter':
            mutant.promoter = new_val
        elif param == 'ligand_class':
            new_ligand_class, new_ligand_ks = new_val
            mutant.params['ligand_ks'] = new_ligand_ks
            mutant.ligand_class = new_ligand_class
        else:
            mutant.params[param] = new_val
        return mutant

    def _reproduction_copy(self, time):
        '''
        Creates a copy for reproduction.

        Parameters
        ----------
        time : int
            simulation time

        Returns
        -------
        Returns the gene copy.
        '''
        copied = super(Gene, self)._reproduction_copy(time=time)
        copied.is_enzyme = self.is_enzyme
        copied.promoter = self.promoter
        # NOTE: operators and binding sequences are copied separately and linked
        # back to genes during reproduction copy of the complete genome. This is
        # because ops and bss can be shared by genes and therefore can be non-
        # redundantly copied and mapped to genes.
        copied.params = self.params
        return copied

    def _mutation_copy(self, time):
        '''
        Creates mutated copy of gene.

        Parameters
        ----------
        time : int
            simulation time

        Returns
        -------
        Returns mutated copy.
        '''
        mutant = super(Gene, self)._mutation_copy(time=time)
        mutant.is_enzyme = self.is_enzyme
        mutant.promoter = self.promoter
        mutant.operator = self.operator
        # NOTE: operators, promoters and binding sequences can be 'shared' by
        # genes after their duplication and divergence. Only when these
        # Sequences are themselves mutated, will a new 'unique' Sequence object
        # be linked to the gene.
        mutant.params = copy(self.params)
        return mutant

    def _hgt_copy(self, time):
        '''
        Creates copy of gene that is horizontally transferred.

        Parameters
        ----------
        time : int
            simulation time

        Returns
        -------
        Returns copy for HGT.
        '''
        copied = super(Gene, self)._hgt_copy(time=time)
        copied.is_enzyme = self.is_enzyme
        copied.promoter = self.promoter._hgt_copy()
        copied.operator = self.operator._hgt_copy()
        # NOTE: operators, promoters and binding sequences should not be shared
        # between the ancestral and HGT'd copy of a gene. These sequences
        # maintain references to binding/bound ops/bss which are specific for
        # the genomic context, i.e. a hgt'd gene loses the genomic context of
        # the donor cell and gains that of the acceptor.
        copied.params = copy(self.params)
        return copied

    def toJSON(self, attr_mapper, index, d=None, *args, **kwargs):
        '''
        Create JSON representation of gene.

        Parameters
        ----------
        attr_mapper : dict
            mapping from properties to colours

        Returns
        -------
        JSON dict
        '''

        _d = {'name': 'gene_' + str(index),
             'description':self['type'],
             'colour': mpl.colors.rgb2hex(attr_mapper.color_protein(self)),
             'children':[self.promoter, self.operator]}
        if d is not None:
            _d['name'] = d['name'] + "_" + str(index)
            _d['description'] = d['description']
            _d['children'] += d['children']
        return _d

    def __setitem__(self, key, value):
        self.params[key] = value

    def __getitem__(self, key):
        return self.params[key]

    def __str__(self):
        out_str = "[" + super(Gene, self).__str__() + ', ' + str(self.promoter) + ', '
        kvs = []
        kvs.append(('operator', str(self.operator)))
        if self.params["type"] == "tf":
            kvs.append(('bind_seq', str(self.binding_sequence)))
            kvs.append(('ligand_class', self.ligand_class.name))

        for k, v in sorted(self.params.items()):
            if k in ["subs_ks", "ene_ks", "ligand_ks"]:
                item_strs = []
                for mol, const in v.items():
                    item_strs.append(mol.name + ":" + str(const))
                kvs.append((str(k) , '{' + " ".join(item_strs) + "}"))
            else:
                kvs.append((str(k), str(v)))
        out_str += ', '.join([ k + ':' + v for k, v in kvs ]) + ']'
        return out_str

class Transporter (Gene):

    '''
    Transporter gene class.

    Transporters can transport metabolites across the cell membrane. The class
    defines the kinetic parameters of the transport reaction. The `exporting`
    parameter determines the direction of transport.

    Parameters
    ----------
    reaction : :class:`VirtualMicrobes.virtual_cell.event.Reaction.Reaction`
        the transport reaction of the gene
    ene_ks : float or list of floats
        energy molecule binding constant
    subtrate_ks : float or list of floats
        substrate binding constants
    v_max : float
        max reaction flux constant
    exporting : bool
        if true, set to exporting
    '''

    __slots__ = ['reaction']

    def __init__(self, reaction, ene_ks=10., substrates_ks=10.,
                 v_max=1. , exporting=False, **kwargs):
        super(Transporter, self).__init__(type_='pump', is_enzyme=True, **kwargs)

        self.reaction = reaction
        self.params['ene_ks'] = init_molecule_ks(self.reaction.energy_source_class, ene_ks)
        self.params['subs_ks'] = init_molecule_ks(self.reaction.substrate_class, substrates_ks, external=True)
        self.params["v_max"] = v_max
        self.params["exporting"] = exporting

    def randomize_params(self, rand_gene_params, rand_generator, rand_direction=False):
        '''
        Randomizes gene properties.

        Parameters
        ----------
        rand_gene_params : dict
            parameters of randomization function
        rand_generator : RNG
        rand_direction : bool
            if true, randomize the direction of transport
        '''
        super(Transporter, self).randomize_params(rand_gene_params, rand_generator)
        for k in self.params.keys():
            if k in ['subs_ks', 'ene_ks']:
                for mol in self[k].keys():
                    self[k][mol] = randomized_param(rand_gene_params, rand_generator)
            elif k in ['v_max']:
                self[k] = randomized_param(rand_gene_params, rand_generator)
            elif k in ['exporting'] and rand_direction:
                self[k] = rand_generator.choice([False, True])

    def ode_params(self):
        '''
        Returns a list of dictionaries of parameters necessary and sufficient to
        parameterize an ODE for all the sub-reactions associated with this Gene.
        '''
        return self.reaction.sub_reaction_dicts, self["subs_ks"], self["ene_ks"]

    def _reproduction_copy(self, time):
        copied = super(Transporter, self)._reproduction_copy(time=time)
        copied.reaction = self.reaction
        return copied

    def _mutation_copy(self, time):
        mutant = super(Transporter, self)._mutation_copy(time=time)
        mutant.reaction = self.reaction
        return mutant

    def _hgt_copy(self, time):
        copied = super(Transporter, self)._hgt_copy(time=time)
        copied.reaction = self.reaction
        return copied

    def simple_str(self):
        p = 'e-p' if self.params['exporting'] else 'i-p'
        return p + str(self.reaction.substrate_class)

    def toJSON(self, *args, **kwargs):
        # substrate_ks = [ {'name':str(sub),   sub, ks in self['subs_ks'].items() ]
        expoimpo = "Exporter" if self.params['exporting'] else "Importer"  # Has to be defined here, or the condition will apply to all the rest of the description aswell :(
        d = {'name': 'Pump ' + str(self.id),
             'description': str(self.reaction) +
                            '<br>' + expoimpo +
                            '<br> <b> Vmax: </b>' + str(self.params['v_max']) +
                            '<br> <b> Energy k\'s: </b>' + ', '.join([ str(mol.name) + ':' + str(k)[:6] for mol, k in self.params['ene_ks'].items() ]) +
                            '<br> <b> Sub k\'s: </b>' + ', '.join([ str(mol.name) + ':' + str(k)[:6] for mol, k in self.params['subs_ks'].items() ]),
             'colour' :  mpl.colors.rgb2hex(mpl.colors.colorConverter.to_rgb('blue')),
             'children' : [] }
        return super(Transporter, self).toJSON(d=d, *args, **kwargs)

class MetabolicGene (Gene):

    """
    :version:
    :author:
    """

    __slots__ = ['reaction']

    def __init__(self, reaction, substrates_ks=10., v_max=1., forward=True, **kwargs):
        super(MetabolicGene, self).__init__(type_='enz', is_enzyme=True, **kwargs)
        self.reaction = reaction
        self.params["v_max"] = v_max
        self.params["subs_ks"] = init_substrates_ks(reaction, substrates_ks)

    def randomize_params(self, rand_gene_params, rand_generator):
        super(MetabolicGene, self).randomize_params(rand_gene_params, rand_generator)
        for k in self.params.keys():
            if k in ['subs_ks']:
                for mol in self[k].keys():
                    self[k][mol] = randomized_param(rand_gene_params, rand_generator)
            elif k in ['v_max']:
                self[k] = randomized_param(rand_gene_params, rand_generator)

    def ode_params(self):
        '''
        Returns a list of dictionaries of parameters necessary and sufficient to
        parameterize an ODE for all the sub-reactions associated with this Gene.
        '''
        return self.reaction.sub_reaction_dicts, self['subs_ks']

    def _reproduction_copy(self, time):
        copied = super(MetabolicGene, self)._reproduction_copy(time=time)
        copied.reaction = self.reaction
        return copied

    def _mutation_copy(self, time):
        mutant = super(MetabolicGene, self)._mutation_copy(time=time)
        mutant.reaction = self.reaction
        return mutant

    def _hgt_copy(self, time):
        copied = super(MetabolicGene, self)._hgt_copy(time=time)
        copied.reaction = self.reaction
        return copied

    def simple_str(self):
        return ('+'.join([ str(r) for r in self.reaction.reactants ]) + ' >\n' +
                '+'.join([ str(p) for p in self.reaction.products ])
                )
        # return str('enz '+ ''.join( '['+str(cl)+']' for cl in self.reaction.reactants ) +
        #                              '>'+ ''.join( '['+str(cl)+']' for cl in self.reaction.products ))

    def toJSON(self, *args, **kwargs):
        # substrate_ks = [ {'name':str(sub),   sub, ks in self['subs_ks'].items() ]
        d = {'name': 'Enzyme ' + str(self.id),
             'description': '<b> Vmax: </b>' + str(self.params['v_max']) +
                            '<br> <b> Sub k\'s: </b>' + ', '.join([ str(mol.name) + ':' + str(k)[:6] for mol, k in self.params['subs_ks'].items() ]) +
                            '<br>' + str(self.reaction),
             'colour': mpl.colors.rgb2hex(mpl.colors.colorConverter.to_rgb('purple')),
             'children' : [] }
        return super(MetabolicGene, self).toJSON(d=d, *args, **kwargs)

class TranscriptionFactor (Gene):
    """
    :version:
    :author:
    """

    __slots__ = [ 'binding_sequence', 'ligand_class']

    def __init__(self, ligand_mol_class, ligand_ks=10., ligand_cooperativity=1.,
                 binding_seq_len=10, binding_seq=None, eff_apo=1., eff_bound=1., k_bind_op=1.,
                 binding_cooperativity=2, sense_external=False, **kwargs):
        super(TranscriptionFactor, self).__init__(type_='tf', **kwargs)

        self.binding_sequence = BindingSequence(sequence=binding_seq, length=binding_seq_len)
        self.init_ligand(ligand_mol_class, ligand_ks)
        self.params['ligand_coop'] = ligand_cooperativity
        self.params['eff_apo'] = eff_apo
        self.params['eff_bound'] = eff_bound
        self.params['k_bind_op'] = k_bind_op
        self.params['binding_coop'] = binding_cooperativity
        self.params['sense_external'] = sense_external

    def init_ligand(self, ligand_class, ligand_ks=10):
        '''
        Set ligand class and the kinetic (K) constants of binding affinity for
        individual molecule species.

        Parameters
        ----------
        ligand_class : :class:`VirtualMicrobes.event.Molecule.MoleculeClass`
        ligand_ks : float or list of floats
            binding affinity (K) values for individual Molecule species
        '''
        self.ligand_class = ligand_class
        self.params['ligand_ks'] = init_molecule_ks(ligand_class, ligand_ks)

    def randomize_params(self, rand_gene_params, rand_generator):
        super(TranscriptionFactor, self).randomize_params(rand_gene_params, rand_generator)
        self.params['sense_external'] = (rand_generator.uniform(0.0,1.0) < 0.5)
        for k in self.params.keys():
            if k in ['ligand_ks']:
                for ligand in self[k].keys():
                    self[k][ligand] = randomized_param(rand_gene_params, rand_generator)
            if k in ['eff_apo', 'eff_bound', 'k_bind_op']:
                self[k] = randomized_param(rand_gene_params, rand_generator)

    def randomize_good_params(self, rand_gene_params, rand_generator):
        super(TranscriptionFactor, self).randomize_params(rand_gene_params, rand_generator)
        self.promoter.strength = rand_gene_params.max - rand_gene_params.base ** rand_generator.uniform(rand_gene_params.upper, rand_gene_params.upper-1)
        self.params['sense_external'] = (rand_generator.uniform(0.0,1.0) < 0.5)
        for k in self.params.keys():
            if k in ['ligand_ks']:
                for ligand in self[k].keys():
                    self[k][ligand] = rand_gene_params.min + rand_gene_params.base ** rand_generator.uniform(rand_gene_params.lower, rand_gene_params.lower+1) # Ks need to be low to be good
            if k in ['eff_apo','k_bind_op']:
                self[k] = rand_gene_params.min + rand_gene_params.base ** rand_generator.uniform(rand_gene_params.lower, rand_gene_params.lower+1) # Bound effect needs to be high
            if k in ['eff_bound']:
                self[k] = rand_gene_params.max - rand_gene_params.base ** rand_generator.uniform(rand_gene_params.upper, rand_gene_params.upper-1) # Bound effect needs to be high

    def randomize(self, rand_gene_params, rand_gen, **kwargs):
        super(TranscriptionFactor, self).randomize(rand_gene_params, rand_gen, **kwargs)
        self.binding_sequence.randomize(rand_gen)

    def _reproduction_copy(self, time):
        copied = super(TranscriptionFactor, self)._reproduction_copy(time=time)
        copied.ligand_class = self.ligand_class
        return copied

    def _mutation_copy(self, time):
        mutant = super(TranscriptionFactor, self)._mutation_copy(time=time)
        mutant.ligand_class = self.ligand_class
        mutant.binding_sequence = self.binding_sequence
        return mutant

    def _hgt_copy(self, time):
        copied = super(TranscriptionFactor, self)._hgt_copy(time=time)
        copied.ligand_class = self.ligand_class
        copied.binding_sequence = self.binding_sequence._hgt_copy()
        return copied

    def simple_str(self):
        s = str('tf ' + str(self.ligand_class))
        if self.params['sense_external']:
            s += '-e'
        else:
            s += '-i'
        return s

    def toJSON(self, *args, **kwargs):
        # print ','.join( [ str(mol.name)+':'+str(k) for mol,k in self.params['ligand_ks'] ] )
        # substrate_ks = [ {'name':str(sub),   sub, ks in self['subs_ks'].items() ]
        sense = '-e' if self.params['sense_external'] else '-i'
        d = {'name': 'TF ' + str(self.id) + sense,
             'description': 'BS: ' + self.binding_sequence.sequence +
                            '<br><b>Ligand:</b> ' + str(self.ligand_class) +
                            '<br><b>APO: </b>' + str(self.params['eff_apo']) +
                            '<br><b>Bound: </b>' + str(self.params['eff_bound']) +
                            '<br><b> Ligand k\'s: </b>' +
                            '<br>' + ', '.join([ str(mol.name) + ':' + str(k)[:6] for mol, k in self.params['ligand_ks'].items() ]),
             'colour': mpl.colors.rgb2hex(mpl.colors.colorConverter.to_rgb('brown')),
             'children' : [self.binding_sequence]}
        return super(TranscriptionFactor, self).toJSON(d=d, *args, **kwargs)

def init_molecule_ks(mol_class, mol_ks, external=False):
    '''
    Initialize the ordered mapping from molecules to Ks.

    Each molecule in a moleculeclass has an associated K value, that is the
    binding affinity.

    Parameters
    ----------
    mol_class : :class:`VirtualMicrobes.event.Molecule.MoleculeClass`
    mol_ks : float or list
        the K values for individual molecules

    Returns
    -------
    mapping from :class:`VirtualMicrobes.event.Molecule.Molecule` to K values (float)
    '''
    mol_ks_dict = OrderedDict()
    if isinstance(mol_ks, dict):
        for mol in mol_class:
            if not isinstance(mol, Molecule):
                raise Exception('expected a {}'.format(Molecule))
            if external:
                mol = mol.paired
            mol_ks_dict[mol] = mol_ks[mol.name]
    elif isinstance(mol_ks, float):
        for mol in mol_class:
            if external:
                mol = mol.paired
            mol_ks_dict[mol] = mol_ks
    elif isinstance(mol_ks, list):
        for mol, k in zip(mol_class, mol_ks):
            if external:
                mol = mol.paired
            mol_ks_dict[mol] = k
    return mol_ks_dict

def init_substrates_ks(reaction, kss):
    '''
    Initialize the ordered mapping from substrate molecules to Ks for a
    Conversion reaction.

    Each molecule in a moleculeclass has an associated K value, that is the
    binding affinity.

    Parameters
    ----------
    reaction : :class:`VirtualMicrobes.event.Reaction.Conversion`
    mol_ks : float or list
        the K values for individual molecules

    Returns
    -------
    mapping from :class:`VirtualMicrobes.event.Molecule.Molecule` to K values (float)
    '''
    ks_reactants_dict = OrderedDict()
    if isinstance(kss, dict):
        for reactant in reaction.reactants:
            if isinstance(reactant, Molecule):  # Reactions
                    if not isinstance(reactant, Molecule):
                        raise Exception('expected a {}'.format(Molecule))
                    ks_reactants_dict[reactant] = kss[reactant.name]
            else:
                for mol_name, mol in reactant.molecules.items():
                    if not isinstance(mol, Molecule):
                        raise Exception('expected a {}'.format(Molecule))
                    ks_reactants_dict[mol] = kss[mol_name]
    elif isinstance(kss, list):
        for reactant, ks in zip(reaction.reactants, kss):
            if isinstance(reactant, MoleculeClass):
                for mol, k in zip(reactant, ks):
                    ks_reactants_dict[mol] = k
            else:
                ks_reactants_dict[reactant] = ks
    elif isinstance(kss, float):
        for reactant in reaction.reactants:
            if isinstance(reactant, MoleculeClass):
                for mol in reactant:
                    ks_reactants_dict[mol] = kss
            else:
                ks_reactants_dict[reactant] = kss
    return ks_reactants_dict

def read_gene(environment, gene, gene_index, verbose=False):
    if(gene["type"] == 'enz'):
        rea = environment.find_reaction(gene["reaction"])
        newgene = MetabolicGene(reaction=rea, pr_str=gene["Prom_str"], operator=gene["operator"], fixed_length=gene["fixed_length"],
                                promoter_phylo_type='base', v_max=gene["v_max"], substrates_ks=gene["subs_ks"],
                                operator_phylo_type='base')
    elif(gene["type"] == 'pump'):
        rea = environment.find_reaction(gene["reaction"])
        newgene = Transporter(reaction=rea, exporting=gene["exporting"] == 'True', operator=gene["operator"],
                              pr_str=gene["Prom_str"], fixed_length=gene["fixed_length"], v_max=gene["v_max"],
                              ene_ks=gene["ene_ks"], substrates_ks=gene["subs_ks"], promoter_phylo_type='base',
                              operator_phylo_type='base')
    elif(gene["type"] == 'tf'):
        ligand_class = gene['ligand_class']
        molclassdict = environment.resource_classes.copy()
        molclassdict.update(environment.energy_classes)
        newgene = TranscriptionFactor(molclassdict[ligand_class], ligand_ks=gene["ligand_ks"], ligand_cooperativity=gene["ligand_coop"],
                                      binding_seq=gene["bind_seq"], eff_apo=gene["eff_apo"], eff_bound=gene["eff_bound"],
                                      k_bind_op=gene["k_bind_op"], binding_cooperativity=gene["binding_coop"], pr_str=gene["Prom_str"],
                                      sense_external=gene["sense_external"] == 'True', operator=gene["operator"])
    return newgene


def random_gene(environment, rand_gene_params, rand_gen, params, keep_transport_direction=True):
    gene_type = rand_gen.choice(gene_types)
    gene = None
    if gene_type == 'enz':
        conversion = rand_gen.choice(environment.conversions)
        gene = MetabolicGene(reaction=conversion, operator_seq_len=params.operator_seq_len)
        gene.randomize(rand_gene_params, rand_gen)
    elif gene_type == 'pump':
        transport = rand_gen.choice(environment.transports)
        gene = Transporter(reaction=transport, operator_seq_len=params.operator_seq_len)
        rand_direction = False if keep_transport_direction else True
        gene.randomize(rand_gene_params, rand_gen, rand_direction=rand_direction)
    elif gene_type == 'tf':
        ligand_class = rand_gen.choice(environment.molecule_classes)
        gene = TranscriptionFactor(ligand_mol_class=ligand_class,
                                   ligand_cooperativity=params.ligand_binding_cooperativity,
                                   operator_seq_len=params.operator_seq_len,
                                   binding_seq_len=params.binding_seq_len,
                                   binding_cooperativity=params.tf_binding_cooperativity)
        gene.randomize(rand_gene_params, rand_gen)
    return gene

def pump_rates(pump, pump_conc, metabolite_conc_dict):
    '''Estimate of pumping rates for each substrate

    :param pump: pump gene
    :param pump_conc: internal pump concentration
    :param metabolite_conc_dict: concentrations of metabolites
    '''
    metabolite_rate_dict = dict()  # NOTE: unordered ok
    sub_reactions, subs_kss, ene_kss = pump.ode_params()
    for sub_reaction_params in sub_reactions:
        if pump.exporting:
            sub = sub_reaction_params['products']['substrate']['mol']
        else:
            sub = sub_reaction_params['reactants']['substrate']['mol']
        sub_conc = metabolite_conc_dict[sub]
        _sub_stoi = sub_reaction_params['reactants']['substrate']['stoi']
        sub_k_bind = subs_kss[sub]
        ene_mol = sub_reaction_params['reactants']['energy']['mol']
        ene_conc = metabolite_conc_dict[ene_mol]
        _ene_stoi = sub_reaction_params['reactants']['energy']['stoi']
        ene_k_bind = ene_kss[ene_mol]
        rate = pump_conc * pump['v_max'] * sub_conc * ene_conc / ((sub_conc + sub_k_bind) * (ene_conc + ene_k_bind))
        metabolite_rate_dict[sub] = -rate if pump.exporting else rate
    return metabolite_rate_dict

def convert_rates(enzyme, enzyme_conc, metabolite_conc_dict):
    '''Estimate of conversion rates per substrate

    :param enzyme: enzyme gene
    :param enzyme_conc: internal enzyme concentrations
    :param metabolite_conc_dict: concentrations of metabolites
    '''
    metabolite_rate_dict = dict()  # NOTE: unordered ok
    for sub_reaction_params in enzyme.ode_params():
        nume = enzyme['v_max'] * enzyme_conc
        denom = 1.
        for reac_dict in sub_reaction_params['reactants']:
            reac = reac_dict['mol']
            re_stoi = reac_dict['stoi']
            re_k_bind = reac_dict['k_bind']
            nume *= pow(metabolite_conc_dict[reac], re_stoi)
            denom *= pow(metabolite_conc_dict[reac] + re_k_bind, re_stoi)
        rate = nume / denom
        for reac_dict in sub_reaction_params['reactants']:
            reac = reac_dict['mol']
            re_stoi = reac_dict['stoi']
            metabolite_rate_dict[reac] = -rate * re_stoi
        for prod_dict in sub_reaction_params['products']:
            prod = prod_dict['mol']
            prod_stoi = prod_dict['stoi']
            metabolite_rate_dict[prod] = rate * prod_stoi
    return metabolite_rate_dict
