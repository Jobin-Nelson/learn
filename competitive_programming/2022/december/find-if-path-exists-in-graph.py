'''
Created Date: 2022-12-19
Qn: There is a bi-directional graph with n vertices, where each vertex is
    labeled from 0 to n - 1 (inclusive). The edges in the graph are represented
    as a 2D integer array edges, where each edges[i] = [ui, vi] denotes a
    bi-directional edge between vertex ui and vertex vi. Every vertex pair is
    connected by at most one edge, and no vertex has an edge to itself.

    You want to determine if there is a valid path that exists from vertex
    source to vertex destination.

    Given edges and the integers n, source, and destination, return true if
    there is a valid path from source to destination, or false otherwise.
Link: https://leetcode.com/problems/find-if-path-exists-in-graph/
Notes:
    - use dfs or bfs
'''
from collections import defaultdict
def validPath(n: int, edges: list[list[int]], source: int, destination: int) -> bool:
    graph = defaultdict(list)

    for (s, d) in edges:
        graph[s].append(d)
        graph[d].append(s)

    graph[source]
    visited = set()

    def dfs(cur_node: int) -> bool:
        if cur_node == destination: return True
        
        if cur_node in visited: return False
        visited.add(cur_node)
        for nei in graph[cur_node]:
            if dfs(nei): return True
        return False
    return dfs(source)
    

if __name__ == '__main__':
    n1, e1, s1, d1 = 3, [[0,1],[1,2],[2,0]], 0, 2
    n2, e2, s2, d2 = 6, [[0,1],[0,2],[3,5],[5,4],[4,3]], 0, 5

    print(validPath(n1, e1, s1, d1))
    print(validPath(n2, e2, s2, d2))
