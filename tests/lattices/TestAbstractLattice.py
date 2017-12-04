import unittest
from models.lattices.AbstractLattice import AbstractLattice

class TestAbstractLattice(unittest.TestCase):


    def test_constructor(self):
        lattice=AbstractLattice(3, 5)

        self.assertEqual(lattice.getXsize(), 3)
        self.assertEqual(type(lattice.getXsize()), int)
        self.assertEqual(lattice.getYsize(), 5)
        self.assertEqual(type(lattice.getYsize()), int)
        self.assertEqual(lattice.getNodeNumber(), 15)
        self.assertEqual(type(lattice.getNodeNumber()), int)
