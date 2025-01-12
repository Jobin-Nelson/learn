"""
Created Date: 2024-12-31
Qn: You have planned some train traveling one year in advance. The days of the
    year in which you will travel are given as an integer array days. Each day
    is an integer from 1 to 365.

    Train tickets are sold in three different ways:

    - a 1-day pass is sold for costs[0] dollars,
    - a 7-day pass is sold for costs[1] dollars, and
    - a 30-day pass is sold for costs[2] dollars.

    The passes allow that many days of consecutive travel.

    - For example, if we get a 7-day pass on day 2, then we can travel for 7
      days: 2, 3, 4, 5, 6, 7, and 8.

    Return the minimum number of dollars you need to travel every day in the
    given list of days.
Link: https://leetcode.com/problems/minimum-cost-for-tickets/
Notes:
    - use dp
"""

import unittest
from sys import maxsize


class Solution:
    def minCostTickets(self, days: list[int], costs: list[int]) -> int:
        dp = [0] * (len(days) + 1)
        for i in reversed(range(len(days))):
            j = i
            dp[i] = maxsize
            for cost, duration in zip(costs, [1, 7, 30]):
                while j < len(days) and days[j] < days[i] + duration:
                    j += 1
                dp[i] = min(dp[i], cost + dp[j])
        return dp[0]


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_minCostTickets1(self):
        d = [1, 4, 6, 7, 8, 20]
        c = [2, 7, 15]
        expected = 11
        self.assertEqual(expected, self.sol.minCostTickets(d, c))

    def test_minCostTickets2(self):
        d = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 30, 31]
        c = [2, 7, 15]
        expected = 17
        self.assertEqual(expected, self.sol.minCostTickets(d, c))


if __name__ == '__main__':
    unittest.main()
