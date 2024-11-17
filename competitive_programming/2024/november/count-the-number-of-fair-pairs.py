"""
Created Date: 2024-11-13
Qn: Given a 0-indexed integer array nums of size n and two integers lower and
    upper, return the number of fair pairs.

    A pair (i, j) is fair if:

    - 0 <= i < j < n, and
    - lower <= nums[i] + nums[j] <= upper
Link: https://leetcode.com/problems/count-the-number-of-fair-pairs/
Notes:
    - use sort and binary search
"""

import unittest


class Solution:
    def countFairPairs(self, nums: list[int], lower: int, upper: int) -> int:
        nums.sort()

        def binary_search(l: int, r: int, target: int) -> int:
            while l <= r:
                m = l + ((r - l) >> 1)
                if nums[m] < target:
                    l = m + 1
                else:
                    r = m - 1
            return r

        res = 0
        N = len(nums)
        for i in range(N):
            low = lower - nums[i]
            up = upper - nums[i]
            res += binary_search(i + 1, N - 1, up + 1) - binary_search(
                i + 1, N - 1, low
            )
        return res


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_countFairPairs1(self):
        n = [0, 1, 7, 4, 4, 5]
        lower = 3
        upper = 6
        self.assertEqual(self.sol.countFairPairs(n, lower, upper), 6)

    def test_countFairPairs2(self):
        n = [1, 7, 9, 2, 5]
        lower = 11
        upper = 11
        self.assertEqual(self.sol.countFairPairs(n, lower, upper), 1)


if __name__ == '__main__':
    unittest.main()
