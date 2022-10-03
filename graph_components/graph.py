from graph_components.vertex import Vertex


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
