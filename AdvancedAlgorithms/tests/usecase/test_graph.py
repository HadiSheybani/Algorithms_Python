import pytest
from hamcrest import *

from AdvancedAlgorithms.usecase.graph import Graph

class TestGraph:
    def setup_method(self, method):
        self.__graph = Graph()
        self.__matrix = [[0, 1, 1, 1]
                        ,[1, 0, 0, 1]
                        ,[1, 0, 0, 1]
                        ,[1, 1, 1, 0]]

    def test_GivenAnUndirectedGraphMatrixThenCheckVertices(self):
        vertices = self.__graph.create(self.__matrix, 4, False)
        assert_that(len(vertices[0].edges), equal_to(3))
        assert_that(len(vertices[1].edges), equal_to(2))
        assert_that(len(vertices[2].edges), equal_to(2))
        assert_that(len(vertices[3].edges), equal_to(3))
    
    def test_GivenADirectedGraphMatrixThenCheckVertices(self):
        self.__graph.create(self.__matrix, 4, True)
        edges = self.__graph.edges
        counter = 0
        for row in range(4):
            for col in range(4):
                if self.__matrix[row][col] != 0:
                    assert_that(edges[counter].source.ID, equal_to(row))
                    assert_that(edges[counter].destination.ID, equal_to(col))
                    assert_that(edges[counter].weight, equal_to(self.__matrix[row][col]))
                    counter = counter + 1
    
    def test_GiveAGraphWhenCallGetMatrixThenItShouldReturnGraphMatrix(self):
        self.__graph.create(self.__matrix, 4, False)
        assert_that(self.__graph.get_matrix(), equal_to(self.__matrix))
        