import unittest
from main import Graph


class Test(unittest.TestCase):
    def test_depth_first_search(self):
        incident = [[0, 1], [0, 2], [1, 3], [2, 3], [3, 4], [4, 5]]
        graph = Graph(vertices=6)
        for i in incident:
            graph.connect_vertices(*i)
        self.assertDictEqual(graph.depth_first_search(0),
                             {0: 0, 1: 1, 2: 1, 3: 2, 4: 3, 5: 4})

    def test_breadth_first_search(self):
        incident = [[0, 1], [0, 2], [1, 3], [2, 3], [3, 4], [4, 5]]
        graph = Graph(vertices=6)
        for i in incident:
            graph.connect_vertices(*i)
        self.assertDictEqual(graph.breadth_first_search(1),
                             {0: 1, 1: 0, 2: 2, 3: 1, 4: 2, 5: 3})

    def test_dijkstra(self):
        graph = Graph(5)
        graph.connect_vertices(0, 1, 3)
        graph.connect_vertices(0, 2, 1)
        graph.connect_vertices(0, 3, 6)
        graph.connect_vertices(1, 4, 8)
        graph.connect_vertices(2, 3, 4)
        graph.connect_vertices(2, 4, 12)
        graph.connect_vertices(3, 4, 4)
        self.assertDictEqual(graph.dijkstra(0),
                             {0: 0, 1: 3, 2: 1, 3: 5, 4: 9})

    def test_bellman_ford(self):
        graph = Graph(5)
        graph.connect_vertices(1, 2, 2)
        graph.connect_vertices(1, 3, 1)
        graph.connect_vertices(3, 2, -1)
        graph.connect_vertices(2, 4, 3)
        graph.connect_vertices(3, 4, 2)
        self.assertDictEqual(graph.bellman_ford(1),
                             {0: float('inf'), 1: 0, 2: 0, 3: 1, 4: 3})

    def test_bellman_ford_error_check(self):
        graph = Graph(3)
        graph.connect_vertices(1, 2, -1)
        graph.connect_vertices(2, 1, -1)
        with self.assertRaises(ValueError):
            graph.bellman_ford(1)
            graph.bellman_ford(2)


if __name__ == '__main__':
    unittest.main()