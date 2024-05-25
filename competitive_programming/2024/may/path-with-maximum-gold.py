"""
Created Date: 2024-05-14
Qn: In a gold mine grid of size m x n, each cell in this mine has an integer representing the amount of gold in that cell, 0 if it is empty.

    Return the maximum amount of gold you can collect under the conditions:

        - Every time you are located in a cell you will collect all the gold in
          that cell. 
        - From your position, you can walk one step to the left, right, up, or
          down. 
        - You can't visit the same cell more than once. 
        - Never visit a cell with 0 gold. 
        - You can start and stop collecting gold from any position in the grid
          that has some gold.

Link: https://leetcode.com/problems/path-with-maximum-gold/
Notes:
    - use dfs with visited or inplace editing of cells
"""
def getMaximumGold(grid: list[list[int]]) -> int:
    R, C = len(grid), len(grid[0])
    dirs = [(0, -1), (-1, 0), (0, 1), (1, 0)]

    def dfs(r: int, c: int) -> int:
        if min(r, c) < 0 or r == R or c == C or grid[r][c] == 0:
            return 0
        cur_value = grid[r][c]
        grid[r][c] = 0
        res = 0
        for x, y in dirs:
            dx, dy = r + x, c + y
            res = max(res, dfs(dx, dy))
        grid[r][c] = cur_value
        res += cur_value
        # print(f'for {(r, c)} = {grid[r][c]}; {res = }')
        return res

    res = 0
    for r in range(R):
        for c in range(C):
            res = max(res, dfs(r, c))
    return res

if __name__ == '__main__':
    g1 = [[0,6,0],[5,8,7],[0,9,0]]
    g2 = [[1,0,7],[2,0,6],[3,4,5],[0,3,0],[9,0,20]]

    print(getMaximumGold(g1))
    print(getMaximumGold(g2))
