"""
Created Date: 2025-03-23
Qn: You are in a city that consists of n intersections numbered from 0 to n - 1
    with bi-directional roads between some intersections. The inputs are
    generated such that you can reach any intersection from any other
    intersection and that there is at most one road between any two
    intersections.

    You are given an integer n and a 2D integer array roads where roads[i] =
    [ui, vi, timei] means that there is a road between intersections ui and vi
    that takes timei minutes to travel. You want to know in how many ways you
    can travel from intersection 0 to intersection n - 1 in the shortest amount
    of time.

    Return the number of ways you can arrive at your destination in the
    shortest amount of time. Since the answer may be large, return it modulo
    109 + 7.
Link: https://leetcode.com/problems/number-of-ways-to-arrive-at-destination/
Notes:
"""

import unittest
from collections import defaultdict
import heapq


class Solution:
    def countPaths(self, n: int, roads: list[list[int]]) -> int:
        adj = defaultdict(list)
        for u, v, w in roads:
            adj[u].append((w, v))
            adj[v].append((w, u))

        MOD = 10**9 + 7
        min_heap = [(0, 0)]
        min_cost = [float('inf')] * n
        path_count = [0] * n
        path_count[0] = 1

        while min_heap:
            cost, node = heapq.heappop(min_heap)
            for nei_cost, nei in adj[node]:
                if nei_cost + cost < min_cost[nei]:
                    min_cost[nei] = nei_cost + cost
                    path_count[nei] = path_count[node]
                    heapq.heappush(min_heap, (cost + nei_cost, nei))
                elif nei_cost + cost == min_cost[nei]:
                    path_count[nei] = (path_count[node] + path_count[nei]) % MOD
        return path_count[n - 1]


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_countPaths1(self):
        n = 7
        r = [
            [0, 6, 7],
            [0, 1, 2],
            [1, 2, 3],
            [1, 3, 3],
            [6, 3, 3],
            [3, 5, 1],
            [6, 5, 1],
            [2, 5, 1],
            [0, 4, 5],
            [4, 6, 2],
        ]
        expected = 4
        self.assertEqual(expected, self.sol.countPaths(n, r))

    def test_countPaths2(self):
        n = 2
        r = [[1, 0, 10]]
        expected = 1
        self.assertEqual(expected, self.sol.countPaths(n, r))


if __name__ == '__main__':
    unittest.main()
