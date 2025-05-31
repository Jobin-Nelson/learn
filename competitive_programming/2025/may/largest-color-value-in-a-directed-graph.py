"""
Created Date: 2025-05-26
Qn: There is a directed graph of n colored nodes and m edges. The nodes are
    numbered from 0 to n - 1.

    You are given a string colors where colors[i] is a lowercase English letter
    representing the color of the ith node in this graph (0-indexed). You are
    also
    given a 2D array edges where edges[j] = [aj, bj] indicates that there is a
    directed edge from node aj to node bj.

    A valid path in the graph is a sequence of nodes x1 -> x2 -> x3 -> ... -> xk
    such that there is a directed edge from xi to xi+1 for every 1 <= i < k. The
    color value of the path is the number of nodes that are colored the most
    frequently occurring color along that path.

    Return the largest color value of any valid path in the given graph, or -1 if
    the graph contains a cycle.
Link: https://leetcode.com/problems/largest-color-value-in-a-directed-graph/
Notes:
    - use dfs
"""

import unittest
from collections import defaultdict


class Solution:
    def largestPathValue(self, colors: str, edges: list[list[int]]) -> int:
        ord_a = ord('a')
        n = len(colors)
        freq = [[0] * 26 for _ in range(n)]

        # topological sort
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)

        def dfs(node: int) -> int|float:
            if node in path:
                return float('inf')
            if node in visit:
                return 0

            visit.add(node)
            path.add(node)

            color_index = ord(colors[node]) - ord_a
            freq[node][color_index] += 1

            for nei in adj[node]:
                if dfs(nei) == float('inf'):
                    return float('inf')
                for c in range(26):
                    freq[node][c] = max(
                        freq[node][c],
                        (1 if c == color_index else 0) + freq[nei][c]
                    )

            path.remove(node)
            return max(freq[node])

        res = 0
        visit, path = set(), set()

        for i in range(n):
            res = max(dfs(i), res)
        return -1 if res == float('inf') else res


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_largestPathValue1(self):
        c = "abaca"
        e = [[0, 1], [0, 2], [2, 3], [3, 4]]
        expected = 3
        self.assertEqual(expected, self.sol.largestPathValue(c, e))

    def test_largestPathValue2(self):
        c = "a"
        e = [[0, 0]]
        expected = -1
        self.assertEqual(expected, self.sol.largestPathValue(c, e))


if __name__ == '__main__':
    unittest.main()
