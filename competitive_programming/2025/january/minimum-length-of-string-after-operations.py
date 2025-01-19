"""
Created Date: 2025-01-13
Qn: You are given a string s.

    You can perform the following process on s any number of times:

    - Choose an index i in the string such that there is at least one character
      to the left of index i that is equal to s[i], and at least one character
      to the right that is also equal to s[i].
    - Delete the closest character to the left of index i that is equal to
      s[i].
    - Delete the closest character to the right of index i that is equal to
      s[i].

    Return the minimum length of the final string s that you can achieve.
Link: https://leetcode.com/problems/minimum-length-of-string-after-operations/
Notes:
    - add 1 if odd and 2 if even
"""

import unittest
from collections import Counter


class Solution:
    def minimumLength(self, s: str) -> int:
        return sum(1 if v & 1 else 2 for v in Counter(s).values())


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_minimumLength1(self):
        s = "abaacbcbb"
        expected = 5
        self.assertEqual(expected, self.sol.minimumLength(s))

    def test_minimumLength2(self):
        s = "aa"
        expected = 2
        self.assertEqual(expected, self.sol.minimumLength(s))

    def test_minimumLength3(self):
        s = "lyqkwhyy"
        expected = 6
        self.assertEqual(expected, self.sol.minimumLength(s))


if __name__ == '__main__':
    unittest.main()
