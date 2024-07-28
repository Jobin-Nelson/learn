"""
Created Date: 2024-07-26
Qn: There are n cities numbered from 0 to n-1. Given the array edges where
    edges[i] = [fromi, toi, weighti] represents a bidirectional and weighted
    edge between cities fromi and toi, and given the integer distanceThreshold.

    Return the city with the smallest number of cities that are reachable
    through some path and whose distance is at most distanceThreshold, If there
    are multiple such cities, return the city with the greatest number.

    Notice that the distance of a path connecting cities i and j is equal to
    the sum of the edges' weights along that path.
Link: https://leetcode.com/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/
Notes:
    - use dijkstra's algo
"""

import heapq
from collections import defaultdict


def findTheCity(n: int, edges: list[list[int]], distanceThreshold: int) -> int:
    graph = defaultdict(list)

    for s, d, w in edges:
        graph[s].append((d, w))
        graph[d].append((s, w))

    def dijkstra(src: int) -> int:
        heap = [(0, src)]
        visited = set()

        while heap:
            dist, node = heapq.heappop(heap)
            if node in visited:
                continue
            visited.add(node)
            for nei, dist2 in graph[node]:
                nei_dist = dist + dist2
                if nei_dist <= distanceThreshold:
                    heapq.heappush(heap, (nei_dist, nei))
        return len(visited) - 1

    res = -1
    min_count = n
    for node in range(n):
        count = dijkstra(node)
        if count <= min_count:
            res, min_count = node, count
    return res


if __name__ == '__main__':
    n1, e1, d1 = 4, [[0, 1, 3], [1, 2, 1], [1, 3, 4], [2, 3, 1]], 4
    n2, e2, d2 = (
        5,
        [[0, 1, 2], [0, 4, 8], [1, 2, 3], [1, 4, 2], [2, 3, 1], [3, 4, 1]],
        2,
    )
    n3, e3, d3 = 5, [[0,1,2],[0,4,8],[1,2,3],[1,4,2],[2,3,1],[3,4,1]], 2

    print(findTheCity(n1, e1, d1))
    print(findTheCity(n2, e2, d2))
    print(findTheCity(n3, e3, d3))
