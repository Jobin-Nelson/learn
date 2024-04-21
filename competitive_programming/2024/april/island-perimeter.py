"""
Created Date: 2024-04-18
Qn: You are given row x col grid representing a map where grid[i][j] = 1
    represents land and grid[i][j] = 0 represents water.

    Grid cells are connected horizontally/vertically (not diagonally). The grid
    is completely surrounded by water, and there is exactly one island (i.e.,
    one or more connected land cells).

    The island doesn't have "lakes", meaning the water inside isn't connected
    to the water around the island. One cell is a square with side length 1.
    The grid is rectangular, width and height don't exceed 100. Determine the
    perimeter of the island.
Link: https://leetcode.com/problems/island-perimeter/
Notes:
    - use dfs
"""
def islandPerimeter(grid: list[list[int]]) -> int:
    visited = set()
    R, C = len(grid), len(grid[0])
    def dfs(r: int, c: int) -> int:
        if r >= R or c >= C or r < 0 or c < 0 or grid[r][c] == 0:
            return 1
        if (r, c) in visited:
            return 0
        visited.add((r, c))

        perim = dfs(r, c + 1)
        perim += dfs(r, c - 1)
        perim += dfs(r + 1, c)
        perim += dfs(r - 1, c)
        return perim

    for r in range(R):
        for c in range(C):
            if grid[r][c] == 1:
                return dfs(r, c)
    return 0


if __name__ == '__main__':
    g1 = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
    g2 = [[1]]
    g3 = [[1,0]]

    print(islandPerimeter(g1))
    print(islandPerimeter(g2))
    print(islandPerimeter(g3))

