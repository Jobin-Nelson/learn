"""
Created Date: 2026-02-10
Qn: You are given an integer array nums.

    A is called balanced if the number of distinct even numbers in the subarray
    is equal to the number of distinct odd numbers.

    Return the length of the longest balanced subarray.
Link: https://leetcode.com/problems/longest-balanced-subarray-i/
Notes:
"""

import unittest


class Solution:
    def longestBalanced(self, nums: list[int]) -> int:
        n = len(nums)
        res = 0
        for i in range(n):
            even, odd = {}, {}
            for j in range(i, n):
                num = nums[j]
                if num & 1:
                    odd[num] = odd.get(num, 0) + 1
                else:
                    even[num] = even.get(num, 0) + 1
                if len(odd) == len(even):
                    res = max(res, j - i + 1)
        return res


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test1(self):
        n = [2, 5, 4, 3]
        expected = 4
        self.assertEqual(expected, self.sol.longestBalanced(n))

    def test2(self):
        n = [3, 2, 2, 5, 4]
        expected = 5
        self.assertEqual(expected, self.sol.longestBalanced(n))

    def test3(self):
        n = [1, 2, 3, 2]
        expected = 3
        self.assertEqual(expected, self.sol.longestBalanced(n))


if __name__ == '__main__':
    unittest.main()
