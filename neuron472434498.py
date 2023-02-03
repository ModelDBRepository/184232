'''
Defines a class, Neuron472434498, of neurons from Allen Brain Institute's model 472434498

A demo is available by running:

    python -i mosinit.py
'''
class Neuron472434498:
    def __init__(self, name="Neuron472434498", x=0, y=0, z=0):
        '''Instantiate Neuron472434498.
        
        Parameters:
            x, y, z -- position offset
            
        Note: if name is not specified, Neuron472434498_instance is used instead
        '''
                
        self._name = name
        # load the morphology
        from load_swc import load_swc
        load_swc('Rorb-IRES2-Cre-D_Ai14_IVSCC_-172651.01.01.01_464113513_m.swc', self,
                 use_axon=False, xshift=x, yshift=y, zshift=z)

        # custom axon (works because dropping axon during import)
        from neuron import h
        self.axon = [h.Section(cell=self, name='axon[0]'),
                     h.Section(cell=self, name='axon[1]')]
        for sec in self.axon:
            sec.L = 30
            sec.diam = 1
            sec.nseg = 1
        self.axon[0].connect(self.soma[0](0.5))
        self.axon[1].connect(self.axon[0](1))
        self.all += self.axon

        self._insert_mechanisms()
        self._discretize_model()
        self._set_mechanism_parameters()
    
    def __str__(self):
        if self._name is not None:
            return self._name
        else:
            return "Neuron472434498_instance"
                
    def _insert_mechanisms(self):
        from neuron import h
        for sec in self.all:
            sec.insert("pas")
        for mech in [u'CaDynamics', u'Ca_HVA', u'Ca_LVA', u'Ih', u'Im', u'K_P', u'K_T', u'Kv3_1', u'NaTs', u'Nap', u'SK']:
            self.soma[0].insert(mech)
    
    def _set_mechanism_parameters(self):
        from neuron import h
        for sec in self.all:
            sec.Ra = 10.0
            sec.e_pas = -86.9853973389
        for sec in self.apic:
            sec.cm = 2.16
            sec.g_pas = 1.84653032455e-06
        for sec in self.axon:
            sec.cm = 1.0
            sec.g_pas = 0.000181342816224
        for sec in self.dend:
            sec.cm = 2.16
            sec.g_pas = 0.000166472303498
        for sec in self.soma:
            sec.cm = 1.0
            sec.ena = 53.0
            sec.ek = -107.0
            sec.gbar_Im = 2.98663e-07
            sec.gbar_Ih = 0.000409273
            sec.gbar_NaTs = 0.760571
            sec.gbar_Nap = 0.000438316
            sec.gbar_K_P = 0.0162449
            sec.gbar_K_T = 0.00409989
            sec.gbar_SK = 9.9112e-05
            sec.gbar_Kv3_1 = 0.136349
            sec.gbar_Ca_HVA = 0.000319809
            sec.gbar_Ca_LVA = 0.00655533
            sec.gamma_CaDynamics = 0.00132812
            sec.decay_CaDynamics = 806.45
            sec.g_pas = 0.000129687
    
    def _discretize_model(self):
        for sec in self.all:
            sec.nseg = 1 + 2 * int(sec.L / 40)

