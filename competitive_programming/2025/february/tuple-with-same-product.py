"""
Created Date: 2025-02-06
Qn: Given an array nums of distinct positive integers, return the number of
    tuples (a, b, c, d) such that a * b = c * d where a, b, c, and d are
    elements of nums, and a != b != c != d.
Link: https://leetcode.com/problems/tuple-with-same-product/
Notes:
"""

import unittest
from collections import defaultdict


class Solution:
    def tupleSameProduct(self, nums: list[int]) -> int:
        product_count = defaultdict(int)
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                product = nums[i] * nums[j]
                product_count[product] += 1
        return sum(8 * ((c * (c - 1)) // 2) for c in product_count.values())


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_tupleSameProduct1(self):
        n = [2, 3, 4, 6]
        expected = 8
        self.assertEqual(expected, self.sol.tupleSameProduct(n))

    def test_tupleSameProduct2(self):
        n = [1, 2, 4, 5, 10]
        expected = 16
        self.assertEqual(expected, self.sol.tupleSameProduct(n))


if __name__ == '__main__':
    unittest.main()
