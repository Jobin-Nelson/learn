"""
Created Date: 2025-05-28
Qn: There exist two undirected trees with n and m nodes, with distinct labels
    in ranges [0, n - 1] and [0, m - 1], respectively.

    You are given two 2D integer arrays edges1 and edges2 of lengths n - 1 and
    m - 1, respectively, where edges1[i] = [ai, bi] indicates that there is an
    edge between nodes ai and bi in the first tree and edges2[i] = [ui, vi]
    indicates that there is an edge between nodes ui and vi in the second tree.
    You are also given an integer k.

    Node u is target to node v if the number of edges on the path from u to v
    is less than or equal to k. Note that a node is always target to itself.

    Return an array of n integers answer, where answer[i] is the maximum
    possible number of nodes target to node i of the first tree if you have to
    connect one node from the first tree to another node in the second tree.

    Note that queries are independent from each other. That is, for every query
    you will remove the added edge before proceeding to the next query.
Link: https://leetcode.com/problems/maximize-the-number-of-target-nodes-after-connecting-trees-i/
Notes:
    - use bfs or dfs
    - pre calculate hopes for both trees
    - and return node from tree1 + maxhopes2
"""

import unittest
from collections import deque


class Solution:
    def maxTargetNodes(
        self, edges1: list[list[int]], edges2: list[list[int]], k: int
    ) -> list[int]:
        def bfs(node: int, adj: list[list[int]], level: int) -> int:
            q = deque([(-1, node)])

            res = 0
            cur_level = 0
            while q:
                if cur_level > level:
                    break
                for _ in range(len(q)):
                    parent, node = q.popleft()
                    for nei in adj[node]:
                        if nei != parent:
                            q.append((node, nei))
                    res += 1
                cur_level += 1
            return res

        def build(edges: list[list[int]], k: int) -> list[int]:
            n = len(edges) + 1
            children = [[] for _ in range(n)]
            for u, v in edges:
                children[u].append(v)
                children[v].append(u)
            return [bfs(node, children, k) for node in range(n)]

        hopes1 = build(edges1, k)
        hopes2 = build(edges2, k - 1)
        max_hopes2 = max(hopes2)
        return [h + max_hopes2 for h in hopes1]


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_maxTargetNodes1(self):
        e1 = [[0, 1], [0, 2], [2, 3], [2, 4]]
        e2 = [[0, 1], [0, 2], [0, 3], [2, 7], [1, 4], [4, 5], [4, 6]]
        k = 2
        expected = [9, 7, 9, 8, 8]
        self.assertEqual(expected, self.sol.maxTargetNodes(e1, e2, k))

    def test_maxTargetNodes2(self):
        e1 = [[0, 1], [0, 2], [0, 3], [0, 4]]
        e2 = [[0, 1], [1, 2], [2, 3]]
        k = 1
        expected = [6, 3, 3, 3, 3]
        self.assertEqual(expected, self.sol.maxTargetNodes(e1, e2, k))


if __name__ == '__main__':
    unittest.main()
