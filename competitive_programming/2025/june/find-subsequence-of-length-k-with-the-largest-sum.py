"""
Created Date: 2025-06-28
Qn: You are given an integer array nums and an integer k. You want to find a
    subsequence of nums of length k that has the largest sum.

    Return any such subsequence as an integer array of length k.

    A subsequence is an array that can be derived from another array by
    deleting some or no elements without changing the order of the remaining
    elements.
Link: https://leetcode.com/problems/find-subsequence-of-length-k-with-the-largest-sum/
Notes:
    - zip with index
    - sort by num
    - get top k elements
    - sort by index
"""

import unittest


class Solution:
    def maxSubsequence(self, nums: list[int], k: int) -> list[int]:
        return [
            n
            for _, n in sorted(
                sorted(enumerate(nums), key=lambda x: x[1], reverse=True)[:k]
            )
        ]


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_maxSubsequence1(self):
        n, k = [2, 1, 3, 3], 2
        expected = [3, 3]
        self.assertEqual(expected, self.sol.maxSubsequence(n, k))

    def test_maxSubsequence2(self):
        n, k = [-1, -2, 3, 4], 3
        expected = [-1, 3, 4]
        self.assertEqual(expected, self.sol.maxSubsequence(n, k))

    def test_maxSubsequence3(self):
        n, k = [3, 4, 3, 3], 2
        expected = [3, 4]
        self.assertEqual(expected, self.sol.maxSubsequence(n, k))


if __name__ == '__main__':
    unittest.main()
