from AdvancedAlgorithms.entity.vertex import Vertex
from AdvancedAlgorithms.entity.edge import Edge
from AdvancedAlgorithms.usecase.graph import Graph


class Kruskal:

    def run(self, graph):
        edges = graph.edges
        vertices = graph.vertices
        edges = self.__sort_edges(edges)
        tree_edges = list()
        tree_vertices = list()
        for edge in edges:
            if len(vertices) == 0:
                break;
            tree_edges.append(edge)
            try:
                tree_vertices.index(edge.source)
            except ValueError:
                tree_vertices.append(edge.source)
                vertices.remove(edge.source)
            try:
                tree_vertices.index(edge.destination)
            except ValueError:
                tree_vertices.append(edge.destination)
                vertices.remove(edge.source)
        tree_graph = Graph()
        tree_graph.vertices = tree_vertices.copy()
        tree_graph.edges = tree_edges.copy()
        return tree_graph
        
    
    def __sort_edges(self, edges):
        sort_list = list()
        for edge in edges:
            index = 0
            for e in sort_list:
                if (edge.weight < e.weight):
                    index = index + 1
            sort_list.insert(index, sort_list)
        return sort_list
