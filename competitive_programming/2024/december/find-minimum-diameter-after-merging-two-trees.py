"""
Created Date: 2024-12-24
Qn: There exist two undirected trees with n and m nodes, numbered from 0
    to n - 1 and from 0 to m - 1, respectively. You are given two 2D
    integer arrays edges1 and edges2 of lengths n - 1 and m - 1,
    respectively, where edges1[i] = [ai, bi] indicates that there is an
    edge between nodes ai and bi in the first tree and edges2[i] = [ui,
    vi] indicates that there is an edge between nodes ui and vi in the
    second tree.

    You must connect one node from the first tree with another node from
    the second tree with an edge.

    Return the minimum possible diameter of the resulting tree.

    The diameter of a tree is the length of the longest path between any
    two nodes in the tree.
Link: https://leetcode.com/problems/find-minimum-diameter-after-merging-two-trees/
Notes:
    - find diameter from every node and join the half of the max diameter from
      both trees
"""

import unittest
from collections import defaultdict
import math
import heapq


class Solution:
    def minimumDiameterAfterMerge(
        self, edges1: list[list[int]], edges2: list[list[int]]
    ) -> int:
        def build_adj(edges: list[list[int]]) -> dict[int, list[int]]:
            adj = defaultdict(list)

            for u, v in edges:
                adj[u].append(v)
                adj[v].append(u)
            return adj

        def get_diameter(cur: int, par: int, adj: dict[int, list[int]]) -> tuple[int, int]:
            max_d = 0
            max_child_paths = [0, 0]
            for nei in adj[cur]:
                if nei == par: continue
                nei_d, nei_max_leaf_path = get_diameter(nei, cur, adj)
                max_d = max(max_d, nei_d)
                heapq.heappush(max_child_paths, nei_max_leaf_path)
                heapq.heappop(max_child_paths)
            max_d = max(max_d, sum(max_child_paths))
            return (max_d, 1 + max(max_child_paths))

        adj1, adj2 = build_adj(edges1), build_adj(edges2)
        d1, _ = get_diameter(0, -1, adj1)
        d2, _ = get_diameter(0, -1, adj2)
        return max(d1, d2, 1 + math.ceil(d1 / 2) + math.ceil(d2/2))


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_minimumDiameterAfterMerge1(self):
        e1, e2 = [[0, 1], [0, 2], [0, 3]], [[0, 1]]
        expected = 3
        self.assertEqual(expected, self.sol.minimumDiameterAfterMerge(e1, e2))

    def test_minimumDiameterAfterMerge2(self):
        e1, e2 = (
            [[0, 1], [0, 2], [0, 3], [2, 4], [2, 5], [3, 6], [2, 7]],
            [[0, 1], [0, 2], [0, 3], [2, 4], [2, 5], [3, 6], [2, 7]],
        )
        expected = 5
        self.assertEqual(expected, self.sol.minimumDiameterAfterMerge(e1, e2))


if __name__ == '__main__':
    unittest.main()
