"""
Created Date: 2025-04-17
Qn: Given a 0-indexed integer array nums of length n and an integer k, return
    the number of pairs (i, j) where 0 <= i < j < n, such that nums[i] ==
    nums[j] and (i * j) is divisible by k.
Link: https://leetcode.com/problems/count-equal-and-divisible-pairs-in-an-array/
Notes:
    - iterate twice over the loop
"""

import unittest


class Solution:
    def countPairs(self, nums: list[int], k: int) -> int:
        res = 0

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if i * j % k == 0 and nums[i] == nums[j]:
                     res += 1
        return res


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_countPairs1(self):
        n, k = [3, 1, 2, 2, 2, 1, 3], 2
        expected = 4
        self.assertEqual(expected, self.sol.countPairs(n, k))

    def test_countPairs2(self):
        n, k = [1, 2, 3, 4], 1
        expected = 0
        self.assertEqual(expected, self.sol.countPairs(n, k))


if __name__ == '__main__':
    unittest.main()
