"""
Created Date: 2025-02-03
Qn: You are given an array of integers nums. Return the length of the longest
    subarray of nums which is either strictly increasing or strictly decreasing
Link: https://leetcode.com/problems/longest-strictly-increasing-or-strictly-decreasing-subarray/
Notes:
    - use two variables for counting decreasing and increasing
    - return the max of two
"""

import unittest
from itertools import accumulate, pairwise, starmap


class Solution:
    def longestMonotonicSubarray(self, nums: list[int]) -> int:
        # Functional approach
        def count(acc: tuple[int, int], val: tuple[int, int]) -> tuple[int, int]:
            return (
                acc[0] + 1 if val[0] > val[1] else 1,
                acc[1] + 1 if val[0] < val[1] else 1,
            )

        return max(starmap(max, accumulate(pairwise(nums), count, initial=(1, 1))))

        # Imperative approach
        # dec, inc = 1, 1
        # res = 1
        # for i, n in enumerate(nums[:-1]):
        #     dec = dec + 1 if n > nums[i+1] else 1
        #     inc = inc + 1 if n < nums[i+1] else 1
        #     res = max(res, dec, inc)
        # return res


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_longestMonotonicSubarray1(self):
        n = [1, 4, 3, 3, 2]
        expected = 2
        self.assertEqual(expected, self.sol.longestMonotonicSubarray(n))

    def test_longestMonotonicSubarray2(self):
        n = [3] * 4
        expected = 1
        self.assertEqual(expected, self.sol.longestMonotonicSubarray(n))

    def test_longestMonotonicSubarray3(self):
        n = [3, 2, 1]
        expected = 3
        self.assertEqual(expected, self.sol.longestMonotonicSubarray(n))


if __name__ == '__main__':
    unittest.main()
