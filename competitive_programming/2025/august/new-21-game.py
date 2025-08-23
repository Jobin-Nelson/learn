"""
Created Date: 2025-08-17
Qn: Alice plays the following game, loosely based on the card game "21".

    Alice starts with 0 points and draws numbers while she has less than k
    points. During each draw, she gains an integer number of points randomly
    from the range [1, maxPts], where maxPts is an integer. Each draw is
    independent and the outcomes have equal probabilities.

    Alice stops drawing numbers when she gets k or more points.

    Return the probability that Alice has n or fewer points.

    Answers within 10-5 of the actual answer are considered accepted.
Link: https://leetcode.com/problems/new-21-game/
Notes:
"""

import unittest


class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        # sliding window
        if k == 0:
            return 1.0

        windowSum = 0
        for i in range(k, k + maxPts):
            windowSum += 1 if i <= n else 0

        dp = {}
        for i in range(k - 1, -1, -1):
            dp[i] = windowSum / maxPts
            remove = 0
            if i + maxPts <= n:
                remove = dp.get(i + maxPts, 1)
            windowSum += dp[i] - remove
        return dp[0]

        # TLE
        # dp: list[float] = [0] * (n + 1)
        # dp[0] = 1
        # for i in range(1, n + 1):
        #     for j in range(1, maxPts + 1):
        #         if i - j >= 0 and i - j < k:
        #             dp[i] += dp[i - j] / maxPts
        # return sum(dp[k:])


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_new21Game1(self):
        n, k, m = 10, 1, 10
        expected = 1.00000
        self.assertAlmostEqual(expected, self.sol.new21Game(n, k, m), places=5)

    def test_new21Game2(self):
        n, k, m = 6, 1, 10
        expected = 0.6
        self.assertAlmostEqual(expected, self.sol.new21Game(n, k, m), places=5)

    def test_new21Game3(self):
        n, k, m = 21, 17, 10
        expected = 0.73278
        self.assertAlmostEqual(expected, self.sol.new21Game(n, k, m), places=5)


if __name__ == '__main__':
    unittest.main()
