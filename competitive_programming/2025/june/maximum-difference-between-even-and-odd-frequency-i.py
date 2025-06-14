"""
Created Date: 2025-06-10
Qn: You are given a string s consisting of lowercase English letters.

    Your task is to find the maximum difference diff = a1 - a2 between the
    frequency of characters a1 and a2 in the string such that:

    - a1 has an odd frequency in the string.
    - a2 has an even frequency in the string.

    Return this maximum difference.
Link: https://leetcode.com/problems/maximum-difference-between-even-and-odd-frequency-i/
Notes:
"""

import unittest


class Solution:
    def maxDifference(self, s: str) -> int:
        ord_a = ord('a')
        freq = [0] * 26
        for c in s:
            freq[ord(c) - ord_a] += 1
        return max(f for f in freq if f & 1 == 1) - min(
            f for f in freq if f & 1 == 0 and f != 0
        )


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_maxDifference1(self):
        s = "aaaaabbc"
        expected = 3
        self.assertEqual(expected, self.sol.maxDifference(s))

    def test_maxDifference2(self):
        s = "abcabcab"
        expected = 1
        self.assertEqual(expected, self.sol.maxDifference(s))

    def test_maxDifference3(self):
        s = "yzyyys"
        expected = -3
        self.assertEqual(expected, self.sol.maxDifference(s))


if __name__ == '__main__':
    unittest.main()
