import pytest
from hamcrest import *

from AdvancedAlgorithms.algorithms.shortest_path.bellman_ford import Bellman_Ford
from AdvancedAlgorithms.usecase.graph import Graph
from AdvancedAlgorithms.entity.vertex import Vertex
from AdvancedAlgorithms.entity.edge import Edge


class TestDijkstra:
    def setup_method(self, method):
        pass

    def test_GivenAGraphAndSourceAndDestinationVertexThenAlgorihtmShouldReturnShortestPath(self):
        graph = Graph()
        matric = [[0,   3,  5,  0,  0,  0]
                 ,[0,   0,  8,  0,  0,  0]
                 ,[0,   0,  0,  -3, 2,  0]
                 ,[0,   0,  0,  0,  0,  4]
                 ,[0,   0,  0,  0,  0,  3]
                 ,[0,   0,  0,  0,  0,  0]]
        graph.create(matric, 6, True)
        dijkstra = Bellman_Ford()
        output = dijkstra.run(graph, graph.vertices[0], graph.vertices[5])
        path_weight = output['distance']
        vertices_id = list()
        for vertex in output['vertices']:
            vertices_id.append(vertex.ID)
        assert_that(vertices_id, equal_to([0, 2, 3, 5]))

    def test_GivenAGraphWithNegativeCycleThenAlgorithmShouldReturnNone(self):
        graph = Graph()
        matric = [[0,   3,  5,  0,  0,  0]
                 ,[0,   0,  2,  0,  0,  0]
                 ,[0,   0,  0,  -6, 2,  0]
                 ,[0,   3,  0,  0,  0,  4]
                 ,[0,   0,  0,  0,  0,  3]
                 ,[0,   0,  0,  0,  0,  0]]
        graph.create(matric, 6, True)
        dijkstra = Bellman_Ford()
        try:
            output = dijkstra.run(graph, graph.vertices[0], graph.vertices[5])
            assert False
        except ValueError as error:
            assert_that(error.args[0], equal_to("Negative Cycle Exists!"))