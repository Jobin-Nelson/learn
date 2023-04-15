'''
Created Date: 2023-04-07
Qn: You are given an m x n binary matrix grid, where 0 represents a sea cell
    and 1 represents a land cell.

    A move consists of walking from one land cell to another adjacent
    (4-directionally) land cell or walking off the boundary of the grid.

    Return the number of land cells in grid for which we cannot walk off the
    boundary of the grid in any number of moves.
Link: https://leetcode.com/problems/number-of-enclaves/
Notes:
    - use dfs
    - remove land cells connected to the edges
    - add up all the leftover land cells
'''
def numEnclaves(grid: list[list[int]]) -> int:
    M, N = len(grid), len(grid[0])

    def dfs(r: int, c: int):
        if r < 0 or c < 0 or r >= M or c >= N or grid[r][c] == 0: return

        grid[r][c] = 0
        dfs(r, c-1) 
        dfs(r, c+1)
        dfs(r-1, c)
        dfs(r+1, c)
    
    for i in range(M):
        for j in [0, N-1]:
            if grid[i][j] == 1: dfs(i, j)

    for i in [0, M-1]:
        for j in range(N):
            if grid[i][j] == 1: dfs(i, j)

    res = sum(sum(row) for row in grid)
    return res

if __name__ == '__main__':
    g1 = [[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]
    g2 = [[0,1,1,0],[0,0,1,0],[0,0,1,0],[0,0,0,0]]
    g3 = [[0,0,0,1,1,1,0,1,0,0],[1,1,0,0,0,1,0,1,1,1],[0,0,0,1,1,1,0,1,0,0],[0,1,1,0,0,0,1,0,1,0],[0,1,1,1,1,1,0,0,1,0],[0,0,1,0,1,1,1,1,0,1],[0,1,1,0,0,0,1,1,1,1],[0,0,1,0,0,1,0,1,0,1],[1,0,1,0,1,1,0,0,0,0],[0,0,0,0,1,1,0,0,0,1]]

    print(numEnclaves(g1))
    print(numEnclaves(g2))
    print(numEnclaves(g3))
