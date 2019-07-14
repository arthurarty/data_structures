class Graph:
    def __init__(self, gdict=None):
        if gdict is None:
            gdict = []
        self.gdict = gdict

    def get_vertices(self):
        # get the keys of the dictionary
        return list(self.gdict.keys())

    def edges(self):
        return self.findedges()

    def findedges(self):
        edgename = []
        for vertex in self.gdict:
            for next_vertex in self.gdict[vertex]:
                if {next_vertex, vertex} not in edgename:
                    edgename.append({vertex, next_vertex})
        return edgename

graph_elements = {
    'a': ['b', 'c'],
    'b': ['a', 'd'],
    'c': ['a', 'd'],
    'd': ['e'],
    'e': ['d']
}

g = Graph(graph_elements)
print(g.get_vertices())
print(g.edges())
