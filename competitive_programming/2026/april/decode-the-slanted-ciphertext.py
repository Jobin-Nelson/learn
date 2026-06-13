"""
Created Date: 2026-04-04
Qn:
Link: https://leetcode.com/problems/decode-the-slanted-ciphertext/
Notes:
"""

import unittest


class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        n = len(encodedText)
        C = n // rows

        return ''.join(
            encodedText[i] for c in range(C) for i in range(c, n, C + 1)
        ).rstrip()


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test1(self):
        enc, rows = "ch   ie   pr", 3
        expected = "cipher"
        self.assertEqual(expected, self.sol.decodeCiphertext(enc, rows))

    def test2(self):
        enc, rows = "iveo    eed   l te   olc", 4
        expected = "i love leetcode"
        self.assertEqual(expected, self.sol.decodeCiphertext(enc, rows))

    def test3(self):
        enc, rows = "coding", 1
        expected = "coding"
        self.assertEqual(expected, self.sol.decodeCiphertext(enc, rows))


if __name__ == '__main__':
    unittest.main()
