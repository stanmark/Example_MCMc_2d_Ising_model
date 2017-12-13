"""
Module contains abstract class describing 2d lattice
"""
from abc import ABCMeta, abstractmethod
from numpy import array

class AbstractLattice(object):
    """
    General functionality of 2d (m x n) Lattice models
    """
    __metaclass__ = ABCMeta

    @abstractmethod
    def initializeLattice(self)-> None:
        """
            Method should implement default way for incializing lattice
            current idea should implement two initilization schemas
            by reading from a file and generating random lattice
        """
        pass


    def __init__(self, m: int, n: int, lattice=None)-> None:
        self.x_size = m
        self.y_size = n
        self.node_number = m*n
        self.lattice = lattice
        if self.lattice is None:
            self.initializeLattice()
        if lattice is not isinstance(self.lattice, array):
            raise TypeError('lattice should be numpy array')
        return None


    def getXsize(self)-> int:
        """
            Getter for X size (number of nodes)
        """
        return self.x_size


    def getYsize(self)-> int:
        """
            Getter for Y size (number of nodes)
        """
        return self.y_size


    def getNodeNumber(self)-> int:
        """
            Getter for total number of nodes
        """
        return self.node_number


    def getLattice(self):
        """
            Getter for the object representing lattice
        """
        return self.lattice


    def __repr__(self):
        return f"""
            I represent {self.getXsize()}x{self.getYsize()} lattice
            (in total {self.getNodeNumber()} nodes)
            with values:
            {self.getLattice()}
        """
