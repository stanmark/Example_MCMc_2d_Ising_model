import unittest
from models.lattices.BinaryPbcLattice import BinaryPbcLattice

class TestBinaryPbcLattice(unittest.TestCase):


    def test_constructor(self):
        lattice=BinaryPbcLattice(3, 5)

        self.assertEqual(lattice.getXsize(), 3)
        self.assertEqual(lattice.getYsize(), 5)

        self.assertEqual(str(lattice),
        """
            I represent 3x5 lattice
            (in total 15 nodes)
            with values:
            ABC
        """)
