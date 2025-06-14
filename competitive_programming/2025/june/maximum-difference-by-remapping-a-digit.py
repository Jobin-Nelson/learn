"""
Created Date: 2025-06-14
Qn: You are given an integer num. You know that Bob will sneakily remap one of
    the 10 possible digits (0 to 9) to another digit.

    Return the difference between the maximum and minimum values Bob can make
    by remapping exactly one digit in num.

    Notes:

    - When Bob remaps a digit d1 to another digit d2, Bob replaces all
      occurrences of d1 in num with d2.
    - Bob can remap a digit to itself, in which case num does not change.
    - Bob can remap different digits for obtaining minimum and maximum values
      respectively.
    - The resulting number after remapping can contain leading zeroes.

Link: https://leetcode.com/problems/maximum-difference-by-remapping-a-digit/
Notes:
"""

import unittest


class Solution:
    def minMaxDifference(self, num: int) -> int:
        # Functional
        str_num = str(num)
        max_num = next((d for d in str_num if d != '9'), '9')
        min_num = next((d for d in str_num if d != '0'), '0')
        return int(str_num.replace(max_num, '9')) - int(str_num.replace(min_num, '0'))

        # Imperative
        # str_num = str(num)
        # max_num, min_num = '9', '0'
        # for d in str_num:
        #     # find min_num
        #     if d != '0':
        #         min_num = d
        #         break
        # for d in str_num:
        #     if d != '9':
        #         max_num = d
        #         break
        # return int(str_num.replace(max_num, '9')) - int(str_num.replace(min_num, '0'))


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_minMaxDifference1(self):
        n = 11891
        expected = 99009
        self.assertEqual(expected, self.sol.minMaxDifference(n))

    def test_minMaxDifference2(self):
        n = 90
        expected = 99
        self.assertEqual(expected, self.sol.minMaxDifference(n))


if __name__ == '__main__':
    unittest.main()
