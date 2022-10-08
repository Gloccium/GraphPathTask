import unittest
from algorithm import Algorithm
from random import getrandbits, randint
import tracemalloc


class TestMemory(unittest.TestCase):
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

    def test_memory_depth_first_search(self):
        tracemalloc.start()
        self.graph.depth_first_search(0)
        memory_used = tracemalloc.get_traced_memory()[1]
        tracemalloc.stop()
        print(f'Memory used for depth first search is'
              f' {memory_used // 1024} kilobytes')

    def test_memory_breadth_first_search(self):
        tracemalloc.start()
        self.graph.breadth_first_search(0)
        memory_used = tracemalloc.get_traced_memory()[1]
        tracemalloc.stop()
        print(f'Memory used for breadth first search is'
              f' {memory_used // 1024} kilobytes')

    def test_memory_dijkstra(self):
        tracemalloc.start()
        self.graph.dijkstra(0)
        memory_used = tracemalloc.get_traced_memory()[1]
        tracemalloc.stop()
        print(f'Memory used for Dijkstra is'
              f' {memory_used // 1024} kilobytes')

    def test_memory_bellman_ford(self):
        tracemalloc.start()
        self.graph.bellman_ford(0)
        memory_used = tracemalloc.get_traced_memory()[1]
        tracemalloc.stop()
        print(f'Memory used for Bellman-Ford is {memory_used // 1024}'
              f' kilobytes')

    def test_memory_floyd_warshall(self):
        tracemalloc.start()
        self.graph.floyd_warshall()
        memory_used = tracemalloc.get_traced_memory()[1]
        tracemalloc.stop()
        print(f'Memory used for Floyd-Warshall is'
              f' {memory_used // 1024} kilobytes')
