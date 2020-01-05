import pytest
from hamcrest import *

from AdvancedAlgorithms.algorithms.bfs.bfs import BFS
from AdvancedAlgorithms.usecase.graph import Graph
from AdvancedAlgorithms.entity.vertex import Vertex

class TestBFS:

    def test_GivenAGraphToAlgorithmThenCheckTheOutput(self):
        graph = Graph()
        matric = [[0, 1, 1, 0, 0, 0]
                 ,[1, 0, 0, 1, 1, 0]
                 ,[1, 0, 0, 0, 0, 1]
                 ,[0, 1, 0, 0, 0, 0]
                 ,[0, 1, 0, 0, 0, 0]
                 ,[0, 0, 1, 0, 0, 0]]
        graph.create(matric, 6, False)
        bfs = BFS()
        output_vertices = bfs.run(graph)
        vertices_id = list()
        for vertex in output_vertices:
            vertices_id.append(vertex.ID)
        assert_that(vertices_id, equal_to([0, 1, 2, 3, 4, 5]))