class Graph:
    def __init__(self, no_of_vertices=None):
        self.no_of_vertices = no_of_vertices
        self.graph_dict = dict.fromkeys(range(no_of_vertices), [])

    def connect(self, vertex_1: int, vertex_2: int):
        self.graph_dict[vertex_1] = self.graph_dict[vertex_1] + [vertex_2]
        self.graph_dict[vertex_2] = self.graph_dict[vertex_2] + [vertex_1]

    def find_all_distances(self, start_value: int):
        visited_nodes = set()
        queue = [(start_value, 0)]
        dist = []
        track_level = {}
        while queue:
            current_value, level = queue.pop(0)
            if current_value not in visited_nodes:
                visited_nodes.add(current_value)
                track_level[current_value] = level
                for next_vertex in self.graph_dict[current_value]:
                    queue.append((next_vertex, level+1))
        for ii in range(self.no_of_vertices):
            if ii == start_value:
                continue
            if track_level.get(ii) is None:
                dist.append(-1)
            else:
                dist.append((track_level[ii]) * 6)
        return " ".join(map(str, dist))


if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n, m = [int(value) for value in input().split()]
        graph = Graph(n)
        for i in range(m):
            x, y = [int(x) for x in input().split()]
            graph.connect(x - 1, y - 1)
        s = int(input())
        print(graph.find_all_distances(s - 1))
