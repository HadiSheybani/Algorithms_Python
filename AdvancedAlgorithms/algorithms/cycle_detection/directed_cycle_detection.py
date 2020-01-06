from AdvancedAlgorithms.entity.vertex import Vertex
from AdvancedAlgorithms.entity.edge import Edge
from AdvancedAlgorithms.usecase.graph import Graph


class DirectedCycleDetection:
    def __init__(self):
        self.__is_visited = dict()
        self.__queue = list()
        self.__is_repeated = dict()
    
    def run(self, graph):
        self.__queue.clear()
        vertices = graph.vertices
        self.__initial_lists(vertices)
        self.__queue.append(vertices[0])
        while len(self.__queue) != 0:
            vertex = self.__queue.pop(len(self.__queue) - 1)
            self.__is_visited[vertex.ID] = True
            self.__is_repeated[vertex.ID] = True
            for edge in vertex.edges:
                if not self.__is_visited[edge.destination.ID]:
                    self.__queue.append(edge.destination)
                elif self.__is_repeated[edge.destination.ID]:
                    return True
        return False

    def __initial_lists(self, vertices):
        self.__is_visited.clear()
        self.__is_repeated.clear()
        for vertex in vertices:
            self.__is_visited[vertex.ID] = False
            self.__is_repeated[vertex.ID] = False