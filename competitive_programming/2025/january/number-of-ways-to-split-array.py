"""
Created Date: 2025-01-03
Qn: You are given a 0-indexed integer array nums of length n.

    nums contains a valid split at index i if the following are true:

    - The sum of the first i + 1 elements is greater than or equal to the sum
      of the last n - i - 1 elements.
    - There is at least one element to the right of i. That is, 0 <= i < n - 1.

    Return the number of valid splits in nums.
Link: https://leetcode.com/problems/number-of-ways-to-split-array/
Notes:
    - use prefix sums
"""

import unittest
from itertools import accumulate


class Solution:
    def waysToSplitArray(self, nums: list[int]) -> int:
        # Functional approach
        total_sum = sum(nums)
        return sum(1 for n in accumulate(nums[:-1]) if n >= total_sum - n)

        # Imperative approach
        # left_sum = 0
        # right_sum = sum(nums)
        # res = 0
        # for n in nums[:-1]:
        #     left_sum += n
        #     right_sum -= n
        #     if left_sum >= right_sum:
        #         res += 1
        # return res


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_waysToSplitArray1(self):
        n = [10, 4, -8, 7]
        expected = 2
        self.assertEqual(expected, self.sol.waysToSplitArray(n))

    def test_waysToSplitArray2(self):
        n = [2, 3, 1, 0]
        expected = 2
        self.assertEqual(expected, self.sol.waysToSplitArray(n))


if __name__ == '__main__':
    unittest.main()
