"""
Created Date: 2025-04-03
Qn: You are given a 0-indexed integer array nums.

    Return the maximum value over all triplets of indices (i, j, k) such that i
    < j < k. If all such triplets have a negative value, return 0.

    The value of a triplet of indices (i, j, k) is equal to (nums[i] - nums[j])
    * nums[k].
Link: https://leetcode.com/problems/maximum-value-of-an-ordered-triplet-ii/
Notes:
"""

import unittest


class Solution:
    def maximumTripletValue(self, nums: list[int]) -> int:
        imax, dmax, res = 0, 0, 0
        for n in nums:
            res = max(res, dmax * n)
            dmax = max(dmax, imax - n)
            imax = max(imax, n)
        return res


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_maximumTripletValue1(self):
        n = [12, 6, 1, 2, 7]
        expected = 77
        self.assertEqual(expected, self.sol.maximumTripletValue(n))

    def test_maximumTripletValue2(self):
        n = [1, 10, 3, 4, 19]
        expected = 133
        self.assertEqual(expected, self.sol.maximumTripletValue(n))

    def test_maximumTripletValue3(self):
        n = [1, 2, 3]
        expected = 0
        self.assertEqual(expected, self.sol.maximumTripletValue(n))


if __name__ == '__main__':
    unittest.main()
