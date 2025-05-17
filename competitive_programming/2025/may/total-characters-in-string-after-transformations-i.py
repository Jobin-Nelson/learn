"""
Created Date: 2025-05-13
Qn: You are given a string s and an integer t, representing the number of
    transformations to perform. In one transformation, every character in s is
    replaced according to the following rules:

    - If the character is 'z', replace it with the string "ab".
    - Otherwise, replace it with the next character in the alphabet. For
      example, 'a' is replaced with 'b', 'b' is replaced with 'c', and so on.

    Return the length of the resulting string after exactly t transformations.

    Since the answer may be very large, return it modulo 109 + 7.
Link: https://leetcode.com/problems/total-characters-in-string-after-transformations-i/
Notes:
    - simulation
"""

import unittest


class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        mod = 10**9 + 7
        count = [0] * 26

        ord_a = ord('a')
        for c in s:
            count[ord(c) - ord_a] += 1

        for _ in range(t):
            nxt = [0] * 26
            nxt[0] = count[25]
            nxt[1] = (count[25] + count[0]) % mod
            for i in range(2, 26):
                nxt[i] = count[i - 1]
            count = nxt
        return sum(count) % mod


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_lengthAfterTransformations1(self):
        s, t = "abcyy", 2
        expected = 7
        self.assertEqual(expected, self.sol.lengthAfterTransformations(s, t))

    def test_lengthAfterTransformations2(self):
        s, t = "azbk", 1
        expected = 5
        self.assertEqual(expected, self.sol.lengthAfterTransformations(s, t))


if __name__ == '__main__':
    unittest.main()
