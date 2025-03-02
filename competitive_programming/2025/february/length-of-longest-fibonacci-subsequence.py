"""
Created Date: 2025-02-27
Qn: A sequence x1, x2, ..., xn is Fibonacci-like if:

    - n >= 3
    - xi + xi+1 == xi+2 for all i + 2 <= n

    Given a strictly increasing array arr of positive integers forming a
    sequence, return the length of the longest Fibonacci-like subsequence of
    arr. If one does not exist, return 0.

    A subsequence is derived from another sequence arr by deleting any number
    of elements (including none) from arr, without changing the order of the
    remaining elements. For example, [3, 5, 8] is a subsequence of [3, 4, 5, 6,
    7, 8].
Link: https://leetcode.com/problems/length-of-longest-fibonacci-subsequence/
Notes:
    - use dp
"""

import unittest


class Solution:
    def lenLongestFibSubseq(self, arr: list[int]) -> int:
        N = len(arr)
        arr_map = {n: i for i, n in enumerate(arr)}
        dp = [[0] * N for _ in range(N)]
        res = 0

        for i in range(N - 2, -1, -1):
            for j in range(N - 1, i, -1):
                prev, cur = arr[i], arr[j]
                nxt = prev + cur
                length = 2
                if nxt in arr_map:
                    length = 1 + dp[j][arr_map[nxt]]
                    res = max(res, length)
                dp[i][j] = length
        return res


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_lenLongestFibSubseq1(self):
        a = list(range(1, 9))
        expected = 5
        self.assertEqual(expected, self.sol.lenLongestFibSubseq(a))

    def test_lenLongestFibSubseq2(self):
        a = [1, 3, 7, 11, 12, 14, 18]
        expected = 3
        self.assertEqual(expected, self.sol.lenLongestFibSubseq(a))


if __name__ == '__main__':
    unittest.main()
