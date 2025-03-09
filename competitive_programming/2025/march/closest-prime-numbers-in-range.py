"""
Created Date: 2025-03-07
Qn: Given two positive integers left and right, find the two integers num1 and
    num2 such that:

    - left <= num1 < num2 <= right .
    - Both num1 and num2 are prime numbers.
    - num2 - num1 is the minimum amongst all other pairs satisfying the above
      conditions.

    Return the positive integer array ans = [num1, num2]. If there are multiple
    pairs satisfying these conditions, return the one with the smallest num1
    value. If no such numbers exist, return [-1, -1].
Link: https://leetcode.com/problems/closest-prime-numbers-in-range/
Notes:
"""

import unittest
import math
from itertools import pairwise


class Solution:
    def closestPrime(self, left: int, right: int) -> list[int]:
        # Functional approach
        primes = [True] * (right + 1)
        primes[0] = primes[1] = False
        for num in range(2, int(math.sqrt(right)) + 1):
            if not primes[num]:
                continue
            for n in range(num + num, right + 1, num):
                primes[n] = False
        primes = [i for i, v in enumerate(primes) if v and i >= left]
        return min(
            map(list, pairwise(primes)), key=lambda x: x[1] - x[0], default=[-1, -1]
        )

        # Imperative approach
        # primes = [True] * (right+1)
        # primes[0] = primes[1] = False
        # for num in range(2, int(math.sqrt(right)) + 1):
        #     for n in range(num+num, right+1, num):
        #         primes[n] = False
        # primes = [i for i, v in enumerate(primes) if v and i >= left]
        #
        # res = [-1, -1]
        # cur_min = right - left + 1
        # for i in range(len(primes)-1):
        #     x, y = primes[i], primes[i+1]
        #     if y - x < cur_min:
        #         cur_min = y - x
        #         res = [x, y]
        # return res


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_closestPrime1(self):
        l, r = 10, 19
        expected = [11, 13]
        self.assertEqual(expected, self.sol.closestPrime(l, r))

    def test_closestPrime2(self):
        l, r = 4, 6
        expected = [-1, -1]
        self.assertEqual(expected, self.sol.closestPrime(l, r))


if __name__ == '__main__':
    unittest.main()
