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
                if not is_directed:
                    if col < row:
                        continue
                if (graph_matrix[row][col] != 0):
                    edge = Edge(self.__vertices[row], self.__vertices[col], is_directed, graph_matrix[row][col])
                    self.__vertices[row].add_edge(edge)
                    if not is_directed:
                        self.__vertices[col].add_edge(Edge(self.__vertices[col], self.__vertices[row], is_directed, graph_matrix[row][col]))
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

    @vertices.setter
    def vertices(self, vertices):
        self.__vertices.clear()
        self.__vertices = vertices
    
    @edges.setter
    def edges(self, edges):
        self.__edges.clear()
        self.__edges = edges

    def get_matrix(self):
        graph_size = len(self.__vertices)
        self.__sort_vertices()
        matrix = [[0 for i in range(graph_size)] for j in range(graph_size)]
        for edge in self.__edges:
            row = self.__vertices.index(edge.source)
            col = self.__vertices.index(edge.destination)
            matrix[row][col] = edge.weight
            if not self.is_directed:
                matrix[col][row] = edge.weight
        return matrix
    
    def __sort_vertices(self):
        sort_list = list()
        for vertex in self.__vertices:
            index = 0
            for v in sort_list:
                if (vertex.ID > v.ID):
                    index = index + 1
            sort_list.insert(index, vertex)
        self.__vertices = sort_list.copy()