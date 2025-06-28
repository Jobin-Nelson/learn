"""
Created Date: 2025-06-24
Qn: You are given a 0-indexed integer array nums and two integers key and k. A
    k-distant index is an index i of nums for which there exists at least one
    index j such that |i - j| <= k and nums[j] == key.

    Return a list of all k-distant indices sorted in increasing order.
Link: https://leetcode.com/problems/find-all-k-distant-indices-in-an-array/
Notes:
    - get all indices of keys
    - return i-k to i+k for each key
"""

import unittest


class Solution:
    def findKDistantIndices(self, nums: list[int], key: int, k: int) -> list[int]:
        keys = [i for i, n in enumerate(nums) if n == key]
        res = {j for i in keys for j in range(i - k, i + k + 1) if 0 <= j < len(nums)}
        return list(res)


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_findKDistantIndices1(self):
        n = [3, 4, 9, 1, 3, 9, 5]
        key, k = 9, 1
        expected = list(range(1, 7))
        self.assertEqual(expected, self.sol.findKDistantIndices(n, key, k))

    def test_findKDistantIndices2(self):
        n = [2, 2, 2, 2, 2]
        key, k = 2, 2
        expected = list(range(0, 5))
        self.assertEqual(expected, self.sol.findKDistantIndices(n, key, k))


if __name__ == '__main__':
    unittest.main()
