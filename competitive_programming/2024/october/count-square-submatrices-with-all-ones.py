"""
Created Date: 2024-10-27
Qn: Given a m * n matrix of ones and zeros, return how many square submatrices
    have all ones.
Link: https://leetcode.com/problems/count-square-submatrices-with-all-ones/
Notes:
    - use dp
"""

import unittest


class Solution:
    def countSquares(self, matrix: list[list[int]]) -> int:
        R, C = len(matrix), len(matrix[0])
        prev_dp = [0] * (C + 1)

        res = 0
        for r in range(R):
            cur_dp = [0] * (C + 1)
            for c in range(C):
                if matrix[r][c] == 1:
                    cur_dp[c + 1] = 1 + min(prev_dp[c + 1], prev_dp[c], cur_dp[c])
                    res += cur_dp[c + 1]
            prev_dp = cur_dp
        return res

        # Recursive Approach
        # R, C = len(matrix), len(matrix[0])
        # memo = {}
        # def dfs(r: int, c: int) -> int:
        #     if r >= R or c >= C or matrix[r][c] == 0:
        #         return 0
        #     if (r, c) in memo:
        #         return memo[(r,c)]
        #     nonlocal res
        #     bottom = dfs(r+1, c)
        #     bottom_right = dfs(r+1, c+1)
        #     right = dfs(r, c+1)
        #     cur_res =  min(bottom, bottom_right, right) + 1
        #     memo[(r,c)] = cur_res
        #     return cur_res
        # res = 0
        # for r in range(R):
        #     for c in range(C):
        #         res += dfs(r, c)
        # return res


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_countSquares1(self):
        m = [[0, 1, 1, 1], [1, 1, 1, 1], [0, 1, 1, 1]]
        self.assertEqual(self.sol.countSquares(m), 15)

    def test_countSquares2(self):
        m = [[1, 0, 1], [1, 1, 0], [1, 1, 0]]
        self.assertEqual(self.sol.countSquares(m), 7)


if __name__ == '__main__':
    unittest.main()
