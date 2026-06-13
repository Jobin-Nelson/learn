"""
Created Date: 2026-04-23
Qn: You are given a 0-indexed integer array nums. There exists an array arr of
    length nums.length, where arr[i] is the sum of |i - j| over all j such that
    nums[j] == nums[i] and j != i. If there is no such j, set arr[i] to be 0.

    Return the array arr.
Link: https://leetcode.com/problems/sum-of-distances/
Notes:
    - prefix sum
"""

import unittest
from collections import defaultdict


class Solution:
    def distance(self, nums: list[int]) -> list[int]:
        res = [0] * len(nums)
        sum_left = defaultdict(int)
        count_left = defaultdict(int)
        for i, n in enumerate(nums):
            res[i] += count_left[n] * i
            res[i] -= sum_left[n]

            count_left[n] += 1
            sum_left[n] += i

        sum_right = defaultdict(int)
        count_right = defaultdict(int)
        for i, n in reversed(list(enumerate(nums))):
            res[i] += sum_right[n]
            res[i] -= count_right[n] * i

            count_right[n] += 1
            sum_right[n] += i

        return res


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test1(self):
        n = [1, 3, 1, 1, 2]
        expected = [5, 0, 3, 4, 0]
        self.assertEqual(expected, self.sol.distance(n))

    def test2(self):
        n = [0, 5, 3]
        expected = [0, 0, 0]
        self.assertEqual(expected, self.sol.distance(n))


if __name__ == '__main__':
    unittest.main()
