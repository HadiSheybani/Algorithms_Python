import pytest
from hamcrest import *
from AdvancedAlgorithms.algorithms.cycle_detection.directed_cycle_detection import DirectedCycleDetection
from AdvancedAlgorithms.usecase.graph import Graph
from AdvancedAlgorithms.entity.vertex import Vertex
from AdvancedAlgorithms.entity.edge import Edge


class TestCycleDetection:
    def setup_method(self, method):
        pass

    def test_GivenAGraphWithCycleThenAlgorithmShouldReturnTrue(self):
        graph = Graph()
        matric = [[0, 1, 0, 0]
                 ,[0, 0, 1, 0]
                 ,[0, 0, 0, 1]
                 ,[0, 1, 0, 0]]
        graph.create(matric, 4, True)
        cycle_detection = DirectedCycleDetection()
        is_cycle = cycle_detection.run(graph)
        assert_that(is_cycle, equal_to(True))
    
    def test_GivenAGraphWithNoCycleThenAlgorithmShouldReturnFalse(self):
        graph = Graph()
        matric = [[0, 1, 0, 0]
                 ,[0, 0, 1, 0]
                 ,[0, 0, 0, 1]
                 ,[0, 0, 0, 0]]
        graph.create(matric, 4, True)
        cycle_detection = DirectedCycleDetection()
        is_cycle = cycle_detection.run(graph)
        assert_that(is_cycle, equal_to(False))