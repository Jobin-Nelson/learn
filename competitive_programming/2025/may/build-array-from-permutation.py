"""
Created Date: 2025-05-06
Qn: Given a zero-based permutation nums (0-indexed), build an array ans of the
    same length where ans[i] = nums[nums[i]] for each 0 <= i < nums.length and
    return it.

    A zero-based permutation nums is an array of distinct integers from 0 to
    nums.length - 1 (inclusive).
Link: https://leetcode.com/problems/build-array-from-permutation/
Notes:
"""

import unittest


class Solution:
    def buildArray(self, nums: list[int]) -> list[int]:
        return [nums[nums[i]] for i in range(len(nums))]


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_buildArray1(self):
        n = [0,2,1,5,3,4]
        expected = [0,1,2,4,5,3]
        self.assertEqual(expected, self.sol.buildArray(n))

    def test_buildArray2(self):
        n = [5,0,1,2,3,4]
        expected = [4,5,0,1,2,3]
        self.assertEqual(expected, self.sol.buildArray(n))


if __name__ == '__main__':
    unittest.main()
