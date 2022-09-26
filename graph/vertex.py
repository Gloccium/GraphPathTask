class Vertex:
    def __init__(self, vertex_number):
        self.edges = []
        self.vertex_number = vertex_number

    @property
    def incident_vertices(self):
        return [edge.incident_vertex(self) for edge in self.edges]

    def incident_edges(self):
        for edge in self.edges:
            yield edge
