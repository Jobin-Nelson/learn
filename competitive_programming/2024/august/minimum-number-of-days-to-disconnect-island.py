"""
Created Date: 2024-08-11
Qn: You are given an m x n binary grid grid where 1 represents land and 0
    represents water. An island is a maximal 4-directionally (horizontal or
    vertical) connected group of 1's.

    The grid is said to be connected if we have exactly one island, otherwise
    is said disconnected.

    In one day, we are allowed to change any single land cell (1) into a water
    cell (0).

    Return the minimum number of days to disconnect the grid.
Link: https://leetcode.com/problems/minimum-number-of-days-to-disconnect-island/
Notes:
    - there are only three conditions to check
    - if grid is already disconnected, res = 0
    - if grid needs only one swap, res = 1
    - grid atmost needs two swaps, res = 2
"""


def minDays(grid: list[list[int]]) -> int:
    R, C = len(grid), len(grid[0])

    def dfs(r: int, c: int, visit: set[tuple[int, int]]) -> None:
        if not (0 <= r < R) or not (0 <= c < C) or grid[r][c] == 0 or (r, c) in visit:
            return
        visit.add((r, c))
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        for x, y in dirs:
            dfs(r + x, c + y, visit)

    visit = set()
    count = 0

    for r in range(R):
        for c in range(C):
            if grid[r][c] and (r, c) not in visit:
                dfs(r, c, visit)
                count += 1

    if count != 1:
        return 0

    land = list(visit)

    for r, c in land:
        grid[r][c] = 0

        visit = set()
        count = 0
        for r2 in range(R):
            for c2 in range(C):
                if grid[r2][c2] and (r2, c2) not in visit:
                    dfs(r2, c2, visit)
                    count += 1
        if count != 1:
            return 1
        grid[r][c] = 1
    return 2


if __name__ == '__main__':
    g1 = [[0, 1, 1, 0], [0, 1, 1, 0], [0, 0, 0, 0]]
    g2 = [[1, 1]]

    print(minDays(g1))
    print(minDays(g2))
