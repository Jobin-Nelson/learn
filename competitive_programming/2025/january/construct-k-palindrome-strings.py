"""
Created Date: 2025-01-11
Qn: Given a string s and an integer k, return true if you can use all the
    characters in s to construct k palindrome strings or false otherwise.
Link: https://leetcode.com/problems/construct-k-palindrome-strings/
Notes:
"""

import unittest
from collections import Counter


class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        return k <= len(s) and sum(1 for v in Counter(s).values() if v & 1) <= k


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_canConstruct1(self):
        s = "annabelle"
        k = 2
        expected = True
        self.assertEqual(expected, self.sol.canConstruct(s, k))

    def test_canConstruct2(self):
        s = "leetcode"
        k = 3
        expected = False
        self.assertEqual(expected, self.sol.canConstruct(s, k))


if __name__ == '__main__':
    unittest.main()
