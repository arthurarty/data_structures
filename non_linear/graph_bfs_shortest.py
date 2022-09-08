import collections


class Graph:
    def __init__(self, no_of_vertices=None):
        self.no_of_vertices = no_of_vertices
        self.graph_dict = dict.fromkeys(range(no_of_vertices), [])

    def connect(self, vertex_1: int, vertex_2: int):
        self.graph_dict[vertex_1] = self.graph_dict[vertex_1] + [vertex_2]
        self.graph_dict[vertex_2] = self.graph_dict[vertex_2] + [vertex_1]

    def find_all_distances(self, start_value: int):
        visited_nodes = {}
        queue = collections.deque([(start_value, 0)])
        """
        Using a deque is faster than trying to use a list.
        Reason being, collections.deque is implemented as a doubly linked list.
        linked list is better at popping and appending at both ends.
        """
        dist = [-1] * self.no_of_vertices  # make default list = [-1, -1, -1, ] len(dist) = no_of_vertices
        while queue:
            current_value, level = queue.popleft()
            if current_value not in visited_nodes.keys():
                visited_nodes[current_value] = level
                dist[current_value] = visited_nodes[current_value] * 6
                for next_vertex in self.graph_dict[current_value]:
                    queue.append((next_vertex, level+1))
        dist.remove(0)  # we expect just one zero which represents the start_value.
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
