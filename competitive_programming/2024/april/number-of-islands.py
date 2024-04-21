"""
Created Date: 2024-04-19
Qn: Given an m x n 2D binary grid grid which represents a map of '1's (land)
    and '0's (water), return the number of islands.

    An island is surrounded by water and is formed by connecting adjacent lands
    horizontally or vertically. You may assume all four edges of the grid are
    all surrounded by water.
Link: https://leetcode.com/problems/number-of-islands/
Notes:
    - use dfs
    - use visit hashset or modify grid inplace to mark all land cells as
      visited
"""
def numIslands(grid: list[list[str]]) -> int:
    if not grid: return 0
    R, C = len(grid), len(grid[0])
    dirs = [1, 0, -1, 0, 1]
    def dfs(r: int, c: int) -> None:
        if (0 <= r < R and 0 <= c < C and grid[r][c] == '1'):
            grid[r][c] = '0'
            for i in range(len(dirs)-1):
                dfs(r + dirs[i], c + dirs[i+1])
    res = 0
    for r in range(R):
        for c in range(C):
            if grid[r][c] == '1':
                res += 1
                dfs(r, c)
    return res
            

if __name__ == '__main__':
    g1 = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
    g2 = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
    g3 = [ [ "1", "1", "0", "0", "0" ],
    [ "1", "1", "0", "0", "0" ],
    [ "0", "0", "1", "0", "0" ],
    [ "0", "0", "0", "1", "1" ]
]

    print(numIslands(g1))
    print(numIslands(g2))
    print(numIslands(g3))
