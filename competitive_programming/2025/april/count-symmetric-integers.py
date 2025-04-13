"""
Created Date: 2025-04-11
Qn: You are given two positive integers low and high.

    An integer x consisting of 2 * n digits is symmetric if the sum of the
    first n digits of x is equal to the sum of the last n digits of x. Numbers
    with an odd number of digits are never symmetric.

    Return the number of symmetric integers in the range [low, high].
Link: https://leetcode.com/problems/count-symmetric-integers/
Notes:
"""

import unittest


class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        res = 0
        for i in range(low, high+1):
            if i < 100 and i % 11 == 0:
                res +=1
            elif 1000 <= i < 10000:
                left = i // 1000 + i % 1000 // 100
                right = i % 100 // 10 + i % 10
                if left == right:
                    res += 1
        return res


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_countSymmetricIntegers1(self):
        l, h = 1, 100
        expected = 9
        self.assertEqual(expected, self.sol.countSymmetricIntegers(l, h))

    def test_countSymmetricIntegers2(self):
        l, h = 1200, 1230
        expected = 4
        self.assertEqual(expected, self.sol.countSymmetricIntegers(l, h))


if __name__ == '__main__':
    unittest.main()
