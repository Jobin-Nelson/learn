"""
Created Date: 2025-06-15
Qn: You are given an integer num. You will apply the following steps to num two
    separate times:

    - Pick a digit x (0 <= x <= 9).
    - Pick another digit y (0 <= y <= 9). Note y can be equal to x.
    - Replace all the occurrences of x in the decimal representation of num by
      y.

    Let a and b be the two results from applying the operation to num
    independently.

    Return the max difference between a and b.

    Note that neither a nor b may have any leading zeros, and must not be 0.
Link: https://leetcode.com/problems/max-difference-you-can-get-from-changing-an-integer/
Notes:
"""

import unittest


class Solution:
    def maxDiff(self, num: int) -> int:
        str_num = str(num)
        max_d = next((d for d in str_num if d != '9'), '9')
        min_d = (
            str_num.replace(str_num[0], '1')
            if str_num[0] != '1'
            else str_num.replace(
                next((d for d in str_num if d != '0' and d != str_num[0]), '0'), '0'
            )
        )
        return int(str_num.replace(max_d, '9')) - int(min_d)


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_maxDiff1(self):
        n = 555
        expected = 888
        self.assertEqual(expected, self.sol.maxDiff(n))

    def test_maxDiff2(self):
        n = 9
        expected = 8
        self.assertEqual(expected, self.sol.maxDiff(n))

    def test_maxDiff3(self):
        n = 123456
        expected = 820000
        self.assertEqual(expected, self.sol.maxDiff(n))


if __name__ == '__main__':
    unittest.main()
