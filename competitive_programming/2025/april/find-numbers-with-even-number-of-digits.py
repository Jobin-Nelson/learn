"""
Created Date: 2025-04-30
Qn: Given an array nums of integers, return how many of them contain an even
    number of digits.
Link: https://leetcode.com/problems/find-numbers-with-even-number-of-digits/
Notes:
"""

import unittest


class Solution:
    def findNumbers(self, nums: list[int]) -> int:
        def is_even_digit(n: int) -> bool:
            digit = 0
            while n > 0:
                digit += 1
                n //= 10
            return digit & 1 == 0
        return sum(is_even_digit(n) for n in nums)


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_findNumbers1(self):
        n = [12, 345, 2, 6, 7896]
        expected = 2
        self.assertEqual(expected, self.sol.findNumbers(n))

    def test_findNumbers2(self):
        n = [555, 901, 482, 1771]
        expected = 1
        self.assertEqual(expected, self.sol.findNumbers(n))


if __name__ == '__main__':
    unittest.main()
