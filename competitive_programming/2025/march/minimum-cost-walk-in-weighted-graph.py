"""
Created Date: 2025-03-20
Qn: There is an undirected weighted graph with n vertices labeled from 0 to n -
    1.

    You are given the integer n and an array edges, where edges[i] = [ui, vi,
    wi] indicates that there is an edge between vertices ui and vi with a
    weight of wi.

    A walk on a graph is a sequence of vertices and edges. The walk starts and
    ends with a vertex, and each edge connects the vertex that comes before it
    and the vertex that comes after it. It's important to note that a walk may
    visit the same edge or vertex more than once.

    The cost of a walk starting at node u and ending at node v is defined as
    the bitwise AND of the weights of the edges traversed during the walk. In
    other words, if the sequence of edge weights encountered during the walk is
    w0, w1, w2, ..., wk, then the cost is calculated as w0 & w1 & w2 & ... &
    wk, where & denotes the bitwise AND operator.

    You are also given a 2D array query, where query[i] = [si, ti]. For each
    query, you need to find the minimum cost of the walk starting at vertex si
    and ending at vertex ti. If there exists no such walk, the answer is -1.

    Return the array answer, where answer[i] denotes the minimum cost of a walk
    for query i.
Link: https://leetcode.com/problems/minimum-cost-walk-in-weighted-graph/
Notes:
    - use union find
    - walk all paths since we and every weight reduces the weight
"""

import unittest


class UnionFind:
    def __init__(self, n: int) -> None:
        self.parent = list(range(n))
        self.rank = [1] * n

    def find(self, x: int) -> int:
        while x != self.parent[x]:
            x = self.parent[self.parent[x]]
        return x

    def union(self, x: int, y: int) -> None:
        r1, r2 = self.find(x), self.find(y)
        if self.rank[r2] > self.rank[r1]:
            r1, r2 = r2, r1
        self.parent[r2] = r1
        self.rank[r1] += self.rank[r2]


class Solution:
    def minimumCost(
        self, n: int, edges: list[list[int]], query: list[list[int]]
    ) -> list[int]:
        uf = UnionFind(n)
        for u, v, w in edges:
            uf.union(u, v)

        component_cost = {}
        for u, v, w in edges:
            root = uf.find(u)
            if root not in component_cost:
                component_cost[root] = w
            else:
                component_cost[root] &= w

        res = []
        for s, e in query:
            r1, r2 = uf.find(s), uf.find(e)
            if r1 != r2:
                res.append(-1)
            else:
                res.append(component_cost[r1])
        return res


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_minimumCost1(self):
        n = 5
        e = [[0, 1, 7], [1, 3, 7], [1, 2, 1]]
        q = [[0, 3], [3, 4]]
        expected = [1, -1]
        self.assertEqual(expected, self.sol.minimumCost(n, e, q))

    def test_minimumCost2(self):
        n = 3
        e = [[0, 2, 7], [0, 1, 15], [1, 2, 6], [1, 2, 1]]
        q = [[1, 2]]
        expected = [0]
        self.assertEqual(expected, self.sol.minimumCost(n, e, q))


if __name__ == '__main__':
    unittest.main()
