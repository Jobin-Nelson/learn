"""
Created Date: 2026-02-07
Qn: You are given a string s consisting only of characters 'a' and
    'b'

    You can delete any number of characters in s to make s balanced. s is
    balanced if there is no pair of indices (i,j) such that i < j and s[i] =
    'b' and s[j]= 'a'.

    Return the minimum number of deletions needed to make s balanced.
Link: https://leetcode.com/problems/minimum-deletions-to-make-string-balanced/
Notes:
"""

import unittest


class Solution:
    def minimumDeletions(self, s: str) -> int:
        n = len(s)
        min_deletions = 0
        b_count = 0

        for i in range(n):
            if s[i] == 'b':
                b_count += 1
            else:
                min_deletions = min(min_deletions + 1, b_count)
        return min_deletions


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test1(self):
        s = "aababbab"
        expected = 2
        self.assertEqual(expected, self.sol.minimumDeletions(s))

    def test2(self):
        s = "bbaaaaabb"
        expected = 2
        self.assertEqual(expected, self.sol.minimumDeletions(s))

    def test3(self):
        s = "a"
        expected = 0
        self.assertEqual(expected, self.sol.minimumDeletions(s))


if __name__ == '__main__':
    unittest.main()
