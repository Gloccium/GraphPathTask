from graph.vertex import Vertex
from collections import deque


class Graph:
    def __init__(self, vertices):
        self.vertices = [Vertex(i) for i in range(vertices)]

    def connect_vertices(self, first_vertex_index, second_vertex_index,
                         weight=1):
        return Vertex.connect(self.vertices[first_vertex_index],
                              self.vertices[second_vertex_index],
                              weight, self)

    @property
    def edges(self):
        edges = []
        for elem in ([vertex.incident_edges() for vertex in self.vertices]):
            for e in elem:
                edges.append(e)
        return set(edges)

    def depth_first_search(self, start_vertex_index):
        start_vertex = self.vertices[start_vertex_index]
        visited = set()
        planned = [start_vertex]
        visited.add(start_vertex)
        trace = dict()
        trace[start_vertex.vertex_id] = 0
        while len(planned) != 0:
            current = planned.pop()
            for edge in current.incident_edges():
                incident_vertex = edge.incident_vertex(current)
                if incident_vertex not in visited:
                    trace[incident_vertex.vertex_id] = \
                        trace[current.vertex_id] + edge.weight
                    planned.append(incident_vertex)
                    visited.add(incident_vertex)
        return trace

    def breadth_first_search(self, start_vertex_index):
        start_vertex = self.vertices[start_vertex_index]
        visited = set()
        planned = deque([start_vertex])
        visited.add(start_vertex)
        trace = dict()
        trace[start_vertex.vertex_id] = 0
        while len(planned) != 0:
            current = planned.popleft()
            for edge in current.incident_edges():
                incident_vertex = edge.incident_vertex(current)
                if incident_vertex not in visited:
                    trace[incident_vertex.vertex_id] = \
                        trace[current.vertex_id] + edge.weight
                    planned.append(incident_vertex)
                    visited.add(incident_vertex)
        return trace

    def dijkstra(self, start_vertex):
        not_visited = self.vertices.copy()
        track = dict()
        track[self.vertices[start_vertex]] = 0
        while True:
            vertex_to_open = None
            best_characteristic = float('inf')
            for vertex in not_visited:
                if vertex in track and track[vertex] < best_characteristic:
                    best_characteristic = track[vertex]
                    vertex_to_open = vertex
            if vertex_to_open is None:
                result = dict()
                for x in track:
                    result[x.vertex_id] = track[x]
                return result

            for vertex in [x for x in vertex_to_open.incident_edges()
                           if x.first_vertex == vertex_to_open]:
                current_characteristic = track[vertex_to_open] + vertex.weight
                next_vertex = vertex.incident_vertex(vertex_to_open)
                if (next_vertex not in track) \
                        or track[next_vertex] > current_characteristic:
                    track[next_vertex] = current_characteristic

            not_visited.remove(vertex_to_open)

    def bellman_ford(self, start_vertex):
        distance = dict()
        for vertex in self.vertices:
            distance[vertex.vertex_id] = float("Inf")
        distance[start_vertex] = 0
        for i in range(len(self.vertices) - 1):
            for edge in self.edges:
                if distance[edge.first_vertex.vertex_id] != float("Inf") \
                        and distance[edge.first_vertex.vertex_id] \
                        + edge.weight \
                        < distance[edge.second_vertex.vertex_id]:
                    distance[edge.second_vertex.vertex_id] \
                        = distance[edge.first_vertex.vertex_id] + edge.weight
        for edge in self.edges:
            if distance[edge.first_vertex.vertex_id] != float("Inf") \
                    and distance[edge.first_vertex.vertex_id] \
                    + edge.weight < distance[edge.second_vertex.vertex_id]:
                raise ValueError("Found negative weight cycle")
        return distance
