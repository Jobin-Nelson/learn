"""
Created Date: 2025-01-29
Qn: In this problem, a tree is an undirected graph that is connected and has no
    cycles.

    You are given a graph that started as a tree with n nodes labeled from 1 to
    n, with one additional edge added. The added edge has two different
    vertices chosen from 1 to n, and was not an edge that already existed. The
    graph is represented as an array edges of length n where edges[i] = [ai,
    bi] indicates that there is an edge between nodes ai and bi in the graph.

    Return an edge that can be removed so that the resulting graph is a tree of
    n nodes. If there are multiple answers, return the answer that occurs last
    in the input.
Link: https://leetcode.com/problems/redundant-connection/
Notes:
    - use union find and return the first edge that cannot be unioned
"""

import unittest

class UnionFind:
    def __init__(self, n: int) -> None:
        self.parents = list(range(n))
        self.ranks = [1] * n

    def find(self, x: int) -> int:
        while self.parents[x] != x:
            self.parents[x] = self.parents[self.parents[x]]
            x = self.parents[x]
        return x

    def union(self, x: int, y: int) -> bool:
        px, py = self.find(x), self.find(y)
        if px == py:
            return False
        if self.ranks[py] > self.ranks[px]:
            px, py = py, px
        self.parents[py] = px
        self.ranks[px] += self.ranks[py]
        return True


class Solution:
    def findRedundantConnection(self, edges: list[list[int]]) -> list[int]:
        uf = UnionFind(len(edges))
        
        for u, v in edges:
            if not uf.union(u-1, v-1):
                return [u, v]
        return []


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_findRedundantConnection1(self):
        e = [[1, 2], [1, 3], [2, 3]]
        expected = [2, 3]
        self.assertEqual(expected, self.sol.findRedundantConnection(e))

    def test_findRedundantConnection2(self):
        e = [[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]]
        expected = [1, 4]
        self.assertEqual(expected, self.sol.findRedundantConnection(e))


if __name__ == '__main__':
    unittest.main()
