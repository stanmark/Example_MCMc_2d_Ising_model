from models.lattices.AbstractLattice import AbstractLattice
import numpy as np

class BinaryPbcLattice(AbstractLattice):
    """
    Desc
    """

    def initializeLattice(self):
        self.lattice = np.zeros((self.getXsize(), self.getYsize()), dtype=bool)
