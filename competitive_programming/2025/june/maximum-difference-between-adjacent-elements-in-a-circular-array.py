"""
Created Date: 2025-06-12
Qn: Given a circular array nums, find the maximum absolute difference between
    adjacent elements.

    Note: In a circular array, the first and last elements are adjacent.
Link: https://leetcode.com/problems/maximum-difference-between-adjacent-elements-in-a-circular-array/
Notes:
"""

import unittest
from itertools import cycle, islice, pairwise


class Solution:
    def maxAdjacentDistance(self, nums: list[int]) -> int:
        # Functional
        return max(abs(x - y) for x, y in pairwise(islice(cycle(nums), len(nums) + 1)))
        # Imperative
        # N = len(nums)
        # prev = nums[0]
        # res = 0
        # for i, n in enumerate(cycle(nums)):
        #     if i == N + 1:
        #         break
        #     res = max(res, abs(n - prev))
        #     prev = n
        # return res


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_maxAdjacentDistance1(self):
        n = [1, 2, 4]
        expected = 3
        self.assertEqual(expected, self.sol.maxAdjacentDistance(n))

    def test_maxAdjacentDistance2(self):
        n = [-5, -10, -5]
        expected = 5
        self.assertEqual(expected, self.sol.maxAdjacentDistance(n))


if __name__ == '__main__':
    unittest.main()
