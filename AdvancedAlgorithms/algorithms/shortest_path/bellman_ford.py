from AdvancedAlgorithms.entity.vertex import Vertex
from AdvancedAlgorithms.entity.edge import Edge
from AdvancedAlgorithms.usecase.graph import Graph
import math


class Bellman_Ford:
    def __init__(self):
        self.__distance = dict()
        self.__pre_node = dict()
        self.__queue = list()
    
    def run(self, graph, source, destination):
        vertices = graph.vertices
        edges = graph.edges
        self.__initial_algorithms(vertices, source)
        for i in range(len(vertices) - 1):
            for edge in edges:
                temp_dis = self.__distance[edge.source.ID] + edge.weight
                if temp_dis < self.__distance[edge.destination.ID]:
                    self.__distance[edge.destination.ID] = temp_dis
                    self.__pre_node[edge.destination.ID] = edge.source
        
        for edge in edges:
            if self.__distance[edge.source.ID] + edge.weight < self.__distance[edge.destination.ID]:
                raise ValueError("Negative Cycle Exists!")
        
        output = dict()
        output['distance'] = self.__distance[destination.ID]
        output['vertices'] = self.__find_shortest_path(destination)
        return output
        

    def __initial_algorithms(self, vertices, src):
        self.__distance.clear()
        self.__pre_node.clear()
        for vertex in vertices:
            self.__distance[vertex.ID] = math.inf
            self.__pre_node[vertex.ID] = None
        self.__distance[src.ID] = 0

    def __find_shortest_path(self, destination):
        shortest_path = list()
        dis = self.__distance[destination.ID]
        vertex = destination
        while True:
            shortest_path.append(vertex)
            vertex = self.__pre_node[vertex.ID]
            if self.__distance[vertex.ID] == 0:
                shortest_path.append(vertex)
                break
        shortest_path.reverse()
        return shortest_path