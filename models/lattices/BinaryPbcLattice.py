"""
Module implements a binary boolean lattice
"""
from models.lattices.AbstractLattice import AbstractLattice
import numpy as np

class BinaryPbcLattice(AbstractLattice):
    """
       2d lattice of size m x n with boolean values in nodes (True, False)
       Due to logic table of 
    """

    def initializeLattice(self):
        self.lattice = np.zeros((self.getXsize(), self.getYsize()), dtype=bool)

#### Create test cases of binary models 2x2 to check the logic ... :w
#logic
