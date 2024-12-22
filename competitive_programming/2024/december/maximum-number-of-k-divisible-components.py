"""
Created Date: 2024-12-21
Qn: There is an undirected tree with n nodes labeled from 0 to n - 1. You are
    given the integer n and a 2D integer array edges of length n - 1, where
    edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi
    in the tree.

    You are also given a 0-indexed integer array values of length n, where
    values[i] is the value associated with the ith node, and an integer k.

    A valid split of the tree is obtained by removing any set of edges,
    possibly empty, from the tree such that the resulting components all have
    values that are divisible by k, where the value of a connected component is
    the sum of the values of its nodes.

    Return the maximum number of components in any valid split.
Link: https://leetcode.com/problems/maximum-number-of-k-divisible-components/
Notes:
    - use graph
"""

import unittest
from collections import defaultdict


class Solution:
    def maxKDivisibleComponents(
        self, n: int, edges: list[list[int]], values: list[int], k: int
    ) -> int:
        adj = defaultdict(list)

        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)

        res = 0
        def dfs(cur: int, parent: int) -> int:
            total = values[cur]
            for nei in adj[cur]:
                if nei != parent:
                    total += dfs(nei, cur)
            if total % k == 0:
                nonlocal res
                res += 1
            return total

        dfs(0, -1)
        return res


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_maxDvisibleComponents1(self):
        n = 5
        e = [[0, 2], [1, 2], [1, 3], [2, 4]]
        v = [1, 8, 1, 4, 4]
        k = 6
        expected = 2
        self.assertEqual(expected, self.sol.maxKDivisibleComponents(n, e, v, k))

    def test_maxDvisibleComponents2(self):
        n = 7
        e = [[0, 1], [0, 2], [1, 3], [1, 4]]
        v = [3, 0, 6, 1, 5, 2, 1]
        k = 3
        expected = 3
        self.assertEqual(expected, self.sol.maxKDivisibleComponents(n, e, v, k))


if __name__ == '__main__':
    unittest.main()
