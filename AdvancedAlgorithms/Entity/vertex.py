

class Vertex:

    def __init__(self, id):
        self.__id = id
        self.__edges = list()

    def add_edge(self, edge):
        self.__edges.append(edge)
    
    @property
    def ID(self):
        return self.__id

    @property
    def edges(self):
        return self.__edges
    
    