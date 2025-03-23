"""
Created Date: 2025-03-18
Qn: You are given an array nums consisting of positive integers.

    We call a subarray of nums nice if the bitwise AND of every pair of
    elements that are in different positions in the subarray is equal to 0.

    Return the length of the longest nice subarray.

    A subarray is a contiguous part of an array.

    Note that subarrays of length 1 are always considered nice.
Link: https://leetcode.com/problems/longest-nice-subarray/
Notes:
    - keep track of used bits
    - use xor when there is a common bit
"""

import unittest


class Solution:
    def longestNicestSubarray(self, nums: list[int]) -> int:
        l = 0
        cur = nums[l]
        res = 1
        for r in range(1, len(nums)):
            while cur & nums[r] != 0:
                cur ^= nums[l]
                l += 1
            cur |= nums[r]
            res = max(res, r - l + 1)
        return res


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_longestNicestSubarray1(self):
        n = [1, 3, 8, 48, 10]
        expected = 3
        self.assertEqual(expected, self.sol.longestNicestSubarray(n))

    def test_longestNicestSubarray2(self):
        n = [3, 1, 5, 11, 13]
        expected = 1
        self.assertEqual(expected, self.sol.longestNicestSubarray(n))

    def test_longestNicestSubarray3(self):
        n = [
            744437702,
            379056602,
            145555074,
            392756761,
            560864007,
            934981918,
            113312475,
            1090,
            16384,
            33,
            217313281,
            117883195,
            978927664,
        ]
        expected = 3
        self.assertEqual(expected, self.sol.longestNicestSubarray(n))


if __name__ == '__main__':
    unittest.main()
