import pytest
from hamcrest import *

from AdvancedAlgorithms.algorithms.spanning_trees.prim_jarnik import Prim_Jarnik
from AdvancedAlgorithms.usecase.graph import Graph
from AdvancedAlgorithms.entity.vertex import Vertex
from AdvancedAlgorithms.entity.edge import Edge


class TestPrimJarnik:

    def test_GiveAGraphThenAlgorithmShouldReturnTheMinimumSpanningTree(self):
        graph = Graph()
        matric = [[0,   2,  6,  0,  5,  10, 0]
                 ,[2,   0,  0,  3,  3,  0,  0]
                 ,[6,   0,  0,  1,  0,  2,  0]
                 ,[0,   3,  1,  0,  4,  0,  5]
                 ,[5,   3,  0,  4,  0,  0,  0]
                 ,[10,  0,  2,  0,  0,  0,  3]
                 ,[0,   0,  0,  5,  0,  5,  0]]
        graph.create(matric, 7, False)
        prim_jarnik = Prim_Jarnik()
        tree = prim_jarnik.run(graph)
        assert_that(tree.get_matrix(), equal_to([[0, 2, 0, 0, 0, 0, 0]
                                                ,[2, 0, 0, 3, 3, 0, 0]
                                                ,[0, 0, 0, 1, 0, 2, 0]
                                                ,[0, 3, 1, 0, 0, 0, 0]
                                                ,[0, 3, 0, 0, 0, 0, 0]
                                                ,[0, 0, 2, 0, 0, 0, 3]
                                                ,[0, 0, 0, 0, 0, 3, 0]]))