"""
Created Date: 2024-12-29
Qn: You are given a list of strings of the same length words and a string
    target.

    Your task is to form target using the given words under the following
    rules:

    - target should be formed from left to right.
    - To form the ith character (0-indexed) of target, you can choose the kth
      character of the jth string in words if target[i] = words[j][k].
    - Once you use the kth character of the jth string of words, you can no
      longer use the xth character of any string in words where x <= k. In
      other words, all characters to the left of or at index k become unusuable
      for every string.
    - Repeat the process until you form the string target.

    Notice that you can use multiple characters from the same string in words
    provided the conditions above are met.

    Return the number of ways to form target from words. Since the answer may
    be too large, return it modulo 109 + 7.
Link: https://leetcode.com/problems/number-of-ways-to-form-a-target-string-given-a-dictionary/
Notes:
    - use dfs and memoization
"""

import unittest


class Solution:
    def numWays(self, words: list[str], target: str) -> int:
        mod = 10**9 + 7
        N = len(words[0])
        cnt = [[0] * 26 for _ in range(N)]
        ord_a = ord('a')

        for w in words:
            for i, c in enumerate(w):
                cnt[i][ord(c) - ord_a] += 1

        dp = {}

        def dfs(i: int, k: int) -> int:
            if i == len(target):
                return 1
            if k == N:
                return 0
            if (i, k) in dp:
                return dp[(i, k)]
            res = dfs(i, k + 1)
            res += cnt[k][ord(target[i]) - ord_a] * dfs(i + 1, k + 1)
            dp[(i, k)] = res % mod
            return dp[(i, k)]

        return dfs(0, 0)


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_numWays1(self):
        w, t = ["acca", "bbbb", "caca"], "aba"
        expected = 6
        self.assertEqual(expected, self.sol.numWays(w, t))

    def test_numWays2(self):
        w, t = ["abba", "baab"], "bab"
        expected = 4
        self.assertEqual(expected, self.sol.numWays(w, t))


if __name__ == '__main__':
    unittest.main()
