'''
Created Date: 2023-03-25
Qn: You are given an integer n. There is an undirected graph with n nodes,
    numbered from 0 to n - 1. You are given a 2D integer array edges where
    edges[i] = [ai, bi] denotes that there exists an undirected edge connecting
    nodes ai and bi.

    Return the number of pairs of different nodes that are unreachable from
    each other.
Link: https://leetcode.com/problems/count-unreachable-pairs-of-nodes-in-an-undirected-graph/
Notes:
    - total pair of connections = n * (n-1) // 2
    - find the number of nodes in each connected component and subtract from
      total
'''
from collections import defaultdict

def countPairs(n: int, edges: list[list[int]]) -> int:
    graph = defaultdict(list)
    for a, b in edges:
        graph[a].append(b)
        graph[b].append(a)

    visited = [False] * n
    def dfs(i: int) -> int:
        if visited[i]: return 0
        visited[i] = True
        res = 1
        for nei in graph[i]:
            res += dfs(nei)
        return res
    total = n * (n-1) // 2
    for node in range(n):
        if not visited[node]:
            reacheable = dfs(node)
            total -= reacheable * (reacheable - 1) // 2
    return total

if __name__ == '__main__':
    n1, e1 = 3, [[0,1],[0,2],[1,2]]
    n2, e2 = 7, [[0,2],[0,5],[2,4],[1,6],[5,4]]

    print(countPairs(n1, e1))
    print(countPairs(n2, e2))
