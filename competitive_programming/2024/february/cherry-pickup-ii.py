"""
Created Date: 2024-02-11
Qn: You are given a rows x cols matrix grid representing a field of cherries
    where grid[i][j] represents the number of cherries that you can collect
    from the (i, j) cell.

    You have two robots that can collect cherries for you:

        - Robot #1 is located at the top-left corner (0, 0), and 
        - Robot #2 is located at the top-right corner (0, cols - 1).

    Return the maximum number of cherries collection using both robots by
    following the rules below:

        - From a cell (i, j), robots can move to cell (i + 1, j - 1), (i + 1,
          j), or (i + 1, j + 1). 
        - When any robot passes through a cell, It picks up all cherries, and
          the cell becomes an empty cell. 
        - When both robots stay in the same cell, only one takes the cherries. 
        - Both robots cannot move outside of the grid at any moment. 
        - Both robots should reach the bottom row in grid.

Link: https://leetcode.com/problems/cherry-pickup-ii/
Notes:
    - use tabulation or dfs with memoization
"""
from itertools import product

def cherryPickup(grid: list[list[int]]) -> int:
    R, C = len(grid), len(grid[0])
    dp = [[0] * C for _ in range(C)]

    for r in range(R-1, -1, -1):
        cur_dp = [[0] * C for _ in range(C)]
        for c1 in range(C-1):
            for c2 in range(c1+1, C):
                max_cherries = 0
                cherries = grid[r][c1] + grid[r][c2]
                for c1d, c2d in product([-1, 0, 1], [-1, 0, 1]):
                    nc1, nc2 = c1 + c1d, c2 + c2d
                    if nc1 < 0 or nc2 == C: continue
                    max_cherries = max(max_cherries, cherries + dp[nc1][nc2])
                cur_dp[c1][c2] = max_cherries
        dp = cur_dp
    return dp[0][C-1]


    # memo = {}
    #
    # def dfs(r: int, c1: int, c2: int) -> int:
    #     if (r, c1, c2) in memo: return memo[(r, c1, c2)]
    #     if c1 == c2 or min(c1, c2) < 0 or max(c1, c2) == C: return 0
    #     if r == R - 1: return grid[r][c1] + grid[r][c2]
    #     res = 0
    #     for c1d in (-1, 0, 1):
    #         for c2d in (-1, 0, 1):
    #             res = max(res, dfs(r+1, c1 + c1d, c2 + c2d))
    #     memo[(r, c1, c2)] = res + grid[r][c1] + grid[r][c2]
    #     return memo[(r, c1, c2)]
    # return dfs(0, 0, C-1)

if __name__ == '__main__':
    g1 = [[3,1,1],[2,5,1],[1,5,5],[2,1,1]]
    g2 = [[1,0,0,0,0,0,1],[2,0,0,0,0,3,0],[2,0,9,0,0,0,0],[0,3,0,5,4,0,0],[1,0,2,3,0,0,6]]

    print(cherryPickup(g1))
    print(cherryPickup(g2))
