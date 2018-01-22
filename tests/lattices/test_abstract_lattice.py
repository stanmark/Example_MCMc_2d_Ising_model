from models.lattices.AbstractLattice import AbstractLattice
from numpy import array

class ExampleLattice(AbstractLattice):
    def initializeLattice(self):
        self.lattice = array([[1,2,3]])

def test_constructor():
    lattice = ExampleLattice(3, 5)

    assert lattice.getXsize() == 3
    assert type(lattice.getXsize()) == int
    assert lattice.getYsize() == 5
    assert type(lattice.getYsize()) == int
    assert lattice.getNodeNumber() == 15
    assert type(lattice.getNodeNumber()) == int
    assert lattice.getLattice() == 'ABC'

    assert str(lattice) == \
    """
        I represent 3x5 lattice
        (in total 15 nodes)
        with values:
        ABC
    """
