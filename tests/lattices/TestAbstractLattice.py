import unittest
from models.lattices.AbstractLattice import AbstractLattice

class ExampleLattice(AbstractLattice):
    def initializeLattice(self):
        self.lattice='ABC'

class TestAbstractLattice(unittest.TestCase):


    def test_constructor(self):
        lattice=ExampleLattice(3, 5)

        self.assertEqual(lattice.getXsize(), 3)
        self.assertEqual(type(lattice.getXsize()), int)
        self.assertEqual(lattice.getYsize(), 5)
        self.assertEqual(type(lattice.getYsize()), int)
        self.assertEqual(lattice.getNodeNumber(), 15)
        self.assertEqual(type(lattice.getNodeNumber()), int)
        self.assertEqual(lattice.getLattice(), 'ABC')

        self.assertEqual(str(lattice),
        """
            I represent 3x5 lattice
            (in total 15 nodes)
            with values:
            ABC
        """)
