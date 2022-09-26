class Vertex:
    def __init__(self):
        self.edges = []

    @property
    def incident_vertices(self):
        return [edge.incident_vertex(self) for edge in self.edges]

    def incident_edges(self):
        for edge in self.edges:
            yield edge
