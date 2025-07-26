"""
Created Date: 2025-07-25
Qn: You are given an integer array nums.

    You are allowed to delete any number of elements from nums without making
    it empty. After performing the deletions, select a subarray of nums such
    that:

    1. All elements in the subarray are unique.
    2. The sum of the elements in the subarray is maximized.

    Return the maximum sum of such a subarray.
Link: https://leetcode.com/problems/maximum-unique-subarray-sum-after-deletion/
Notes:
    - if max is less than zero return max
    - return unique sum if not negative
"""

import unittest


class Solution:
    def maxSum(self, nums: list[int]) -> int:
        return max(nums) if max(nums) < 0 else sum(set(n for n in nums if n > 0))


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_maxSum1(self):
        n = list(range(1, 6))
        expected = 15
        self.assertEqual(expected, self.sol.maxSum(n))

    def test_maxSum2(self):
        n = [1, 1, 0, 1, 1]
        expected = 1
        self.assertEqual(expected, self.sol.maxSum(n))

    def test_maxSum3(self):
        n = [1, 2, -1, -2, 1, 0, -1]
        expected = 3
        self.assertEqual(expected, self.sol.maxSum(n))


if __name__ == '__main__':
    unittest.main()
