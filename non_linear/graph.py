class Graph:
    def __init__(self, vertices=None, graph_dict=None):
        if graph_dict is None and vertices:
            graph_dict = dict.fromkeys(range(vertices), [])
            self.graph_dict = graph_dict
        else:
            self.graph_dict = graph_dict

    def connect(self, x, y):
        self.graph_dict[x] = self.graph_dict[x] + [y]
        self.graph_dict[y] = self.graph_dict[y] + [x]

    def get_vertices(self):
        # get the keys of the dictionary
        return list(self.graph_dict.keys())

    def edges(self):
        return self.findedges()

    def findedges(self):
        edgename = []
        for vertex in self.graph_dict:
            for next_vertex in self.graph_dict[vertex]:
                if {next_vertex, vertex} not in edgename:
                    edgename.append({vertex, next_vertex})
        return edgename

    def find_all_distances(self, start):
        visited_nodes = set()
        queue = [start]
        output_str = ""
        level = 0
        while len(queue) > 0:
            current_node = queue.pop(0)
            dist = level * 6
            if dist:
                output_str += str(dist)
            for next_vertex in self.graph_dict[current_node]:
                if {next_vertex, current_node} not in visited_nodes:
                    queue.append(next_vertex)
                    visited_nodes.add({next_vertex, current_node})
            level += 1
        return output_str





graph_elements = {
    'a': ['b', 'c'],
    'b': ['a', 'd'],
    'c': ['a', 'd'],
    'd': ['e'],
    'e': ['d']
}

g = Graph(5, graph_elements)
# g = Graph(5)
# g.connect(1 -1, 2 -1)
print(g.get_vertices())
print(g.edges())
