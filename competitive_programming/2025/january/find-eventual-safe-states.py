"""
Created Date: 2025-01-24
Qn: There is a directed graph of n nodes with each node labeled from 0 to n -
    1. The graph is represented by a 0-indexed 2D integer array graph where
    graph[i] is an integer array of nodes adjacent to node i, meaning there is
    an edge from node i to each node in graph[i].

    A node is a terminal node if there are no outgoing edges. A node is a safe
    node if every possible path starting from that node leads to a terminal
    node (or another safe node).

    Return an array containing all the safe nodes of the graph. The answer
    should be sorted in ascending order.
Link: https://leetcode.com/problems/find-eventual-safe-states/
Notes:
    - use dfs
"""

import unittest


class Solution:
    def eventualSafeNodes(self, graph: list[list[int]]) -> list[int]:
        n = len(graph)
        safe = {}

        def dfs(i: int) -> bool:
            if i in safe:
                return safe[i]
            safe[i] = False
            for nei in graph[i]:
                if not dfs(nei):
                    return False
            safe[i] = True
            return True

        return [i for i in range(n) if dfs(i)]


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_eventualSafeNodes1(self):
        g = [[1, 2], [2, 3], [5], [0], [5], [], []]
        expected = [2, 4, 5, 6]
        self.assertEqual(expected, self.sol.eventualSafeNodes(g))

    def test_eventualSafeNodes2(self):
        g = [[1, 2], [2, 3], [5], [0], [5], [], []]
        expected = [2, 4, 5, 6]
        self.assertEqual(expected, self.sol.eventualSafeNodes(g))


if __name__ == '__main__':
    unittest.main()
