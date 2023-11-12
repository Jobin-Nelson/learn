'''
Created Date: 2023-11-11
Qn: There is a directed weighted graph that consists of n nodes numbered from
    0 to n - 1. The edges of the graph are initially represented by the given
      array edges where edges[i] = [fromi, toi, edgeCosti] meaning that there
      is an edge from fromi to toi with the cost edgeCosti.

    Implement the Graph class:

        - Graph(int n, int[][] edges) initializes the object with n nodes and
          the given edges. 
        - addEdge(int[] edge) adds an edge to the list of edges where edge =
          [from, to, edgeCost]. It is guaranteed that there is no edge between
          the two nodes before adding this one. 
        - int shortestPath(int node1, int node2) returns the minimum cost of a
          path from node1 to node2. If no path exists, return -1. The cost of a
          path is the sum of the costs of the edges in the path.

Link: https://leetcode.com/problems/design-graph-with-shortest-path-calculator/
Notes:
    - use dijkstra's algorithm to find the shortest path
'''

from collections import defaultdict
import heapq

class Graph:
    def __init__(self, n: int, edges: list[list[int]]):
        self.g = [[] for _ in range(n)]
        for u, v, w in edges:
            self.g[u].append((v, w))

    def addEdge(self, edge: list[int]) -> None:
        u, v, w = edge
        self.g[u].append((v, w))

    def shortestPath(self, node1: int, node2: int) -> int:
        h = [(0, node1)]
        visited = [False] * len(self.g)
        while h:
            w, node = heapq.heappop(h)
            if node == node2: return w
            if visited[node]: continue
            visited[node] = True
            for nei, nei_w in self.g[node]:
                if not visited[nei]:
                    heapq.heappush(h, (w + nei_w, nei))
        return -1

if __name__ == '__main__':
    g = Graph(4, [[0, 2, 5], [0, 1, 2], [1, 2, 1], [3, 0, 3]])
    print(g.shortestPath(3, 2))
    print(g.shortestPath(0, 3))
    g.addEdge([1, 3, 4])
    print(g.shortestPath(0, 3))
