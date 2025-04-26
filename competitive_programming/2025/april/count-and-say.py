"""
Created Date: 2025-04-18
Qn: The count-and-say sequence is a sequence of digit strings defined by the
    recursive formula:

    - countAndSay(1) = "1"
    - countAndSay(n) is the run-length encoding of countAndSay(n - 1).

    Run-length encoding (RLE) is a string compression method that works by
    replacing consecutive identical characters (repeated 2 or more times) with
    the concatenation of the character and the number marking the count of the
    characters (length of the run). For example, to compress the string
    "3322251" we replace "33" with "23", replace "222" with "32", replace "5"
    with "15" and replace "1" with "11". Thus the compressed string becomes
    "23321511".

    Given a positive integer n, return the nth element of the count-and-say
    sequence.
Link: https://leetcode.com/problems/count-and-say/
Notes:
"""

import unittest


class Solution:
    def countAndSay(self, n: int) -> str:
        cur = "1"

        def rle(s: str) -> str:
            prev = s[0]
            count = 1
            res = []
            for c in s[1:]:
                if c == prev:
                    count += 1
                else:
                    res.append(f'{count}{prev}')
                    prev = c
                    count = 1

            return ''.join(res) + f'{count}{prev}'

        for _ in range(1, n):
            cur = rle(cur)
        return cur


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_countAndSay1(self):
        n = 4
        expected = "1211"
        self.assertEqual(expected, self.sol.countAndSay(n))

    def test_countAndSay2(self):
        n = 1
        expected = "1"
        self.assertEqual(expected, self.sol.countAndSay(n))


if __name__ == '__main__':
    unittest.main()
