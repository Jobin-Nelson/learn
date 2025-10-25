"""
Created Date: 2025-10-24
Qn: An integer x is numerically balanced if for every digit d in the number x,
    there are exactly d occurrences of that digit in x.

    Given an integer n, return the smallest numerically balanced number
    strictly greater than n.
Link: https://leetcode.com/problems/next-greater-numerically-balanced-number/
Notes:
"""

import unittest
from collections import Counter


class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        for i in range(n + 1, 12244445):
            count = Counter(str(i))
            if all(count[d] == int(d) for d in count):
                return i
        return -1


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test1(self):
        n = 1
        expected = 22
        self.assertEqual(expected, self.sol.nextBeautifulNumber(n))

    def test2(self):
        n = 1000
        expected = 1333
        self.assertEqual(expected, self.sol.nextBeautifulNumber(n))

    def test3(self):
        n = 3000
        expected = 3133
        self.assertEqual(expected, self.sol.nextBeautifulNumber(n))


if __name__ == '__main__':
    unittest.main()
