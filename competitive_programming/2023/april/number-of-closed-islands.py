'''
Created Date: 2023-04-06
Qn: Given a 2D grid consists of 0s (land) and 1s (water).  An island is a
    maximal 4-directionally connected group of 0s and a closed island is an
    island totally (all left, top, right, bottom) surrounded by 1s.

    Return the number of closed islands
Link: https://leetcode.com/problems/number-of-closed-islands/
Notes:
    - use dfs to mark nodes as visited and return True only if you encounter 1
'''
def closedIsland(grid: list[list[int]]) -> int:
    # M, N = len(grid), len(grid[0])
    # def dfs(r: int, c: int) -> bool:
    #     if r < 0 or r >= M or c < 0 or c >= N: return False
    #     if grid[r][c] == 1: return True
    #     grid[r][c] = 1
    #
    #     return dfs(r+1, c) and dfs(r-1, c) and dfs(r, c+1) and dfs(r, c-1)
    #
    # res = 0
    # for i in range(M):
    #     for j in range(N):
    #         if grid[i][j] == 0 and dfs(i, j):
    #             res += 1
    # return res
    rows, cols = len(grid), len(grid[0])
    count = 0
    
    def dfs(i, j):
        if i < 0 or j < 0 or i >= rows or j >= cols: return False
        if grid[i][j] == 1: return True

        grid[i][j] = 1 # mark as visited

        left = dfs(i, j-1)
        right = dfs(i, j+1)
        up = dfs(i-1, j)
        down = dfs(i+1, j)
        return left and right and up and down
    
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 0 and dfs(i, j):
                count += 1
    
    return count

if __name__ == '__main__':
    g1 = [[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,1,0,1],[1,1,1,1,1,1,1,0]]
    g2 = [[0,0,1,0,0],[0,1,0,1,0],[0,1,1,1,0]]
    g3 = [[0,0,1,1,0,1,0,0,1,0],[1,1,0,1,1,0,1,1,1,0],[1,0,1,1,1,0,0,1,1,0],[0,1,1,0,0,0,0,1,0,1],[0,0,0,0,0,0,1,1,1,0],[0,1,0,1,0,1,0,1,1,1],[1,0,1,0,1,1,0,0,0,1],[1,1,1,1,1,1,0,0,0,0],[1,1,1,0,0,1,0,1,0,1],[1,1,1,0,1,1,0,1,1,0]]

    print(closedIsland(g1))
    print(closedIsland(g2))
    print(closedIsland(g3))
