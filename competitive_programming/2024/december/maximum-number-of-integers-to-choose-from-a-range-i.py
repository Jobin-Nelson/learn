"""
Created Date: 2024-12-06
Qn: You are given an integer array banned and two integers n and maxSum. You
    are choosing some number of integers following the below rules:

    - The chosen integers have to be in the range [1, n].
    - Each integer can be chosen at most once.
    - The chosen integers should not be in the array banned.
    - The sum of the chosen integers should not exceed maxSum.

    Return the maximum number of integers you can choose following the
    mentioned rules.
Link: https://leetcode.com/problems/maximum-number-of-integers-to-choose-from-a-range-i/
Notes:
"""

import unittest
from itertools import accumulate
from operator import add


class Solution:
    def maxCount(self, banned: list[int], n: int, maxSum: int) -> int:
        # Functional approach
        banned_set = set(banned)
        unbanned_nums = (i for i in range(1, n + 1) if i not in banned_set)
        return (
            sum(1 for i in accumulate(unbanned_nums, add, initial=0) if i <= maxSum) - 1
        )

        # Imperative approach
        # banned_set = set(banned)
        # res = 0
        # cur_sum =0
        # for i in range(1, n+1):
        #     if cur_sum + i > maxSum:
        #         break
        #     if i not in banned_set:
        #         res += 1
        #         cur_sum += i
        # return res


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_maxCount1(self):
        b = [1, 6, 5]
        n, m = 5, 6
        expected = 2
        self.assertEqual(expected, self.sol.maxCount(b, n, m))

    def test_maxCount2(self):
        b = list(range(1, 8))
        n, m = 8, 1
        expected = 0
        self.assertEqual(expected, self.sol.maxCount(b, n, m))

    def test_maxCount3(self):
        b = [11]
        n, m = 7, 50
        expected = 7
        self.assertEqual(expected, self.sol.maxCount(b, n, m))


if __name__ == '__main__':
    unittest.main()
