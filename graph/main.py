class Vertex:
    def __init__(self, key):
        self.id = key
        self.connected_to = {}

    def add_neighbor(self, neighbor, weight=0):
        self.connected_to[neighbor] = weight

    def __str__(self):
        return str(self.id) + " connectedTo: " + str([x.id for x in self.connected_to])

    def connections(self):
        return self.connected_to.keys()

    def id(self):
        return self.id

    def weight(self, neighbor):
        return self.connected_to[neighbor]


class Graph:
    def __init__(self):
        self.vertices = {}
        self.num_vertices = 0

    def add_vertex(self, key):
        self.num_vertices += 1
        new_vertex = Vertex(key)
        self.vertices[key] = new_vertex
        return new_vertex

    def vertex(self, n):
        if n in self.vertices:
            return self.vertices[n]
        else:
            return None

    def __contains__(self, n):
        return n in self.vertices

    def add_edge(self, f, t, weight=0):
        if f not in self.vertices:
            nv = self.add_vertex(f)
        if t not in self.vertices:
            nv = self.add_vertex(t)

        self.vertices[f].add_neighbor(self.vertices[t], weight)

    def vertices(self):
        return self.vertices.keys()

    def __iter__(self):
        return iter(self.vertices.values())
