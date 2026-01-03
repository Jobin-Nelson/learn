"""
Created Date: 2026-01-01
Qn: You are given a large integer represented as an integer array digits, where
    each digits[i] is the ith digit of the integer. The digits are ordered from
    most significant to least significant in left-to-right order. The large
    integer does not contain any leading 0's.

    Increment the large integer by one and return the resulting array of
    digits.
Link: https://leetcode.com/problems/plus-one/
Notes:
"""

import unittest


class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        i = len(digits) - 1
        while i >= 0 and digits[i] == 9:
            digits[i] = 0
            if i == 0:
                return [1] + digits
            else:
                i -= 1
        else:
            digits[i] += 1
        return digits


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test1(self):
        d = [1, 2, 3]
        expected = [1, 2, 4]
        self.assertEqual(expected, self.sol.plusOne(d))

    def test2(self):
        d = list(range(4, 0, -1))
        expected = [4, 3, 2, 2]
        self.assertEqual(expected, self.sol.plusOne(d))

    def test3(self):
        d = [9]
        expected = [1, 0]
        self.assertEqual(expected, self.sol.plusOne(d))


if __name__ == '__main__':
    unittest.main()
