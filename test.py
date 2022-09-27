import unittest
from main import Graph


class Test(unittest.TestCase):
    def test_depth_first_search(self):
        incident = [[0, 1], [0, 2], [1, 2], [1, 3], [2, 4], [3, 4]]
        graph = Graph(vertices=5)
        for i in incident:
            graph.connect_vertices(*i)
        self.assertDictEqual(graph.depth_first_search(1),
                             {1: 0, 0: 1, 2: 1, 3: 1, 4: 2})

    def test_breadth_first_search(self):
        incident = [[0, 1], [0, 2], [1, 2], [1, 3], [2, 4], [3, 4]]
        graph = Graph(vertices=5)
        for i in incident:
            graph.connect_vertices(*i)
        self.assertDictEqual(graph.breadth_first_search(1),
                             {1: 0, 0: 1, 2: 1, 3: 1, 4: 2})
