"""
Created Date: 2025-06-06
Qn: You are given a string s and a robot that currently holds an empty string
    t. Apply one of the following operations until s and t are both empty:

    - Remove the first character of a string s and give it to the robot. The
      robot will append this character to the string t.
    - Remove the last character of a string t and give it to the robot. The
      robot will write this character on paper.

    Return the lexicographically smallest string that can be written on the
    paper.
Link: https://leetcode.com/problems/using-a-robot-to-print-the-lexicographically-smallest-string/
Notes:
    - use stack
"""

import unittest


class Solution:
    def robotWithString(self, s: str) -> str:
        freq = [0] * 26
        ord_a = ord('a')
        for c in s:
            freq[ord(c) - ord_a] += 1
        min_character_index = 0

        stack = []
        res = []
        for c in s:
            stack.append(c)
            freq[ord(c) - ord_a] -= 1

            while min_character_index < 26 and freq[min_character_index] == 0:
                min_character_index += 1

            while stack and ord(stack[-1]) - ord_a <= min_character_index:
                res.append(stack.pop())
        return ''.join(res)


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_robotWithString1(self):
        s = "zza"
        expected = "azz"
        self.assertEqual(expected, self.sol.robotWithString(s))

    def test_robotWithString2(self):
        s = "bac"
        expected = "abc"
        self.assertEqual(expected, self.sol.robotWithString(s))

    def test_robotWithString3(self):
        s = "bdda"
        expected = "addb"
        self.assertEqual(expected, self.sol.robotWithString(s))


if __name__ == '__main__':
    unittest.main()
