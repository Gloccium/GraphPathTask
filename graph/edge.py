class Edge:
    def __init__(self, first_vertex, second_vertex, weight=1):
        self.first_vertex = first_vertex
        self.second_vertex = second_vertex
        self.weight = weight

    def get_opposite_vertex(self, vertex):
        if self.first_vertex == vertex:
            return self.second_vertex
        return self.first_vertex
