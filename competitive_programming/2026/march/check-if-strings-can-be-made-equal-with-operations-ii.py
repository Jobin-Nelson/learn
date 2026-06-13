"""
Created Date: 2026-03-30
Qn: You are given two strings s1 and s2, both of length n, consisting of
    lowercase English letters.

    You can apply the following operation on any of the two strings any number
    of times:

    Choose any two indices i and j such that i < j and the difference j - i is
    even, then swap the two characters at those indices in the string. Return
    true if you can make the strings s1 and s2 equal, and false otherwise.
Link: https://leetcode.com/problems/check-if-strings-can-be-made-equal-with-operations-ii/
Notes:
    - check even and odd letter counts
"""

import unittest


class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        ord_a = ord('a')
        ao, ae = [0] * 26, [0] * 26
        bo, be = [0] * 26, [0] * 26
        for i, c in enumerate(s1):
            if i & 1:
                ao[ord(c) - ord_a] += 1
            else:
                ae[ord(c) - ord_a] += 1

        for i, c in enumerate(s2):
            if i & 1:
                bo[ord(c) - ord_a] += 1
            else:
                be[ord(c) - ord_a] += 1
        return ao == bo and ae == be


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test1(self):
        s1, s2 = "abcdba", 'cabdab'
        expected = True
        self.assertEqual(expected, self.sol.checkStrings(s1, s2))

    def test2(self):
        s1, s2 = 'abe', 'bea'
        expected = False
        self.assertEqual(expected, self.sol.checkStrings(s1, s2))


if __name__ == '__main__':
    unittest.main()
