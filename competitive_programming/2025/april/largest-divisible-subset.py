"""
Created Date: 2025-04-06
Qn: Given a set of distinct positive integers nums, return the largest subset
    answer such that every pair (answer[i], answer[j]) of elements in this
    subset satisfies:

    - answer[i] % answer[j] == 0, or
    - answer[j] % answer[i] == 0

    If there are multiple solutions, return any of them.
Link: https://leetcode.com/problems/largest-divisible-subset/
Notes:
    - use dfs
"""

from functools import cache
import unittest



class Solution:
    def largestDivisibleSubset(self, nums: list[int]) -> list[int]:
        nums.sort()

        @cache
        def dfs(i: int) -> list[int]:
            if i == len(nums):
                return []
            res = [nums[i]]
            for j in range(i + 1, len(nums)):
                if nums[j] % nums[i] == 0:
                    res = max(res, [nums[i]] + dfs(j), key=len)
            return res

        res = []
        for i in range(len(nums)):
            res = max(res, dfs(i), key=len)
        return res


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_largestDivisibleSubset1(self):
        n = [1, 2, 3]
        expected = [1, 2]
        self.assertEqual(expected, self.sol.largestDivisibleSubset(n))

    def test_largestDivisibleSubset2(self):
        n = [1, 2, 3]
        expected = [1, 2]
        self.assertEqual(expected, self.sol.largestDivisibleSubset(n))


if __name__ == '__main__':
    unittest.main()
