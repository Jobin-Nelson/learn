"""
Created Date: 2025-10-18
Qn: You are given an integer array nums and an integer k.

    You are allowed to perform the following operation on each element of the
    array at most once:

    Add an integer in the range [-k, k] to the element. Return the maximum
    possible number of distinct elements in nums after performing the
    operations.
Link: https://leetcode.com/problems/maximum-number-of-distinct-elements-after-operations/
Notes:
"""

import math
import unittest


class Solution:
    def maxDistinctElements(self, nums: list[int], k: int) -> int:
        nums.sort()
        prev = -math.inf
        res = 0

        for n in nums:
            cur = min(max(n - k, prev + 1), n + k)
            if cur > prev:
                res += 1
                prev = cur
        return res


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test1(self):
        n, k = [1, 2, 2, 3, 3, 4], 2
        expected = 6
        self.assertEqual(expected, self.sol.maxDistinctElements(n, k))

    def test2(self):
        n, k = [4, 4, 4, 4], 1
        expected = 3
        self.assertEqual(expected, self.sol.maxDistinctElements(n, k))


if __name__ == '__main__':
    unittest.main()
