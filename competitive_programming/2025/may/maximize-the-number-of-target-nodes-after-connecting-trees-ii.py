"""
Created Date: 2025-05-29
Qn: There exist two undirected trees with n and m nodes, labeled from [0, n -
    1] and [0, m - 1], respectively.

    You are given two 2D integer arrays edges1 and edges2 of lengths n - 1 and
    m - 1, respectively, where edges1[i] = [ai, bi] indicates that there is an
    edge between nodes ai and bi in the first tree and edges2[i] = [ui, vi]
    indicates that there is an edge between nodes ui and vi in the second tree.

    Node u is target to node v if the number of edges on the path from u to v
    is even. Note that a node is always target to itself.

    Return an array of n integers answer, where answer[i] is the maximum
    possible number of nodes that are target to node i of the first tree if you
    had to connect one node from the first tree to another node in the second
    tree.

    Note that queries are independent from each other. That is, for every query
    you will remove the added edge before proceeding to the next query.
Link: https://leetcode.com/problems/maximize-the-number-of-target-nodes-after-connecting-trees-ii/
Notes:
    - use bfs or dfs
"""

import unittest
from collections import deque


class Solution:
    def maxTargetNodes(
        self, edges1: list[list[int]], edges2: list[list[int]]
    ) -> list[int]:
        def bfs(node: int, adj: list[list[int]], color: list[int]) -> int:
            q = deque([(node, -1, 0)])
            res = 0
            while q:
                node, parent, level = q.popleft()
                res += 1 - (level & 1)
                color[node] = level & 1
                for nei in adj[node]:
                    if nei != parent:
                        q.append((nei, node, level + 1))
            return res

        def build(edges: list[list[int]], color: list[int]) -> tuple[int, int]:
            n = len(edges) + 1
            adj = [[] for _ in range(n)]
            for u, v in edges:
                adj[u].append(v)
                adj[v].append(u)

            res = bfs(0, adj, color)
            return (res, n - res)

        n = len(edges1) + 1
        m = len(edges2) + 1
        color1 = [0] * n
        color2 = [0] * m
        depth1 = build(edges1, color1)
        depth2 = build(edges2, color2)
        max_depth2 = max(depth2)
        return [depth1[color1[i]] + max_depth2 for i in range(n)]


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_maxTargetNodes1(self):
        e1 = [[0, 1], [0, 2], [2, 3], [2, 4]]
        e2 = [[0, 1], [0, 2], [0, 3], [2, 7], [1, 4], [4, 5], [4, 6]]
        expected = [8, 7, 7, 8, 8]
        self.assertEqual(expected, self.sol.maxTargetNodes(e1, e2))

    def test_maxTargetNodes2(self):
        e1 = [[0, 1], [0, 2], [0, 3], [0, 4]]
        e2 = [[0, 1], [1, 2], [2, 3]]
        expected = [3, 6, 6, 6, 6]
        self.assertEqual(expected, self.sol.maxTargetNodes(e1, e2))


if __name__ == '__main__':
    unittest.main()
