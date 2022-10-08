import unittest
import time
from random import getrandbits, randint
from algorithm import Algorithm
import tracemalloc


class TestTime(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.graph = cls.create_random_graph(100)

    @staticmethod
    def create_random_graph(size):
        graph = Algorithm(vertices=size)
        for vertex_i in range(size):
            for vertex_j in range(size):
                if vertex_i != vertex_j:
                    if bool(getrandbits(1)):
                        graph.connect_vertices(vertex_i, vertex_j,
                                               randint(0, 10))
        return graph

    def test_time_depth_first_search(self):
        start_time = time.time_ns()
        self.graph.depth_first_search(0)
        end_time = time.time_ns()
        print(f'Depth first search={(end_time - start_time) / 10 ** 9}')

    def test_time_breadth_first_search(self):
        start_time = time.time_ns()
        self.graph.breadth_first_search(0)
        end_time = time.time_ns()
        print(f'Breadth first search={(end_time - start_time) / 10 ** 9}')

    def test_time_dijkstra(self):
        start_time = time.time_ns()
        self.graph.dijkstra(0)
        end_time = time.time_ns()
        print(f'Dijkstra={(end_time - start_time) / 10 ** 9}')

    def test_time_bellman_ford(self):
        start_time = time.time_ns()
        self.graph.bellman_ford(0)
        end_time = time.time_ns()
        print(f'Bellman–Ford={(end_time - start_time) / 10 ** 9}')

    def test_time_floyd_warshall(self):
        start_time = time.time_ns()
        self.graph.floyd_warshall()
        end_time = time.time_ns()
        print(f'Floyd–Warshall={(end_time - start_time) / 10 ** 9}')
