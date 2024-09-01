"""
Created Date: 2024-08-28
Qn: You are given two m x n binary matrices grid1 and grid2 containing only 0's
    (representing water) and 1's (representing land). An island is a group of
    1's connected 4-directionally (horizontal or vertical). Any cells outside
    of the grid are considered water cells.

    An island in grid2 is considered a sub-island if there is an island in
    grid1 that contains all the cells that make up this island in grid2.

    Return the number of islands in grid2 that are considered sub-islands.
Link: https://leetcode.com/problems/count-sub-islands/
Notes:
    - use dfs
"""


def countSubIslands(grid1: list[list[int]], grid2: list[list[int]]) -> int:
    R, C = len(grid2), len(grid2[0])
    dirs = [0, 1, 0, -1, 0]

    def is_sub_island(r: int, c: int) -> bool:
        if r < 0 or r >= R or c < 0 or c >= C or grid2[r][c] == 0:
            return True

        grid2[r][c] = 0
        res = True
        if grid1[r][c] == 0:
            res = False

        for i in range(len(dirs) - 1):
            res = is_sub_island(r + dirs[i], c + dirs[i + 1]) and res
        return res

    res = 0
    for r in range(R):
        for c in range(C):
            if grid2[r][c] == 0 or grid1[r][c] == 0:
                continue
            if is_sub_island(r, c):
                res += 1
    return res


if __name__ == '__main__':
    g11, g12 = [
        [1, 1, 1, 0, 0],
        [0, 1, 1, 1, 1],
        [0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0],
        [1, 1, 0, 1, 1],
    ], [
        [1, 1, 1, 0, 0],
        [0, 0, 1, 1, 1],
        [0, 1, 0, 0, 0],
        [1, 0, 1, 1, 0],
        [0, 1, 0, 1, 0],
    ]
    g21, g22 = [
        [1, 0, 1, 0, 1],
        [1, 1, 1, 1, 1],
        [0, 0, 0, 0, 0],
        [1, 1, 1, 1, 1],
        [1, 0, 1, 0, 1],
    ], [
        [0, 0, 0, 0, 0],
        [1, 1, 1, 1, 1],
        [0, 1, 0, 1, 0],
        [0, 1, 0, 1, 0],
        [1, 0, 0, 0, 1],
    ]

    print(countSubIslands(g11, g12))
    print(countSubIslands(g21, g22))
