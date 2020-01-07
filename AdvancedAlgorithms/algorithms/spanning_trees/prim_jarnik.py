from AdvancedAlgorithms.entity.vertex import Vertex
from AdvancedAlgorithms.entity.edge import Edge
from AdvancedAlgorithms.usecase.graph import Graph
import math

class Prim_Jarnik:
    def __init__(self):
        self.__is_visited = dict()
        self.__queue = list()

    def run(self, graph):
        vertices = graph.vertices
        self.__initial_algorithm(vertices)
        for edge in vertices[3].edges:
            self.__queue.append(edge)

        tree_edges = list()
        counter = 0
        while False in self.__is_visited.values():
            self.__queue = sorted(self.__queue, key=lambda edge : edge.weight)
            min_edge = self.__queue.pop(0)
            tree_edges.append(min_edge)
            self.__is_visited[min_edge.source] = True
            self.__is_visited[min_edge.destination] = True
            for edge in min_edge.destination.edges:
                if not self.__is_visited[edge.destination]:
                    self.__queue.append(edge)
            
        tree_graph = Graph()
        tree_graph.vertices = vertices.copy()
        tree_graph.edges = tree_edges.copy()
        return tree_graph

    
    def __initial_algorithm(self, vertices):
        self.__is_visited.clear()
        self.__queue.clear()
        for vertex in vertices:
            self.__is_visited[vertex] = False
        
        
