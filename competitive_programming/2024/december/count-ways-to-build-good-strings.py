"""
Created Date: 2024-12-30
Qn: Given the integers zero, one, low, and high, we can construct a string by
    starting with an empty string, and then at each step perform either of the
    following:

    - Append the character '0' zero times.
    - Append the character '1' one times. This can be performed any number of
      times.

    A good string is a string constructed by the above process having a length
    between low and high (inclusive).

    Return the number of different good strings that can be constructed
    satisfying these properties. Since the answer can be large, return it
    modulo 109 + 7.
Link: https://leetcode.com/problems/count-ways-to-build-good-strings/
Notes:
    - use dp
"""

import unittest

class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        dp = [1] + [-1] * high
        mod = 10**9 + 7

        def dfs(end: int) -> int:
            if dp[end] != -1:
                return dp[end]
            count = 0
            if end >= zero:
                count += dfs(end - zero)
            if end >= one:
                count += dfs(end - one)
            dp[end] = count % mod
            return dp[end]

        return sum(dfs(end) for end in range(low, high + 1)) % mod


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_countGoodStrings1(self):
        l, h, z, o = 3, 3, 1, 1
        expected = 8
        self.assertEqual(expected, self.sol.countGoodStrings(l, h, z, o))

    def test_countGoodStrings2(self):
        l, h, z, o = 2, 3, 1, 2
        expected = 5
        self.assertEqual(expected, self.sol.countGoodStrings(l, h, z, o))


if __name__ == '__main__':
    unittest.main()
