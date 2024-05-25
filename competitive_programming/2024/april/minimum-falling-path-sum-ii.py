"""
Created Date: 2024-04-26
Qn: Given an n x n integer matrix grid, return the minimum sum of a falling
    path with non-zero shifts.

    A falling path with non-zero shifts is a choice of exactly one element from
    each row of grid such that no two elements chosen in adjacent rows are in
    the same column.
Link: https://leetcode.com/problems/minimum-falling-path-sum-ii/
Notes:
"""
from sys import maxsize

def minFallingPathSum(grid: list[list[int]]) -> int:
    # N = grid[0]
    # prev_dp = grid[0]
    #
    # for r in range(1, N):
    #     dp = [float('inf')] * N
    #     for cur_c in range(N):
    #         for prev_c in range(N):
    #             if prev_c != cur_c:
    #                 dp[cur_c] = min(
    #                     dp[cur_c],
    #                     grid[r][cur_c] + dp[prev_c]
    #                 )
    #     prev_dp = dp
    # return min(prev_dp)


    # R, C = len(grid), len(grid[0])
    # memo = {}
    # def dfs(r: int, c: int) -> int:
    #     if (r, c) in memo: return memo[(r, c)]
    #     if r == R-1: return grid[r][c]
    #     res = maxsize
    #     for next_col in range(C):
    #         if next_col != c:
    #             res = min(
    #                 res,
    #                 grid[r][c] + dfs(r+1, next_col)
    #             )
    #     memo[(r, c)] = res
    #     return res
    # res = maxsize
    # for c in range(C):
    #     res = min(res, dfs(0, c))
    # return res



if __name__ == '__main__':
    g1 = [[1,2,3],[4,5,6],[7,8,9]]
    g2 = [[7]]

    print(minFallingPathSum(g1))
    print(minFallingPathSum(g2))
