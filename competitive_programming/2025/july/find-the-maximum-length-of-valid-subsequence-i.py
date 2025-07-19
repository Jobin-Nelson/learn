"""
Created Date: 2025-07-16
Qn: You are given an integer array nums. A subsequence sub of nums with length
    x is called valid if it satisfies:

    - (sub[0] + sub[1]) % 2 == (sub[1] + sub[2]) % 2 == ... == (sub[x - 2] +
      sub[x - 1]) % 2.

    Return the length of the longest valid subsequence of nums.

    A subsequence is an array that can be derived from another array by
    deleting some or no elements without changing the order of the remaining
    elements.
Link: https://leetcode.com/problems/find-the-maximum-length-of-valid-subsequence-i/
Notes:
"""

import unittest


class Solution:
    def maximumLength(self, nums: list[int]) -> int:
        res = 0
        for pattern in ((0, 0), (0, 1), (1, 0), (1, 1)):
            count = 0
            for n in nums:
                if n & 1 == pattern[count & 1]:
                    count += 1
            res = max(res, count)
        return res


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_maximumLength1(self):
        n = list(range(1, 5))
        expected = 4
        self.assertEqual(expected, self.sol.maximumLength(n))

    def test_maximumLength2(self):
        n = [1, 2, 1, 1, 2, 1, 2]
        expected = 6
        self.assertEqual(expected, self.sol.maximumLength(n))

    def test_maximumLength3(self):
        n = [1, 3]
        expected = 2
        self.assertEqual(expected, self.sol.maximumLength(n))


if __name__ == '__main__':
    unittest.main()
