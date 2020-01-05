from AdvancedAlgorithms.usecase.graph import Graph
from AdvancedAlgorithms.entity.vertex import Vertex
from AdvancedAlgorithms.entity.edge import Edge

class DFS:

    def __init__(self):
        self.__is_visited = dict()
        self.__queue = list()
        self.__search_list = list()
    def run(self, graph):
        self.__queue.clear()
        self.__search_list.clear()
        vertices = graph.vertices
        self.__initial_visited(vertices)
        self.__queue.append(vertices[0])
        self.__is_visited[vertices[0].ID] = True
        while len(self.__queue) != 0:
            vertex = self.__queue.pop(len(self.__queue) - 1)
            self.__is_visited[vertex.ID] = True
            self.__search_list.append(vertex)
            for edge in vertex.edges:
                if not self.__is_visited[edge.destination.ID]:
                    self.__queue.append(edge.destination)
        
        return self.__search_list
    
    def __initial_visited(self, vertices):
        self.__is_visited.clear()
        for vertex in vertices:
            self.__is_visited[vertex.ID] = False