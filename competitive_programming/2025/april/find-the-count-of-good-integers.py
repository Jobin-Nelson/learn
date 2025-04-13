"""
Created Date: 2025-04-12
Qn: You are given two positive integers n and k.

    An integer x is called k-palindromic if:

    - x is a palindrome.
    - x is divisible by k.

    An integer is called good if its digits can be rearranged to form a
    k-palindromic integer. For example, for k = 2, 2020 can be rearranged to
    form the k-palindromic integer 2002, whereas 1010 cannot be rearranged to
    form a k-palindromic integer.

    Return the count of good integers containing n digits. Note that any
    integer must not have leading zeros, neither before nor after
    rearrangement. For example, 1010 cannot be rearranged to form 101.
Link: https://leetcode.com/problems/find-the-count-of-good-integers/
Notes:
    - generate palindrome
    - sort and store in hashset for removing duplicates
    - count the permutations, taking into account leading zeroes
"""

import unittest
import math


class Solution:
    def countGoodIntegers(self, n: int, k: int) -> int:
        dictionary = set()
        base = 10 ** ((n - 1) >> 1)
        skip = n & 1
        for i in range(base, base * 10):
            s = str(i)
            s += s[::-1][skip:]
            palindromicInteger = int(s)
            if palindromicInteger % k == 0:
                dictionary.add(''.join(sorted(s)))

        fac = [math.factorial(i) for i in range(n + 1)]
        res = 0
        for s in dictionary:
            count = [0] * 10
            for c in s:
                count[int(c)] += 1
            total = (n - count[0]) * fac[n - 1]
            for x in count:
                total //= fac[x]
            res += total
        return res


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_countGoodIntegers1(self):
        n, k = 3, 5
        expected = 27
        self.assertEqual(expected, self.sol.countGoodIntegers(n, k))

    def test_countGoodIntegers2(self):
        n, k = 1, 4
        expected = 2
        self.assertEqual(expected, self.sol.countGoodIntegers(n, k))

    def test_countGoodIntegers3(self):
        n, k = 5, 6
        expected = 2468
        self.assertEqual(expected, self.sol.countGoodIntegers(n, k))


if __name__ == '__main__':
    unittest.main()
