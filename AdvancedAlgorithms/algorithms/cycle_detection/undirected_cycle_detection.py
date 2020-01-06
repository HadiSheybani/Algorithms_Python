from AdvancedAlgorithms.entity.vertex import Vertex
from AdvancedAlgorithms.entity.edge import Edge
from AdvancedAlgorithms.usecase.graph import Graph


class UndirectedCycleDetection:

    def __init__(self):
        self.__is_visited = dict()
        self.__queue = list()
        self.__parent_ID = dict()
    
    def run(self, graph):
        self.__queue.clear()
        vertices = graph.vertices
        self.__initial_lists(vertices)
        self.__queue.append(vertices[0])
        self.__parent_ID[vertices[0].ID] = -1
        while len(self.__queue) != 0:
            vertex = self.__queue.pop(len(self.__queue) - 1)
            self.__is_visited[vertex.ID] = True
            for edge in vertex.edges:
                if not self.__is_visited[edge.destination.ID]:
                    self.__queue.append(edge.destination)
                    self.__parent_ID[edge.destination.ID] = vertex.ID
                elif self.__parent_ID[vertex.ID] != edge.destination.ID:
                    return True

        return False

    def __initial_lists(self, vertices):
        self.__is_visited.clear()
        self.__parent_ID.clear()
        for vertex in vertices:
            self.__is_visited[vertex.ID] = False