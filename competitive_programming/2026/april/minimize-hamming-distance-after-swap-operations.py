"""
Created Date: 2026-04-21
Qn: You are given two integer arrays, source and target, both of length n. You
    are also given an array allowedSwaps where each allowedSwaps[i] = [ai, bi]
    indicates that you are allowed to swap the elements at index ai and index
    bi (0-indexed) of array source. Note that you can swap elements at a
    specific pair of indices multiple times and in any order.

    The Hamming distance of two arrays of the same length, source and target,
    is the number of positions where the elements are different. Formally, it
    is the number of indices i for 0 <= i <= n-1 where source[i] != target[i]
    (0-indexed).

    Return the minimum Hamming distance of source and target after performing
    any amount of swap operations on array source.
Link: https://leetcode.com/problems/minimize-hamming-distance-after-swap-operations/
Notes:
"""

import unittest
from collections import defaultdict


class UnionFind:
    def __init__(self, n: int):
        self.fa = list(range(n))
        self.rank = [0] * n

    def find(self, x: int) -> int:
        if self.fa[x] != x:
            self.fa[x] = self.find(self.fa[x])
        return self.fa[x]

    def union(self, x: int, y: int) -> None:
        x, y = self.find(x), self.find(y)
        if x == y:
            return
        if self.rank[x] < self.rank[y]:
            x, y = y, x

        self.fa[y] = x
        if self.rank[x] == self.rank[y]:
            self.rank[x] += 1


class Solution:
    def minimumHammingDistance(
        self, source: list[int], target: list[int], allowedSwaps: list[list[int]]
    ) -> int:
        n = len(source)
        uf = UnionFind(n)
        for a, b in allowedSwaps:
            uf.union(a, b)

        sets = defaultdict(lambda: defaultdict(int))
        for i in range(n):
            f = uf.find(i)
            sets[f][source[i]] += 1

        res = 0
        for i in range(n):
            f = uf.find(i)
            if sets[f][target[i]] > 0:
                sets[f][target[i]] -= 1
            else:
                res += 1
        return res


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test1(self):
        s, t = [1, 2, 3, 4], [2, 1, 4, 5]
        a = [[0, 1], [2, 3]]
        expected = 1
        self.assertEqual(expected, self.sol.minimumHammingDistance(s, t, a))

    def test2(self):
        s, t = [5, 1, 2, 4, 3], [1, 5, 4, 2, 3]
        a = [[0, 4], [4, 2], [1, 3], [1, 4]]
        expected = 0
        self.assertEqual(expected, self.sol.minimumHammingDistance(s, t, a))


if __name__ == '__main__':
    unittest.main()
