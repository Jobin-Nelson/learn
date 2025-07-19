"""
Created Date: 2025-07-15
Qn: A word is considered valid if:

    - It contains a minimum of 3 characters.
    - It contains only digits (0-9), and English letters (uppercase and
      lowercase).
    - It includes at least one vowel.
    - It includes at least one consonant.

    You are given a string word.

    Return true if word is valid, otherwise, return false.

    Notes:

    - 'a', 'e', 'i', 'o', 'u', and their uppercases are vowels.
    - A consonant is an English letter that is not a vowel.
Link: https://leetcode.com/problems/valid-word/
Notes:
"""

import unittest


class Solution:
    def isValid(self, word: str) -> bool:
        if len(word) < 3 or not word.isalnum():
            return False
        vowels = ['a', 'e', 'i', 'o', 'u']
        return any(c in vowels for c in word.lower()) and any(
            c not in vowels for c in word.lower() if c.isalpha()
        )


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_isValid1(self):
        w = "234Adas"
        expected = True
        self.assertEqual(expected, self.sol.isValid(w))

    def test_isValid2(self):
        w = "b3"
        expected = False
        self.assertEqual(expected, self.sol.isValid(w))

    def test_isValid3(self):
        w = "a3$e"
        expected = False
        self.assertEqual(expected, self.sol.isValid(w))

    def test_isValid4(self):
        w = "UuE6"
        expected = False
        self.assertEqual(expected, self.sol.isValid(w))


if __name__ == '__main__':
    unittest.main()
