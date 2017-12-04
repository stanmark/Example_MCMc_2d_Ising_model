class ExternalConditions:
    """
        Class for holding external parameters
    """

    def __init__(self, T=1.0, H=0.0)-> None:
        """
        Keyword arguments:
            T - temperature of the system (default value 0.0)
            H - magnetig field (default value 0.0)
        """
        self.T=float(T)
        self.H=float(H)
        return None


    def setT(self, T: float)-> None:
        """
        T setter
        """
        self.T=float(T)



    def setH(self, H: float)-> None:
        """
        H setter
        """
        self.H=float(H)


    def getT(self)-> float:
        """
        T getter
        """
        return self.T


    def getH(self)-> float:
        """
        H getter
        """
        return self.H
