

class Edge:

    def __init__(self, source, destination, is_directed = False, weight = 1):
        self.__source = source
        self.__destination = destination
        self.__is_directed = is_directed
        self.__weight = weight
    
    @property
    def source(self):
        return self.__source
    
    @property
    def destination(self):
        return self.__destination

    @property
    def is_directed(self):
        return self.__is_directed
    
    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, weight):
        self.__weight = weight

    @is_directed.setter
    def is_directed(self, is_directed):
        self.__is_directed = is_directed
    
