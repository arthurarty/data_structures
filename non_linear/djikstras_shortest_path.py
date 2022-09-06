import sys
from dataclasses import dataclass
from typing import List


@dataclass
class Graph:
    no_of_vertices: int
    graph: List[List[int]] = lambda x: [[]]

    def print_solution(self, dist):
        print("Vertex \t Distance from source")
        for node in range(self.no_of_vertices):
            print(node, "\t", dist[node])

    def min_distance(self, dist: List[int], spt_set: List[bool]):
        """
        A utility function to find the vertex with minimum distance value,
        from the set of vertices not yet included in the shortest path tree
        :param dist: List[int] where int is max_possible int in python
        :param spt_set: List[bool]
        :return:
        """
        min_value = sys.maxsize
        min_index = None
        for ii in range(self.no_of_vertices):
            if dist[ii] < min_value and spt_set[ii] is False:
                min_value = dist[ii]
                min_index = ii
        return min_index

    def dijkstra(self, src):
        dist = [sys.maxsize] * self.no_of_vertices
        dist[src] = 0
        spt_set = [False] * self.no_of_vertices  # tracks whether we have set the shortest path

        for ii in range(self.no_of_vertices):
            # pick the min distance vertex from the set of vertices not yet processed
            # x is always equal to src in first iteration
            x = self.min_distance(dist, spt_set)
            spt_set[x] = True

            # update dist value of the adjacent vertices
            # of the picked vertex only if the current distance
            # is greater than new distance and the vertex is not in the shortest_path_tree
            for y in range(self.no_of_vertices):
                if self.graph[x][y] <= 0:
                    # if value is 0 it mostly a placeholder.
                    # if value is 0, those vertexes do not have an edge connecting them.
                    continue
                if spt_set[y] is True:
                    # we already visited this vertex.
                    continue
                proposed_shortest_distance = dist[x] + self.graph[x][y]
                if proposed_shortest_distance < dist[y]:
                    # i.e. new route is shorted than the last route.
                    dist[y] = proposed_shortest_distance
        self.print_solution(dist)


if __name__ == "__main__":
    g = Graph(9)
    g.graph = [
        [0, 4, 0, 0, 0, 0, 0, 8, 0],
        [4, 0, 8, 0, 0, 0, 0, 11, 0],
        [0, 8, 0, 7, 0, 4, 0, 0, 2],
        [0, 0, 7, 0, 9, 14, 0, 0, 0],
        [0, 0, 0, 9, 0, 10, 0, 0, 0],
        [0, 0, 4, 14, 10, 0, 2, 0, 0],
        [0, 0, 0, 0, 0, 2, 0, 1, 6],
        [8, 11, 0, 0, 0, 0, 1, 0, 7],
        [0, 0, 2, 0, 0, 0, 6, 7, 0]
    ]
    g.dijkstra(0)
    print(g.graph)
