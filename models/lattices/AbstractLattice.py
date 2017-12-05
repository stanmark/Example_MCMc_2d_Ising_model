from abc import ABCMeta, abstractmethod

class AbstractLattice(object):
    """
    General functionality of 2d (m x n) Lattice models
    """
    __metaclass__ = ABCMeta

    @abstractmethod
    def initializeLattice(self):
        pass


    def __init__(self, m: int, n: int)-> None:
        self.x_size=m
        self.y_size=n
        self.node_number=m*n
        self.lattice=None
        self.initializeLattice()
        return None


    def getXsize(self)-> int:
        return self.x_size


    def getYsize(self)-> int:
        return self.y_size


    def getNodeNumber(self)-> int:
        return self.node_number


    def getLattice(self):
        return self.lattice


    def __repr__(self):
        return f"""
            I represent {self.getXsize()}x{self.getYsize()} lattice
            (in total {self.getNodeNumber()} nodes)
            with values:
            {self.getLattice()}
        """
