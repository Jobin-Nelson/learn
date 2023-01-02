'''
Created Date: 2022-12-31
Qn: You are given an m x n integer array grid where grid[i][j] could be:

        - 1 representing the starting square. There is exactly one starting
          square.
        - 2 representing the ending square. There is exactly one ending square.
        - 0 representing empty squares we can walk over.
        - -1 representing obstacles that we cannot walk over.

    Return the number of 4-directional walks from the starting square to the
    ending square, that walk over every non-obstacle square exactly once.
Link: https://leetcode.com/problems/unique-paths-iii/
Notes:
    - use dfs
'''
def uniquePathsIII(grid: list[list[int]]) -> int:
    R, C = range(len(grid)), range(len(grid[0]))

    zeroes = sum(row.count(0) for row in grid)
    start = (0, 0)

    for r in R:
        for c in C:
            if grid[r][c] == 1:
                start = (r, c)
                break
    res = 0
    def dfs(row: int, col: int, zeroes: int) -> None:
        nonlocal res
        grid[row][col] = 3
        for x, y in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            dx, dy = row + x, col + y
            if dx in R and dy in C:
                if grid[dx][dy] == 0: dfs(dx, dy, zeroes-1)
                if grid[dx][dy] == 2 and zeroes == 0: res += 1
        grid[row][col] = 0
        return
    dfs(*start, zeroes)
    return res

if __name__ == '__main__':
    g1 = [[1,0,0,0],[0,0,0,0],[0,0,2,-1]]
    g2 = [[1,0,0,0],[0,0,0,0],[0,0,0,2]]
    g3 = [[0,1],[2,0]]

    print(uniquePathsIII(g1))
    print(uniquePathsIII(g2))
    print(uniquePathsIII(g3))
