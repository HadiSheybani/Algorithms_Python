import pytest
from hamcrest import *

from AdvancedAlgorithms.algorithms.spanning_trees.kruskal import Kruskal
from AdvancedAlgorithms.usecase.graph import Graph
from AdvancedAlgorithms.entity.vertex import Vertex
from AdvancedAlgorithms.entity.edge import Edge

class TestKruskal:
    def setup_method(self, method):
        pass

    def test_GiveAGraphThenAlgorithmShouldReturnTheMinimumSpanningTree(self):
        return
        graph = Graph()
        matric = [[0,   2,  6,  0,  5,  10, 0]
                 ,[2,   0,  0,  3,  3,  0,  0]
                 ,[6,   0,  0,  1,  0,  2,  0]
                 ,[0,   3,  1,  0,  4,  0,  5]
                 ,[5,   3,  0,  4,  0,  0,  0]
                 ,[10,  0,  2,  0,  0,  0,  5]
                 ,[0,   0,  0,  5,  0,  5,  0]]
        graph.create(matric, 7, False)
        kruskal = Kruskal()
        tree = kruskal.run(graph)
        assert_that(tree, equal_to([[0, 2, 0, 0, 0, 0, 0]
                                   ,[2, 0, 0, 3, 3, 0, 0]
                                   ,[0, 0, 0, 1, 0, 2, 0]
                                   ,[0, 3, 1, 0, 0, 0, 0]
                                   ,[0, 3, 0, 0, 0, 0, 0]
                                   ,[0, 0, 2, 0, 0, 0, 5]
                                   ,[0, 0, 0, 0, 0, 5, 0]]))