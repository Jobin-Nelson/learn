"""
Created Date: 2025-02-28
Qn: Given two strings str1 and str2, return the shortest string that has both
    str1 and str2 as subsequences. If there are multiple valid strings, return
    any of them.

    A string s is a subsequence of string t if deleting some number of
    characters from t (possibly 0) results in the string s.
Link: https://leetcode.com/problems/shortest-common-supersequence/
Notes:
    - use dp
"""

import unittest


class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        N, M = len(str1), len(str2)
        prev = [str2[j:] for j in range(M + 1)]

        for i in range(N - 1, -1, -1):
            cur = [""] * (M + 1)
            cur[-1] = str1[i:]
            for j in range(M - 1, -1, -1):
                if str1[i] == str2[j]:
                    cur[j] = str1[i] + prev[j + 1]
                else:
                    cur[j] = min(str1[i] + prev[j], str2[j] + cur[j + 1], key=len)
            prev = cur
        return prev[0]

        # Memory Limit Exceeded
        # cache = {}
        # def backtrack(i: int, j: int) -> str:
        #     if (i, j) in cache:
        #         return cache[(i, j)]
        #     if i == len(str1):
        #         return str2[j:]
        #     if j == len(str2):
        #         return str1[i:]
        #     if str1[i] == str2[j]:
        #         return str1[i] + backtrack(i + 1, j + 1)
        #     res = min(
        #         str1[i] + backtrack(i + 1, j), str2[j] + backtrack(i, j + 1), key=len
        #     )
        #     cache[(i, j)] = res
        #     return res
        #
        # return backtrack(0, 0)


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_shortestCommonSupersequence1(self):
        s1, s2 = "abac", "cab"
        expected = "cabac"
        self.assertEqual(expected, self.sol.shortestCommonSupersequence(s1, s2))

    def test_shortestCommonSupersequence2(self):
        s1, s2 = "aaaaaaaa", "aaaaaaaa"
        expected = "aaaaaaaa"
        self.assertEqual(expected, self.sol.shortestCommonSupersequence(s1, s2))


if __name__ == '__main__':
    unittest.main()
