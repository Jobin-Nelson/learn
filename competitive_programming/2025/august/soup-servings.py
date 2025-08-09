"""
Created Date: 2025-08-08
Qn: You have two soups, A and B, each starting with n mL. On every turn, one of
    the following four serving operations is chosen at random, each with
    probability 0.25 independent of all previous turns:

    - pour 100 mL from type A and 0 mL from type B
    - pour 75 mL from type A and 25 mL from type B
    - pour 50 mL from type A and 50 mL from type B
    - pour 25 mL from type A and 75 mL from type B

    Note:

    - There is no operation that pours 0 mL from A and 100 mL from B.
    - The amounts from A and B are poured simultaneously during the turn.
    - If an operation asks you to pour more than you have left of a soup, pour
      all that remains of that soup.

    The process stops immediately after any turn in which one of the soups is
    used up.

    Return the probability that A is used up before B, plus half the
    probability that both soups are used up in the same turn. Answers within
    10-5 of the actual answer will be accepted.
Link: https://leetcode.com/problems/soup-servings/
Notes:
"""

import unittest
from collections import defaultdict
from math import ceil


class Solution:
    def soupServings(self, n: int) -> float:
        m = ceil(n / 25)
        dp = defaultdict(dict)

        def calculate_dp(i: int, j: int) -> float:
            if i <= 0 and j <= 0:
                return 0.5
            elif i <= 0:
                return 1.0
            elif j <= 0:
                return 0.0
            if i in dp and j in dp[i]:
                return dp[i][j]
            dp[i][j] = (
                calculate_dp(i - 4, j)
                + calculate_dp(i - 3, j - 1)
                + calculate_dp(i - 2, j - 2)
                + calculate_dp(i - 1, j - 3)
            ) / 4.0
            return dp[i][j]

        for k in range(1, m + 1):
            if calculate_dp(k, k) > 1 - 1e-5:
                return 1.0
        return calculate_dp(m, m)


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_soupServings1(self):
        n = 50
        expected = 0.62500
        self.assertEqual(expected, self.sol.soupServings(n))

    def test_soupServings2(self):
        n = 100
        expected = 0.71875
        self.assertEqual(expected, self.sol.soupServings(n))


if __name__ == '__main__':
    unittest.main()
