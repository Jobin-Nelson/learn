"""
Created Date: 2025-03-17
Qn: You are given an integer array nums consisting of 2 * n integers.

    You need to divide nums into n pairs such that:

    - Each element belongs to exactly one pair.
    - The elements present in a pair are equal.

    Return true if nums can be divided into n pairs, otherwise return false.
Link: https://leetcode.com/problems/divide-array-into-equal-pairs/
Notes:
    - check count of all num is even
"""

import unittest
from collections import Counter


class Solution:
    def divideArray(self, nums: list[int]) -> bool:
        return len(nums) & 1 == 0 and all(v & 1 == 0 for v in Counter(nums).values())


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_divideArray1(self):
        n = [3, 2, 3, 2, 2, 2]
        expected = True
        self.assertEqual(expected, self.sol.divideArray(n))

    def test_divideArray2(self):
        n = list(range(1, 5))
        expected = False
        self.assertEqual(expected, self.sol.divideArray(n))


if __name__ == '__main__':
    unittest.main()
