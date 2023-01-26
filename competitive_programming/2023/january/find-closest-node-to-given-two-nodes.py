'''
Created Date: 2023-01-25
Qn: You are given a directed graph of n nodes numbered from 0 to n - 1, where
    each node has at most one outgoing edge.

    The graph is represented with a given 0-indexed array edges of size n,
    indicating that there is a directed edge from node i to node edges[i]. If
    there is no outgoing edge from i, then edges[i] == -1.

    You are also given two integers node1 and node2.

    Return the index of the node that can be reached from both node1 and node2,
    such that the maximum between the distance from node1 to that node, and from
    node2 to that node is minimized. If there are multiple answers, return the node
    with the smallest index, and if no possible answer exists, return -1.

    Note that edges may contain cycles.
Link: https://leetcode.com/problems/find-closest-node-to-given-two-nodes/
Notes:
    - use bfs
    - find shortest distance node
'''
from collections import deque

def closestMeetingNode(edges: list[int], node1: int, node2: int) -> int:
    N = len(edges)
    dist1, dist2 = [float('inf')] * N, [float('inf')] * N

    def bfs(node: int, dist: list[float]):
        q = deque([node])
        visited = [False] * N
        dist[node] = 0
        while q:
            node = q.popleft()
            if visited[node]: continue
            visited[node] = True
            nei = edges[node]
            if nei != -1 and not visited[nei]:
                dist[nei] = 1 + dist[node]
                q.append(nei)

    bfs(node1, dist1)
    bfs(node2, dist2)

    res = -1
    cur_dist = float('inf')
    for i in range(N):
        if cur_dist > max(dist1[i], dist2[i]):
            res = i
            cur_dist = max(dist1[i], dist2[i])
    return res

if __name__ == '__main__':
    e1, n11, n12 = [2, 2, 3, -1], 0, 1
    e2, n21, n22 = [1, 2, -1], 0, 2

    print(closestMeetingNode(e1, n11, n12))
    print(closestMeetingNode(e2, n22, n22))
