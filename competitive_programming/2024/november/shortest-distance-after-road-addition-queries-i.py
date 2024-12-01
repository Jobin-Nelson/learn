"""
Created Date: 2024-11-27
Qn: You are given an integer n and a 2D integer array queries.

    There are n cities numbered from 0 to n - 1. Initially, there is a
    unidirectional road from city i to city i + 1 for all 0 <= i < n - 1.

    queries[i] = [ui, vi] represents the addition of a new unidirectional road
    from city ui to city vi. After each query, you need to find the length of
    the shortest path from city 0 to city n - 1.

    Return an array answer where for each i in the range [0, queries.length -
    1], answer[i] is the length of the shortest path from city 0 to city n - 1
    after processing the first i + 1 queries.
Link: https://leetcode.com/problems/shortest-distance-after-road-addition-queries-i/
Notes:
    - use bfs on graph
"""

import unittest
from collections import deque


class Solution:
    def shortestDistanceAfterQueries(
        self, n: int, queries: list[list[int]]
    ) -> list[int]:
        adj = [[i+1] for i in range(n)]
        def shortest_path() -> int:
            q = deque([(0, 0)]) # node, length
            visited = set([0])
            while q:
                node, length = q.popleft()
                if node == n-1:
                    return length
                for nei in adj[node]:
                    if nei not in visited:
                        visited.add(nei)
                        q.append((nei, length +1))
            return -1
        res = []
        for src, dst in queries:
            adj[src].append(dst)
            res.append(shortest_path())
        return res


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_shortestDistanceAfterQueries1(self):
        n = 5
        q = [[2, 4], [0, 2], [0,4]]
        expected = [3, 2, 1]
        self.assertEqual(self.sol.shortestDistanceAfterQueries(n, q), expected)

    def test_shortestDistanceAfterQueries2(self):
        n = 4
        q = [[0, 3], [0, 2]]
        expected = [1, 1]
        self.assertEqual(self.sol.shortestDistanceAfterQueries(n, q), expected)


if __name__ == '__main__':
    unittest.main()
