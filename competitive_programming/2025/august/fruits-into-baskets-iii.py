"""
Created Date: 2025-08-06
Qn: You are given two arrays of integers, fruits and baskets, each of length n,
    where fruits[i] represents the quantity of the ith type of fruit, and
    baskets[j] represents the capacity of the jth basket.

    From left to right, place the fruits according to these rules:

    - Each fruit type must be placed in the leftmost available basket with a
      capacity greater than or equal to the quantity of that fruit type.
    - Each basket can hold only one type of fruit.
    - If a fruit type cannot be placed in any basket, it remains unplaced.

    Return the number of fruit types that remain unplaced after all possible
    allocations are made.
Link: https://leetcode.com/problems/fruits-into-baskets-iii/
Notes:
"""

import unittest


class SegTree:
    def __init__(self, baskets: list[int]):
        self.n = len(baskets)
        size = 2 << (self.n - 1).bit_length()
        self.seg = [0] * size
        self._build(baskets, 1, 0, self.n - 1)

    def _maintain(self, o: int):
        self.seg[o] = max(self.seg[o * 2], self.seg[o * 2 + 1])

    def _build(self, a: list[int], o: int, l: int, r: int):
        if l == r:
            self.seg[o] = a[l]
            return
        m = (l + r) // 2
        self._build(a, o * 2, l, m)
        self._build(a, o * 2 + 1, m + 1, r)
        self._maintain(o)

    def find_first_and_update(self, o: int, l: int, r: int, x: int) -> int:
        if self.seg[o] < x:
            return -1
        if l == r:
            self.seg[o] = -1
            return l
        m = (l + r) // 2
        i = self.find_first_and_update(o * 2, l, m, x)
        if i == -1:
            i = self.find_first_and_update(o * 2 + 1, m + 1, r, x)
        self._maintain(o)
        return i


class Solution:
    def numOfUnplacedFruits(self, fruits: list[int], baskets: list[int]) -> int:
        segtree = SegTree(baskets)
        m = len(baskets)
        unplaced = 0
        for fruit in fruits:
            if segtree.find_first_and_update(1, 0, m - 1, fruit) == -1:
                unplaced += 1
        return unplaced


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_numOfUnplacedFruits1(self):
        f = [4, 2, 5]
        b = [3, 5, 4]
        expected = 1
        self.assertEqual(expected, self.sol.numOfUnplacedFruits(f, b))

    def test_numOfUnplacedFruits2(self):
        f = [3, 6, 1]
        b = [6, 4, 7]
        expected = 0
        self.assertEqual(expected, self.sol.numOfUnplacedFruits(f, b))


if __name__ == '__main__':
    unittest.main()
