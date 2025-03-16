"""
Created Date: 2025-03-11
Qn: Given a string s consisting only of characters a, b and c.

    Return the number of substrings containing at least one occurrence of all
    these characters a, b and c.
Link: https://leetcode.com/problems/number-of-substrings-containing-all-three-characters/
Notes:
"""

import unittest
from itertools import accumulate


class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        # Functional approach
        def count(acc: list[int], i: int) -> list[int]:
            acc[ord(s[i]) - ord('a')] = i
            return acc

        def add_one(x: int) -> int:
            return 1 + x

        last_pos = accumulate(range(len(s)), count, initial=[-1, -1, -1])
        min_last_pos = map(min, last_pos)
        add_one_min_last_pos = map(add_one, min_last_pos)
        return sum(add_one_min_last_pos)


        # Imperative approach
        # last_pos = [-1] * 3
        # total = 0
        # for pos in range(len(s)):
        #     last_pos[ord(s[pos]) - ord('a')] = pos
        #     total += 1 + min(last_pos)
        # return total


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_numberOfSubstrings1(self):
        s = "abcabc"
        expected = 10
        self.assertEqual(expected, self.sol.numberOfSubstrings(s))

    def test_numberOfSubstrings2(self):
        s = "aaacb"
        expected = 3
        self.assertEqual(expected, self.sol.numberOfSubstrings(s))

    def test_numberOfSubstrings3(self):
        s = "abc"
        expected = 1
        self.assertEqual(expected, self.sol.numberOfSubstrings(s))


if __name__ == '__main__':
    unittest.main()
