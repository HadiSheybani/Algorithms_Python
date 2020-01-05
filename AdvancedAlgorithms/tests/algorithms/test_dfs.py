import pytest
from hamcrest import *

from AdvancedAlgorithms.algorithms.dfs.dfs import DFS
from AdvancedAlgorithms.usecase.graph import Graph
from AdvancedAlgorithms.entity.vertex import Vertex
from AdvancedAlgorithms.entity.edge import Edge

class TestDFS:

    def test_GivenAGraphToAlgorithmThenCheckTheOutput(self):
        graph = Graph()
        matric = [[0, 1, 1, 0, 0, 0]
                 ,[1, 0, 0, 1, 1, 0]
                 ,[1, 0, 0, 0, 0, 1]
                 ,[0, 1, 0, 0, 0, 0]
                 ,[0, 1, 0, 0, 0, 0]
                 ,[0, 0, 1, 0, 0, 0]]
        graph.create(matric, 6, False)
        dfs = DFS()
        output_vertices = dfs.run(graph)
        vertices_id = list()
        for vertex in output_vertices:
            vertices_id.append(vertex.ID)
        assert_that(vertices_id, equal_to([0, 2, 5, 1, 4, 3]))