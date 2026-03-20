"""
Created Date: 2026-01-27
Qn: You are given a directed, weighted graph with n nodes labeled from 0 to n -
    1, and an array edges where edges[i] = [ui, vi, wi] represents a directed
    edge from node ui to node vi with cost wi.

    Each node ui has a switch that can be used at most once: when you arrive at
    ui and have not yet used its switch, you may activate it on one of its
    incoming edges vi → ui reverse that edge to ui → vi and immediately
    traverse it.

    The reversal is only valid for that single move, and using a reversed edge
    costs 2 * wi.

    Return the minimum total cost to travel from node 0 to node n - 1. If it is
    not possible, return -1. Link:
https://leetcode.com/problems/minimum-cost-path-with-edge-reversals/
Notes:
    - use dijkstra
"""

import heapq
import unittest
from sys import maxsize


class Solution:
    def minCost(self, n: int, edges: list[list[int]]) -> int:
        g = [[] for _ in range(n)]
        for x, y, w in edges:
            g[x].append((y, w))
            g[y].append((x, 2 * w))

        dist = [maxsize] * n
        visited = [False] * n
        heap = [(0, 0)]  # distance, node

        while heap:
            cur_dist, x = heapq.heappop(heap)
            if x == n -1:
                return cur_dist
            if visited[x]:
                continue
            visited[x] = True
            for y, w in g[x]:
                new_dist = cur_dist + w
                if new_dist < dist[y]:
                    dist[y] = new_dist
                    heapq.heappush(heap, (new_dist, y))
        return -1


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test1(self):
        n = 4
        e = [[0, 1, 3], [3, 1, 1], [2, 3, 4], [0, 2, 2]]
        expected = 5
        self.assertEqual(expected, self.sol.minCost(n, e))

    def test2(self):
        n = 4
        e = [[0, 2, 1], [2, 1, 1], [1, 3, 1], [2, 3, 3]]
        expected = 3
        self.assertEqual(expected, self.sol.minCost(n, e))


if __name__ == '__main__':
    unittest.main()
