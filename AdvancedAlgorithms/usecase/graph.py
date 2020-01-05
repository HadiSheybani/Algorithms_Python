from AdvancedAlgorithms.entity.vertex import Vertex
from AdvancedAlgorithms.entity.edge import Edge

class Graph:

    def __init__(self):
        self.__vertices = list()
        self.__edges = list()
        self.__is_directed =  False

    def create(self, graph_matrix, graph_size, is_directed):
        self.__is_directed = is_directed
        self.__vertices.clear()
        for i in range(graph_size):
            self.__vertices.append(Vertex(i))
        for row in range(graph_size):
            for col in range(graph_size):
                if (graph_matrix[row][col] != 0):
                    edge = Edge(self.__vertices[row], self.__vertices[col], is_directed, graph_matrix[row][col])
                    self.__vertices[row].add_edge(edge)
                    self.__edges.append(edge)
        return self.__vertices.copy()

    @property
    def vertices(self):
        return self.__vertices.copy()
    
    @property
    def edges(self):
        return self.__edges.copy()
    
    @property
    def is_directed(self):
        return self.__is_directed