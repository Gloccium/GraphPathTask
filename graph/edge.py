class Edge:
    def __init__(self, first_vertex, second_vertex, weight=1):
        self.first_vertex = first_vertex
        self.second_vertex = second_vertex
        self.weight = weight

    def incident_vertex(self, vertex):
        # Check whether vertices are incident
        if not (self.first_vertex == vertex or self.second_vertex == vertex):
            raise ValueError("Vertices are not incident")

        # Get incident vertex
        if self.first_vertex == vertex:
            return self.second_vertex
        return self.first_vertex
