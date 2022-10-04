import unittest
from algorithm import Algorithm


class Test(unittest.TestCase):
    def test_depth_first_search(self):
        incident = [[0, 1], [0, 2], [1, 3], [2, 3], [3, 4], [4, 5]]
        graph = Algorithm(vertices=6)
        for i in incident:
            graph.connect_vertices(*i)
        self.assertDictEqual(graph.depth_first_search(0),
                             {0: 0, 1: 1, 2: 1, 3: 2, 4: 3, 5: 4})

    def test_breadth_first_search(self):
        incident = [[0, 1], [0, 2], [1, 3], [2, 3], [3, 4], [4, 5]]
        graph = Algorithm(vertices=6)
        for i in incident:
            graph.connect_vertices(*i)
        self.assertDictEqual(graph.breadth_first_search(1),
                             {0: 1, 1: 0, 2: 2, 3: 1, 4: 2, 5: 3})

    def test_dijkstra(self):
        graph = Algorithm(vertices=5)
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
        graph = Algorithm(vertices=5)
        graph.connect_vertices(1, 2, 2)
        graph.connect_vertices(1, 3, 1)
        graph.connect_vertices(3, 2, -1)
        graph.connect_vertices(2, 4, 3)
        graph.connect_vertices(3, 4, 2)
        self.assertDictEqual(graph.bellman_ford(1),
                             {0: float('inf'), 1: 0, 2: 0, 3: 1, 4: 3})

    def test_bellman_ford_negative_weight_cycle(self):
        graph = Algorithm(vertices=3)
        graph.connect_vertices(1, 2, -1)
        graph.connect_vertices(2, 1, -1)
        with self.assertRaises(ValueError):
            graph.bellman_ford(1)
            graph.bellman_ford(2)

    def test_floyd_warshall(self):
        graph = Algorithm(vertices=9)
        graph.connect_vertices(0, 1, 4)
        graph.connect_vertices(0, 6, 7)
        graph.connect_vertices(1, 6, 11)
        graph.connect_vertices(1, 7, 20)
        graph.connect_vertices(1, 2, 9)
        graph.connect_vertices(2, 3, 6)
        graph.connect_vertices(2, 4, 2)
        graph.connect_vertices(3, 4, 10)
        graph.connect_vertices(3, 5, 5)
        graph.connect_vertices(4, 5, 15)
        graph.connect_vertices(4, 7, 1)
        graph.connect_vertices(4, 8, 5)
        graph.connect_vertices(5, 8, 12)
        graph.connect_vertices(6, 7, 1)
        graph.connect_vertices(7, 8, 3)
        self.assertEqual(graph.floyd_warshall(),
                         [[0, 4, 13, 19, 15, 24, 7, 8, 11],
                          [float('inf'), 0, 9, 15, 11, 20, 11, 12, 15],
                          [float('inf'), float('inf'),
                           0, 6, 2, 11, float('inf'), 3, 6],
                          [float('inf'), float('inf'), float('inf'),
                           0, 10, 5, float('inf'), 11, 14],
                          [float('inf'), float('inf'), float('inf'),
                           float('inf'), 0, 15, float('inf'), 1, 4],
                          [float('inf'), float('inf'), float('inf'),
                           float('inf'), float('inf'), 0, float('inf'),
                           float('inf'), 12],
                          [float('inf'), float('inf'), float('inf'),
                           float('inf'), float('inf'), float('inf'), 0, 1, 4],
                          [float('inf'), float('inf'), float('inf'),
                           float('inf'), float('inf'), float('inf'),
                           float('inf'), 0, 3],
                          [float('inf'), float('inf'), float('inf'),
                           float('inf'), float('inf'), float('inf'),
                           float('inf'), float('inf'), 0]])

    def test_floyd_warshall_negative_weight_cycle(self):
        graph = Algorithm(vertices=3)
        graph.connect_vertices(0, 1, 4)
        graph.connect_vertices(1, 2, 7)
        graph.connect_vertices(2, 0, -15)
        with self.assertRaises(ValueError):
            graph.floyd_warshall()
