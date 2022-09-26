from graph.vertex import Vertex

class Graph:
    def __init__(self, vertices):
        self.vertices = [Vertex(i) for i in range(vertices)]

    def connect_vertices(self, first_vertex_index, second_vertex_index, weight=1):
        return Vertex.connect(self.vertices[first_vertex_index],
                              self.vertices[second_vertex_index],
                              weight, self)

    def depth_first_search(self, vertex_index):
        start_vertex = self.vertices[vertex_index]
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
