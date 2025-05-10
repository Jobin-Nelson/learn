"""
Created Date: 2025-05-05
Qn: You have two types of tiles: a 2 x 1 domino shape and a tromino shape. You
    may rotate these shapes.

    Given an integer n, return the number of ways to tile an 2 x n board. Since
    the answer may be very large, return it modulo 109 + 7.

    In a tiling, every square must be covered by a tile. Two tilings are
    different if and only if there are two 4-directionally adjacent cells on
    the board such that exactly one of the tilings has both squares occupied by
    a tile.
Link: https://leetcode.com/problems/domino-and-tromino-tiling/
Notes:
"""

import unittest


class Solution:
    def numTilings(self, n: int) -> int:
        MOD = 10 ** 9 + 7
        dp = [[None]*4 for _ in range(n+1)]

        def solve():
            return f(0, True, True)

        def makeState(t1: bool, t2: bool) -> int:
            if not t1 and not t2: return 0
            if t1 and not t2: return 1
            if not t1 and t2: return 2
            return 3

        def f(i: int, t1: bool, t2: bool) -> int:
            if i == n:
                return 1
            state = makeState(t1, t2)
            if dp[i][state] != None:
                return dp[i][state]
            t3, t4 = i + 1 < n, i + 1 < n
            count = 0
            if t1 and t2 and t3: count += f(i+1, False, True)
            if t1 and t2 and t4: count += f(i+1, True, False)
            if t1 and not t2 and t3 and t4: count += f(i+1, False, False)
            if t1 and not t2 and t3 and t4: count += f(i+1, False, False)
            if t1 and t2: count += f(i+1, True, False)
            if t1 and t2 and t3 and t4: count += f(i+1, False, False)
            if t1 and not t2 and t3: count += f(i+1, False, True)
            if not t1 and t2 and t3: count += f(i+1, True, False)
            if not t1 and not t2: count += f(i+1, True, True)
            dp[i][state] = count % MOD
            return dp[i][state]
        return solve()



class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_numTilings1(self):
        n = 3
        expected = 5
        self.assertEqual(expected, self.sol.numTilings(n))

    def test_numTilings2(self):
        n = 1
        expected = 1
        self.assertEqual(expected, self.sol.numTilings(n))


if __name__ == '__main__':
    unittest.main()
