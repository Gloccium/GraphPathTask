from graph.edge import Edge


class Vertex:
    def __init__(self, vertex_id):
        self.edges = []
        self.vertex_id = vertex_id

    @property
    def incident_vertices(self):
        return [edge.incident_vertex(self) for edge in self.edges]

    def incident_edges(self):
        for edge in self.edges:
            yield edge

    @staticmethod
    def connect(first_vertex, second_vertex, weight, graph):
        if first_vertex not in graph.vertices \
                or second_vertex not in graph.vertices:
            raise ValueError()
        edge = Edge(first_vertex, second_vertex, weight)
        first_vertex.edges.append(edge)
        second_vertex.edges.append(edge)
        return edge
