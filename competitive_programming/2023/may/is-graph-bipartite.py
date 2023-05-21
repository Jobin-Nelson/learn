'''
Created Date: 2023-05-19
Qn: There is an undirected graph with n nodes, where each node is numbered
    between 0 and n - 1. You are given a 2D array graph, where graph[u] is an
    array of nodes that node u is adjacent to. More formally, for each v in
    graph[u], there is an undirected edge between node u and node v. The graph
    has the following properties:

        There are no self-edges (graph[u] does not contain u). There are no
        parallel edges (graph[u] does not contain duplicate values). If v is in
        graph[u], then u is in graph[v] (the graph is undirected). The graph
        may not be connected, meaning there may be two nodes u and v such that
        there is no path between them.

    A graph is bipartite if the nodes can be partitioned into two independent
    sets A and B such that every edge in the graph connects a node in set A and
    a node in set B.

    Return true if and only if it is bipartite.
Link: https://leetcode.com/problems/is-graph-bipartite/
Notes:
    - use bfs
    - alternate between two sets after each layer of bfs
'''
from collections import deque

def isBipartite(graph: list[list[int]]) -> bool:
    N = len(graph)
    visited = [0] * N

    def bfs(i: int) -> bool:
        if visited[i]: return True
        
        visited[i] = 1
        q = deque([i])

        while q:
            node = q.popleft()
            for nei in graph[node]:
                if visited[nei] == visited[node]:
                    return False
                elif not visited[nei]:
                    visited[nei] = -1 * visited[node]
                    q.append(nei)
        return True

    for i in range(N):
        if not bfs(i): return False
    
    return True

if __name__ == '__main__':
    g1 = [[1,2,3],[0,2],[0,1,3],[0,2]]
    g2 = [[1,3],[0,2],[1,3],[0,2]]

    print(isBipartite(g1))
    print(isBipartite(g2))

