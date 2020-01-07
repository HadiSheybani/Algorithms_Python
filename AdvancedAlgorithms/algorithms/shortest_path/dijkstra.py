from AdvancedAlgorithms.entity.vertex import Vertex
from AdvancedAlgorithms.entity.edge import Edge
from AdvancedAlgorithms.usecase.graph import Graph
import math

class Dijkstra:
    def __init__(self):
        self.__distance = dict()
        self.__pre_node = dict()
        self.__queue = list()
    
    def run(self, graph, source, destination):
        vertices = graph.vertices
        self.__initial_algorithms(vertices, source)
        while(len(self.__queue) != 0):
            vertex = self.__find_vertex(self.__queue)
            self.__queue.remove(vertex)
            for edge in vertex.edges:
                temp_dis = self.__distance[vertex.ID] + edge.weight
                if temp_dis < self.__distance[edge.destination.ID]:
                    self.__distance[edge.destination.ID] = temp_dis
                    self.__pre_node[edge.destination.ID] = vertex
        output = dict()
        output['distance'] = self.__distance[destination.ID]
        output['vertices'] = self.__find_shortest_path(destination)
        return output

    def __initial_algorithms(self, vertices, src):
        self.__distance.clear()
        self.__pre_node.clear()
        self.__queue.clear()
        for vertex in vertices:
            self.__distance[vertex.ID] = math.inf
            self.__pre_node[vertex.ID] = None
            self.__queue.append(vertex)
        
        self.__distance[src.ID] = 0
    
    def __find_vertex(self, vertices):
        min_dis = math.inf
        min_vertex = None
        for vertex in vertices:
            if self.__distance[vertex.ID] < min_dis:
                min_dis = self.__distance[vertex.ID]
                min_vertex = vertex
        return min_vertex

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
