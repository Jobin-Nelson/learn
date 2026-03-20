"""
Created Date: 2026-03-06
Qn: Given a binary string s without leading zeros, return true if s contains at
    most one contiguous segment of ones. Otherwise, return false.
Link: https://leetcode.com/problems/check-if-binary-string-has-at-most-one-segment-of-ones/
Notes:
"""

import unittest


class Solution:
    def checkOneSegment(self, s: str) -> bool:
        return '01' not in s


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test1(self):
        s = "1001"
        expected = False
        self.assertEqual(expected, self.sol.checkOneSegment(s))

    def test2(self):
        s = "110"
        expected = True
        self.assertEqual(expected, self.sol.checkOneSegment(s))


if __name__ == '__main__':
    unittest.main()
