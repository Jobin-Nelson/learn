"""
Created Date: 2024-12-18
Qn: You are given an integer array prices where prices[i] is the price of the
    ith item in a shop.

    There is a special discount for items in the shop. If you buy the ith item,
    then you will receive a discount equivalent to prices[j] where j is the
    minimum index such that j > i and prices[j] <= prices[i]. Otherwise, you
    will not receive any discount at all.

    Return an integer array answer where answer[i] is the final price you will
    pay for the ith item of the shop, considering the special discount.
Link: https://leetcode.com/problems/final-prices-with-a-special-discount-in-a-shop/
Notes:
    - use monotonic stack
"""

from collections import deque
import unittest


class Solution:
    def finalPrices(self, prices: list[int]) -> list[int]:
        res = prices.copy()
        stack = deque()
        for i, p in enumerate(prices):
            while stack and prices[stack[-1]] >= p:
                res[stack.pop()] -= p
            stack.append(i)
        return res


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_finalPrice1(self):
        p = [8, 4, 6, 2, 3]
        expected = [4, 2, 4, 2, 3]
        self.assertEqual(expected, self.sol.finalPrices(p))

    def test_finalPrice2(self):
        p = list(range(1, 6))
        expected = list(range(1, 6))
        self.assertEqual(expected, self.sol.finalPrices(p))


if __name__ == '__main__':
    unittest.main()
