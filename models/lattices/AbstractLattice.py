

class AbstractLattice:
    """
    General functionality of 2d (m x n) Lattice models
    """


    def __init__(self, m: int, n: int)-> None:
        self.x_size=m
        self.y_size=n
        self.node_number=m*n
        return None


    def getXsize(self)-> int:
        return self.x_size


    def getYsize(self)-> int:
        return self.y_size


    def getNodeNumber(self)-> int:
        return self.node_number
