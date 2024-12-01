"""
Created Date: 2024-11-30
Qn: You are given a 0-indexed 2D integer array pairs where pairs[i] = [starti,
    endi]. An arrangement of pairs is valid if for every index i where 1 <= i <
    pairs.length, we have endi-1 == starti.

    Return any valid arrangement of pairs.

    Note: The inputs will be generated such that there exists a valid
    arrangement of pairs.
Link: https://leetcode.com/problems/valid-arrangement-of-pairs/
Notes:
    - use indegree and outdegree to find the start node
    - exhaustively connect the node
    - reverse and return pairwise
"""

import unittest
from collections import defaultdict, deque
from itertools import pairwise


class Solution:
    def validArguments(self, pairs: list[list[int]]) -> list[list[int]]:
        graph = defaultdict(deque)
        indegree, outdegree = defaultdict(int), defaultdict(int)

        for a, b in pairs:
            graph[a].append(b)
            outdegree[a] += 1
            indegree[b] += 1

        result = []
        start = 0
        for node, count in outdegree.items():
            if count == indegree[node] + 1:
                start = node
                break
        else:
            start = pairs[0][0]

        node_stack = [start]
        while node_stack:
            node = node_stack[-1]
            if graph[node]:
                nei = graph[node].popleft()
                node_stack.append(nei)
            else:
                result.append(node)
                node_stack.pop()
        return [list(p) for p in pairwise(reversed(result))]


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_validArguments1(self):
        p = [[5, 1], [4, 5], [11, 9], [9, 4]]
        expected = [[11, 9], [9, 4], [4, 5], [5, 1]]
        self.assertEqual(self.sol.validArguments(p), expected)

    def test_validArguments2(self):
        p = [[1, 3], [3, 2], [2, 1]]
        expected = [[1, 3], [3, 2], [2, 1]]
        self.assertEqual(self.sol.validArguments(p), expected)

    def test_validArguments3(self):
        p = [[1, 2], [1, 3], [2, 1]]
        expected = [[1, 2], [2, 1], [1, 3]]
        self.assertEqual(self.sol.validArguments(p), expected)


if __name__ == '__main__':
    unittest.main()
