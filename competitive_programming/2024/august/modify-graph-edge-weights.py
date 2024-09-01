"""
Created Date: 2024-08-30
Qn: You are given an undirected weighted connected graph containing n nodes
    labeled from 0 to n - 1, and an integer array edges where edges[i] = [ai,
    bi, wi] indicates that there is an edge between nodes ai and bi with weight
    wi.

    Some edges have a weight of -1 (wi = -1), while others have a positive
    weight (wi > 0).

    Your task is to modify all edges with a weight of -1 by assigning them
    positive integer values in the range [1, 2 * 109] so that the shortest
    distance between the nodes source and destination becomes equal to an
    integer target. If there are multiple modifications that make the shortest
    distance between source and destination equal to target, any of them will
    be considered correct.

    Return an array containing all edges (even unmodified ones) in any order if
    it is possible to make the shortest distance from source to destination
    equal to target, or an empty array if it's impossible.

    Note: You are not allowed to modify the weights of edges with initial
    positive weights.
Link: https://leetcode.com/problems/modify-graph-edge-weights/
Notes:
    - use dijkstra algo
"""

import heapq


def modifiedGraphEdges(
    n: int, edges: list[list[int]], source: int, destination: int, target: int
) -> list[list[int]]:
    graph = [[] for _ in range(n)]
    for u, v, w in edges:
        if w != -1:
            graph[u].append((v, w))
            graph[v].append((u, w))

    def dijkstra(
        graph: list[list[tuple[int, int]]], source: int, destination: int
    ) -> int:
        min_distance = [int(2e9)] * len(graph)
        min_distance[source] = 0
        min_heap = [(0, source)]

        while min_heap:
            d, u = heapq.heappop(min_heap)
            if d > min_distance[u]:
                continue
            for v, w in graph[u]:
                if d + w < min_distance[v]:
                    min_distance[v] = d + w
                    heapq.heappush(min_heap, (min_distance[v], v))
        return min_distance[destination]

    current_shortest_distance = dijkstra(graph, source, destination)
    if current_shortest_distance < target:
        return []

    if current_shortest_distance == target:
        for edge in edges:
            if edge[2] == -1:
                edge[2] = int(2e9)
        return edges

    for i, (u, v, w) in enumerate(edges):
        if w != -1:
            continue

        edges[i][2] = 1
        graph[u].append((v, 1))
        graph[v].append((u, 1))

        new_distance = dijkstra(graph, source, destination)

        if new_distance <= target:
            edges[i][2] += target - new_distance

            for j in range(i + 1, len(edges)):
                if edges[j][2] == -1:
                    edges[j][2] = int(2e9)
            return edges
    return []


if __name__ == '__main__':
    n1, e1, s1, d1, t1 = 5, [[4, 1, -1], [2, 0, -1], [0, 3, -1], [4, 3, -1]], 0, 1, 5
    n2, e2, s2, d2, t2 = 5, [[0, 1, -1], [0, 2, 5]], 0, 2, 6
    n3, e3, s3, d3, t3 = 4, [[1, 0, 4], [1, 2, 3], [2, 3, 5], [0, 3, -1]], 0, 2, 6

    print(modifiedGraphEdges(n1, e1, s1, d1, t1))
    print(modifiedGraphEdges(n2, e2, s2, d2, t2))
    print(modifiedGraphEdges(n3, e3, s3, d3, t3))
