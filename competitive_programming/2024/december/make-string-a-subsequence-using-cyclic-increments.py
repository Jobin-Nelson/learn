"""
Created Date: 2024-12-04
Qn: You are given two 0-indexed strings str1 and str2.

    In an operation, you select a set of indices in str1, and for each index i
    in the set, increment str1[i] to the next character cyclically. That is 'a'
    becomes 'b', 'b' becomes 'c', and so on, and 'z' becomes 'a'.

    Return true if it is possible to make str2 a subsequence of str1 by
    performing the operation at most once, and false otherwise.

    Note: A subsequence of a string is a new string that is formed from the
    original string by deleting some (possibly none) of the characters without
    disturbing the relative positions of the remaining characters.
Link: https://leetcode.com/problems/make-string-a-subsequence-using-cyclic-increments/
Notes:
"""

import unittest
from functools import reduce


class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        # Functional approach
        ord_a = ord('a')
        str2_len = len(str2)

        def char2num(c: str) -> int:
            return ord(c) - ord_a

        return (
            reduce(
                lambda i2, d: i2 + 1
                if not i2 == str2_len
                and (0 <= char2num(str2[i2]) - d < 2 or d - char2num(str2[i2]) == 25)
                else i2,
                map(char2num, str1),
                0,
            )
            == str2_len
        )

        # Imperative approach
        # ord_a = ord('a')
        #
        # def char2num(c: str) -> int:
        #     return ord(c) - ord_a
        #
        # s2 = map(char2num, str2)
        # d2 = next(s2)
        # for d1 in map(char2num, str1):
        #     if 0 <= d2 - d1 < 2 or d1 - d2 == 25:
        #         try:
        #             d2 = next(s2)
        #         except StopIteration:
        #             return True
        # return False


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_canMakeSubsequence1(self):
        str1, str2 = "abc", "ad"
        expected = True
        self.assertEqual(expected, self.sol.canMakeSubsequence(str1, str2))

    def test_canMakeSubsequence2(self):
        str1, str2 = "zc", "ad"
        expected = True
        self.assertEqual(expected, self.sol.canMakeSubsequence(str1, str2))

    def test_canMakeSubsequence3(self):
        str1, str2 = "ab", "d"
        expected = False
        self.assertEqual(expected, self.sol.canMakeSubsequence(str1, str2))

    def test_canMakeSubsequence4(self):
        str1, str2 = "c", "b"
        expected = False
        self.assertEqual(expected, self.sol.canMakeSubsequence(str1, str2))

    def test_canMakeSubsequence5(self):
        str1, str2 = "dm", "e"
        expected = True
        self.assertEqual(expected, self.sol.canMakeSubsequence(str1, str2))


if __name__ == '__main__':
    unittest.main()
