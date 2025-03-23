"""
Created Date: 2025-03-22
Qn: You are given an integer n. There is an undirected graph with n vertices,
    numbered from 0 to n - 1. You are given a 2D integer array edges where
    edges[i] = [ai, bi] denotes that there exists an undirected edge connecting
    vertices ai and bi.

    Return the number of complete connected components of the graph.

    A connected component is a subgraph of a graph in which there exists a path
    between any two vertices, and no vertex of the subgraph shares an edge with
    a vertex outside of the subgraph.

    A connected component is said to be complete if there exists an edge
    between every pair of its vertices.
Link: https://leetcode.com/problems/count-the-number-of-complete-components/
Notes:
    - use union find
"""

import unittest

class UnionFind:
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.rank = [1] * n

    def find(self, x: int) -> int:
        while x != self.parent[x]:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, x: int, y: int):
        px, py = self.find(x), self.find(y)
        if px == py:
            return
        if self.rank[py] > self.rank[px]:
            px, py = py, px
        self.parent[py] = px
        self.rank[px] += self.rank[py]


class Solution:
    def countCompleteComponents(self, n: int, edges: list[list[int]]) -> int:
        uf = UnionFind(n)
        edge_count = [0] * n
        for u, v in edges:
            uf.union(u,v)
        for edge in edges:
            root = uf.find(edge[0])
            edge_count[root] += 1

        complete_count = 0
        for vertex in range(n):
            if uf.find(vertex) == vertex:
                node_count = uf.rank[vertex]
                expected_edges = node_count * (node_count - 1) // 2
                if edge_count[vertex] == expected_edges:
                    complete_count += 1
        return complete_count


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_countCompleteComponents1(self):
        n = 6
        e = [[0, 1], [0, 2], [1, 2], [3, 4]]
        expected = 3
        self.assertEqual(expected, self.sol.countCompleteComponents(n, e))

    def test_countCompleteComponents2(self):
        n = 6
        e = [[0, 1], [0, 2], [1, 2], [3, 4]]
        expected = 3
        self.assertEqual(expected, self.sol.countCompleteComponents(n, e))


if __name__ == '__main__':
    unittest.main()
