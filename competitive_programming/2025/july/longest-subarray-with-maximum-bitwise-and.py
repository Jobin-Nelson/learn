"""
Created Date: 2025-07-30
Qn: You are given an integer array nums of size n.

    Consider a non-empty subarray from nums that has the maximum possible
    bitwise AND.

    In other words, let k be the maximum value of the bitwise AND of any
    subarray of nums. Then, only subarrays with a bitwise AND equal to k should
    be considered. Return the length of the longest such subarray.

    The bitwise AND of an array is the bitwise AND of all the numbers in it.

    A subarray is a contiguous sequence of elements within an array.
Link: https://leetcode.com/problems/longest-subarray-with-maximum-bitwise-and/
Notes:
"""

import unittest
from itertools import groupby


class Solution:
    def longestSubarray(self, nums: list[int]) -> int:
        # Functional approach
        max_value = max(nums)
        return max(len(list(g)) for n, g in groupby(nums) if n == max_value)

        # Imperative approach
        # max_value = nums[0]
        # cur_value_count = 0
        # max_value_count = 0
        # for n in nums:
        #     if n > max_value:
        #         max_value = n
        #         cur_value_count = 1
        #         max_value_count = cur_value_count
        #     elif n == max_value:
        #         cur_value_count += 1
        #     else:
        #         cur_value_count = 0
        #     max_value_count = max(max_value_count, cur_value_count)
        # return max_value_count


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_longestSubarray1(self):
        n = [1, 2, 3, 3, 2, 2]
        expected = 2
        self.assertEqual(expected, self.sol.longestSubarray(n))

    def test_longestSubarray2(self):
        n = [1, 2, 3, 4]
        expected = 1
        self.assertEqual(expected, self.sol.longestSubarray(n))

    def test_longestSubarray3(self):
        n = [
            311155,
            311155,
            311155,
            311155,
            311155,
            311155,
            311155,
            311155,
            201191,
            311155,
        ]
        expected = 8
        self.assertEqual(expected, self.sol.longestSubarray(n))

    def test_longestSubarray4(self):
        n = [96317, 96317, 96317, 96317, 96317, 96317, 96317, 96317, 96317, 279979]
        expected = 1
        self.assertEqual(expected, self.sol.longestSubarray(n))


if __name__ == '__main__':
    unittest.main()
