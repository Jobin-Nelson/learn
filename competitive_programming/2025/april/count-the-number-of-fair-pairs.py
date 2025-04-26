"""
Created Date: 2025-04-19
Qn: Given a 0-indexed integer array nums of size n and two integers lower and
    upper, return the number of fair pairs.

    A pair (i, j) is fair if:

    - 0 <= i < j < n, and
    - lower <= nums[i] + nums[j] <= upper
Link: https://leetcode.com/problems/count-the-number-of-fair-pairs/
Notes:
    - use binary search
"""

import unittest


class Solution:
    def countFairPairs(self, nums: list[int], lower: int, upper: int) -> int:
        def binary_search(l: int, r: int, target: int) -> int:
            while l <= r:
                m = l + ((r - l) >> 1)
                if nums[m] >= target:
                    r = m - 1
                else:
                    l = m + 1
            return l

        nums.sort()
        n = len(nums)
        res = 0
        for i in range(n):
            low = lower - nums[i]
            up = upper - nums[i]
            res += binary_search(i + 1, n - 1, up + 1) - binary_search(
                i + 1, n - 1, low
            )
        return res


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_countFairPairs1(self):
        n, l, u = [0, 1, 7, 4, 4, 5], 3, 6
        expected = 6
        self.assertEqual(expected, self.sol.countFairPairs(n, l, u))

    def test_countFairPairs2(self):
        n, l, u = [1, 7, 9, 2, 5], 11, 11
        expected = 1
        self.assertEqual(expected, self.sol.countFairPairs(n, l, u))


if __name__ == '__main__':
    unittest.main()
