"""
Created Date: 2026-02-03
Qn: You are given an integer array nums of length n.

    An array is trionic if there exist indices 0 < p < q < n − 1 such that:

        - nums[0...p] is strictly increasing,
        - nums[p...q] is strictly decreasing,
        - nums[q...n − 1] is strictly increasing.

    Return true if nums is trionic, otherwise return false.
Link: https://leetcode.com/problems/trionic-array-i/
Notes:
"""

import unittest


class Solution:
    def isTrionic(self, nums: list[int]) -> bool:
        if nums[0] >= nums[1]:
            return False
        count = 1
        for i in range(2, len(nums)):
            n1, n2, n3 = nums[i-2], nums[i-1], nums[i]
            if n2 == n3:
                return False
            if (n1 - n2) * (n2 - n3) < 0:
                count += 1
        return count == 3


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test1(self):
        n = [1, 3, 5, 4, 2, 6]
        expected = True
        self.assertEqual(expected, self.sol.isTrionic(n))

    def test2(self):
        n = [2, 1, 3]
        expected = False
        self.assertEqual(expected, self.sol.isTrionic(n))

    def test3(self):
        n = [4,1,5,2,3]
        expected = False
        self.assertEqual(expected, self.sol.isTrionic(n))


if __name__ == '__main__':
    unittest.main()
