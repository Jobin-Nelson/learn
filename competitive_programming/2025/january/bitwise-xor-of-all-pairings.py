"""
Created Date: 2025-01-16
Qn: You are given two 0-indexed arrays, nums1 and nums2, consisting of
    non-negative integers. There exists another array, nums3, which contains
    the bitwise XOR of all pairings of integers between nums1 and nums2 (every
    integer in nums1 is paired with every integer in nums2 exactly once).

    Return the bitwise XOR of all integers in nums3.
Link: https://leetcode.com/problems/bitwise-xor-of-all-pairings/
Notes:
"""

import unittest
from itertools import product, starmap
from functools import reduce
from operator import xor


class Solution:
    def xorAllNums(self, nums1: list[int], nums2: list[int]) -> int:
        # space optimized
        xor1 = reduce(xor, nums1) if len(nums2) & 1 else 0
        xor2 = reduce(xor, nums2) if len(nums1) & 1 else 0
        return xor1 ^ xor2

        # brute force
        # return reduce(xor, starmap(xor, product(nums1, nums2)))


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_xorAllNums1(self):
        n1, n2 = [2, 1, 3], [10, 2, 5, 0]
        expected = 13
        self.assertEqual(expected, self.sol.xorAllNums(n1, n2))

    def test_xorAllNums2(self):
        n1, n2 = [1, 2], [3, 4]
        expected = 0
        self.assertEqual(expected, self.sol.xorAllNums(n1, n2))


if __name__ == '__main__':
    unittest.main()
