'''
Created Date: 2023-06-18
Qn: You are given an m x n integer matrix grid, where you can move from a cell
    to any adjacent cell in all 4 directions.

    Return the number of strictly increasing paths in the grid such that you
    can start from any cell and end at any cell. Since the answer may be very
    large, return it modulo 109 + 7.

    Two paths are considered different if they do not have exactly the same
    sequence of visited cells.
Link: https://leetcode.com/problems/number-of-increasing-paths-in-a-grid/
Notes:
    - use dfs
'''
def countPaths(grid: list[list[int]]) -> int:
    m, n = len(grid), len(grid[0])
    mod = 10**9 + 7
    dirs = [0, 1, 0, -1, 0]
    dp = [[0] * n for _ in range(m)]

    def dfs(i: int, j: int) -> int:
        if dp[i][j]: return dp[i][j]
        res = 1
        for k in range(len(dirs) - 1):
            di, dj = i + dirs[k], j + dirs[k + 1]
            if 0 <= di < m and 0 <= dj < n and grid[di][dj] > grid[i][j]:
                res += dfs(di, dj) % mod
        dp[i][j] = res
        return res
    return sum(dfs(i, j) for i in range(m) for j in range(n)) % mod

if __name__ == '__main__':
    g1 = [[1,1],[3,4]]
    g2 = [[1],[2]]

    print(countPaths(g1))
    print(countPaths(g2))
