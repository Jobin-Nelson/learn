'''
Created Date: 2023-04-09
Qn: There is a directed graph of n colored nodes and m edges. The nodes are
    numbered from 0 to n - 1.

    You are given a string colors where colors[i] is a lowercase English letter
    representing the color of the ith node in this graph (0-indexed). You are
    also given a 2D array edges where edges[j] = [aj, bj] indicates that there
    is a directed edge from node aj to node bj.

    A valid path in the graph is a sequence of nodes x1 -> x2 -> x3 -> ... ->
    xk such that there is a directed edge from xi to xi+1 for every 1 <= i < k.
    The color value of the path is the number of nodes that are colored the
    most frequently occurring color along that path.

    Return the largest color value of any valid path in the given graph, or -1
    if the graph contains a cycle.
Link: https://leetcode.com/problems/largest-color-value-in-a-directed-graph/
Notes:
    - use topological sort: (u -> v) u always comes before v
    - 2d array to keep track of the count for each node
'''
from collections import deque

def largestPathValue(colors: str, edges: list[list[int]]) -> int:
    n, k = len(colors), 26
    indegrees = [0] * n
    adj = [[] for _ in range(n)]

    for u, v in edges:
        adj[u].append(v)
        indegrees[v] += 1

    zero_indegree = deque(i for i in range(n) if indegrees[i] == 0)
    dp = [[0] * k for _ in range(n)]

    max_count = visited = 0

    while zero_indegree:
        u = zero_indegree.popleft()
        visited += 1
        dp[u][ord(colors[u]) - ord('a')] += 1
        for v in adj[u]:
            for i in range(k):
                dp[v][i] = max(dp[v][i], dp[u][i])
            indegrees[v] -= 1
            if indegrees[v] == 0: zero_indegree.append(v)
        max_count = max(max_count, dp[u][ord(colors[u]) - ord('a')])

    return max_count if visited == n else -1

if __name__ == '__main__':
    c1, e1 = "abaca", [[0,1],[0,2],[2,3],[3,4]]
    c2, e2 = "a", [[0,0]]

    print(largestPathValue(c1, e1))
    print(largestPathValue(c2, e2))
