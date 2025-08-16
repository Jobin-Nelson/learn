"""
Created Date: 2025-08-14
Qn:You are given a string num representing a large integer. An integer is good
    if it meets the following conditions:

    - It is a substring of num with length 3.
    - It consists of only one unique digit.

    Return the maximum good integer as a string or an empty string "" if no
    such integer exists.

    Note:

    - A substring is a contiguous sequence of characters within a string.
    - There may be leading zeroes in num or a good integer.
Link: https://leetcode.com/problems/largest-3-same-digit-number-in-string/
Notes:
    - iterate and compare against last 2 previous values
"""

import unittest


class Solution:
    def largestGoodInteger(self, num: str) -> str:
        return max(
            (num[i] for i in range(2, len(num)) if num[i - 2] == num[i - 1] == num[i]),
            key=int,
            default='',
        ) * 3


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_largestGoodInteger1(self):
        n = "6777133339"
        expected = "777"
        self.assertEqual(expected, self.sol.largestGoodInteger(n))

    def test_largestGoodInteger2(self):
        n = "2300019"
        expected = "000"
        self.assertEqual(expected, self.sol.largestGoodInteger(n))

    def test_largestGoodInteger3(self):
        n = "42352338"
        expected = ""
        self.assertEqual(expected, self.sol.largestGoodInteger(n))


if __name__ == '__main__':
    unittest.main()
