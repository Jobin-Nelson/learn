"""
Created Date: 2025-05-12
Qn: You are given an integer array digits, where each element is a digit. The
    array may contain duplicates.

    You need to find all the unique integers that follow the given
    requirements:

    - The integer consists of the concatenation of three elements from digits
      in any arbitrary order.
    - The integer does not have leading zeros.
    - The integer is even.

    For example, if the given digits were [1, 2, 3], integers 132 and 312
    follow the requirements.

    Return a sorted array of the unique integers.
Link: https://leetcode.com/problems/finding-3-digit-even-numbers/
Notes:
    - find permutations, remove duplicates and return sorted
"""

import unittest
from itertools import permutations


class Solution:
    def findNumbers(self, digits: list[int]) -> list[int]:
        return sorted(
            set(
                n[0] * 100 + n[1] * 10 + n[2]
                for n in permutations(digits, 3)
                if n[0] != 0 and n[2] & 1 == 0
            )
        )


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_findNumbers1(self):
        d = [2, 1, 3, 0]
        expected = [102, 120, 130, 132, 210, 230, 302, 310, 312, 320]
        self.assertEqual(expected, self.sol.findNumbers(d))

    def test_findNumbers2(self):
        d = [2, 2, 8, 8, 2]
        expected = [222, 228, 282, 288, 822, 828, 882]
        self.assertEqual(expected, self.sol.findNumbers(d))

    def test_findNumbers3(self):
        d = [3, 7, 5]
        expected = []
        self.assertEqual(expected, self.sol.findNumbers(d))


if __name__ == '__main__':
    unittest.main()
