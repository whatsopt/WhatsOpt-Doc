# -*- coding: utf-8 -*-
"""
  structure.py generated by WhatsOpt. 
"""
from structure_base import StructureBase
from ssbj_openmdao.disciplines.structure import Structure as StructureDiscipline

class Structure(StructureBase):
    """ An OpenMDAO component to encapsulate Structure discipline """

    def __init__(self, scalers):
        super(Structure, self).__init__()
        # scalers values
        self.struct = StructureDiscipline(scalers)
        
    def compute(self, inputs, outputs):
        """ Structure computation """
        self.struct.compute(inputs, outputs)

	
# To declare partial derivatives computation ...
# 
#    def setup()
#        super(Structure, self).setup()
#        declare_partials('*', '*')  
			
#    def compute_partials(self, inputs, partials):
#        """ Jacobian for Structure """
    
   		
#       	partials['Theta', 'L'] = np.zeros((1, 1))
#       	partials['Theta', 'WE'] = np.zeros((1, 1))
#       	partials['Theta', 'x_str'] = np.zeros((1, 2))
#       	partials['Theta', 'z'] = np.zeros((1, 6))
   		
#       	partials['sigma', 'L'] = np.zeros((5, 1))
#       	partials['sigma', 'WE'] = np.zeros((5, 1))
#       	partials['sigma', 'x_str'] = np.zeros((5, 2))
#       	partials['sigma', 'z'] = np.zeros((5, 6))
   		
#       	partials['WT', 'L'] = np.zeros((1, 1))
#       	partials['WT', 'WE'] = np.zeros((1, 1))
#       	partials['WT', 'x_str'] = np.zeros((1, 2))
#       	partials['WT', 'z'] = np.zeros((1, 6))
   		
#       	partials['WF', 'L'] = np.zeros((1, 1))
#       	partials['WF', 'WE'] = np.zeros((1, 1))
#       	partials['WF', 'x_str'] = np.zeros((1, 2))
#       	partials['WF', 'z'] = np.zeros((1, 6))        