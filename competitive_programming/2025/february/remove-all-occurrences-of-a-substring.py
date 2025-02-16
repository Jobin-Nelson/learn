"""
Created Date: 2025-02-11
Qn: Given two strings s and part, perform the following operation on s until
    all occurrences of the substring part are removed:

    Find the leftmost occurrence of the substring part and remove it from s. Return
    s after removing all occurrences of part.

    A substring is a contiguous sequence of characters in a string.
Link: https://leetcode.com/problems/remove-all-occurrences-of-a-substring/
Notes:
    - use stack
"""

import unittest


class Solution:
    def removeOccurences(self, s: str, part: str) -> str:
        res = []
        part_len = len(part)
        for c in s:
            res.append(c)
            if len(res) >= part_len and ''.join(res[-part_len:]) == part:
                for _ in range(part_len):
                    res.pop()
        return ''.join(res)



class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_removeOccurences1(self):
        s, p = "daabcbaabcbc", "abc"
        expected = 'dab'
        self.assertEqual(expected, self.sol.removeOccurences(s, p))

    def test_removeOccurences2(self):
        s, p = "axxxxyyyyb", "xy"
        expected = 'ab'
        self.assertEqual(expected, self.sol.removeOccurences(s, p))


if __name__ == '__main__':
    unittest.main()
