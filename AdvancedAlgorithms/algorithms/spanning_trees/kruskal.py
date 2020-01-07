from AdvancedAlgorithms.entity.vertex import Vertex
from AdvancedAlgorithms.entity.edge import Edge
from AdvancedAlgorithms.usecase.graph import Graph


class Kruskal:
    
    def __init__(self):
        self.__joint_lists = list()

    def run(self, graph):
        edges = graph.edges
        vertices = graph.vertices
        edges = self.__sort_edges(edges)
        self.__intial_joint_lists(vertices)
        tree_edges = list()
        tree_vertices = list()
        for edge in edges:
            if (len(self.__joint_lists) == 1):
                break
            if self.__joint(edge.source, edge.destination):
                tree_edges.append(edge)
        tree_graph = Graph()
        tree_graph.vertices = vertices.copy()
        tree_graph.edges = tree_edges.copy()
        return tree_graph
        
    
    def __sort_edges(self, edges):
        sort_list = list()
        for edge in edges:
            index = 0
            for e in sort_list:
                if (edge.weight > e.weight):
                    index = index + 1
            sort_list.insert(index, edge)
        return sort_list

    def __intial_joint_lists(self, vertices):
        self.__joint_lists.clear()
        for vertex in vertices:
            joint_list = [vertex.ID]
            self.__joint_lists.append(joint_list)

    def __joint(self, vertex1, vertex2):
        index1 = 0
        index2 = 0
        counter = 0
        for l in self.__joint_lists:
            try:
                l.index(vertex1.ID)
                index1 = counter
            except ValueError:
                pass
            try:
                l.index(vertex2.ID)
                index2 = counter
            except ValueError:
                pass
            counter = counter + 1
        if index1 == index2:
            return False
        self.__joint_lists[index1].extend(self.__joint_lists[index2])
        self.__joint_lists.remove(self.__joint_lists[index2])
        return True

