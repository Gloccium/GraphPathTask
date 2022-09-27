from graph.vertex import Vertex
from collections import deque

class Graph:
    def __init__(self, vertices):
        self.vertices = [Vertex(i) for i in range(vertices)]

    def connect_vertices(self, first_vertex_index, second_vertex_index, weight=1):
        return Vertex.connect(self.vertices[first_vertex_index],
                              self.vertices[second_vertex_index],
                              weight, self)

    def depth_first_search(self, start_vertex_index):
        start_vertex = self.vertices[start_vertex_index]
        visited = set()
        planned = [start_vertex]
        visited.add(start_vertex)
        trace = dict()
        trace[start_vertex.vertex_number] = 0
        while len(planned) != 0:
            current = planned.pop()
            for edge in current.incident_edges():
                incident_vertex = edge.incident_vertex(current)
                if incident_vertex not in visited:
                    trace[incident_vertex.vertex_number] = \
                        trace[current.vertex_number] + edge.weight
                    planned.append(incident_vertex)
                    visited.add(incident_vertex)
        return trace

    def breadth_first_search(self, start_vertex_index):
        start_vertex = self.vertices[start_vertex_index]
        visited = set()
        planned = deque([start_vertex])
        visited.add(start_vertex)
        trace = dict()
        trace[start_vertex.vertex_number] = 0
        while len(planned) != 0:
            current = planned.popleft()
            for edge in current.incident_edges():
                incident_vertex = edge.incident_vertex(current)
                if incident_vertex not in visited:
                    trace[incident_vertex.vertex_number] = \
                        trace[current.vertex_number] + edge.weight
                    planned.append(incident_vertex)
                    visited.add(incident_vertex)
        return trace

    def dijkstra(self, start_vertex_index):
        not_visited = self.vertices.copy()
        track = dict()
        track[self.vertices[start_vertex_index]] = 0
        while True:
            to_open = None
            best_characteristic = float('inf')
            for e in not_visited:
                if e in track and track[e] < best_characteristic:
                    best_characteristic = track[e]
                    to_open = e
            if to_open is None:
                result = dict()
                for x in track:
                    result[x.vertex_number] = track[x]
                return result

            for e in [x for x in to_open.incident_edges()
                      if x.first_vertex == to_open]:
                current_characteristic = track[to_open] + e.weight
                next_vertex = e.incident_vertex(to_open)
                if (next_vertex not in track)\
                        or track[next_vertex] > current_characteristic:
                    track[next_vertex] = current_characteristic

            not_visited.remove(to_open)
