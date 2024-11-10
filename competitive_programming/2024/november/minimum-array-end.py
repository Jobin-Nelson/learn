"""
Created Date: 2024-11-09
Qn: You are given two integers n and x. You have to construct an array of
    positive integers nums of size n where for every 0 <= i < n - 1, nums[i +
    1] is greater than nums[i], and the result of the bitwise AND operation
    between all elements of nums is x.

    Return the minimum possible value of nums[n - 1].
Link: https://leetcode.com/problems/minimum-array-end/
Notes:
"""

from typing import Callable, Iterable
import unittest
from functools import partial, reduce
from itertools import accumulate, repeat, takewhile
from operator import lshift, rshift


class Solution:
    def minEnd(self, n: int, x: int) -> int:
        # Functional approach
        # def iterate(f: Callable, x: int) -> Iterable:
        #     return accumulate(repeat(x), lambda fx, _: f(fx))
        # lshift1 = partial(lshift, 1)
        # lt = iterate(lshift1, 1)
        # lt = filter(lambda n: n & x == 0, lt)
        # rshift1 = partial(rshift, 1)
        # rt = iterate(rshift1, n)
        # rt = takewhile(lambda n: n > 0, rt)
        # it = zip(lt, rt)
        # return reduce(lambda x, y: x | (y[1] & 1) * y[0], it, x)

        # Imperative approach
        res = x
        mask = 1
        n -= 1
        while n > 0:
            if (mask & x) == 0:
                res |= (n & 1) * mask
                n >>= 1
            mask <<= 1
        return res


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_minEnd1(self):
        n, x = 3, 4
        self.assertEqual(self.sol.minEnd(n, x), 6)
    def test_minEnd2(self):
        n, x = 2, 7
        self.assertEqual(self.sol.minEnd(n, x), 15)


if __name__ == '__main__':
    unittest.main()
