"""
Created Date: 2024-05-12
Qn: You are given an n x n integer matrix grid.

    Generate an integer matrix maxLocal of size (n - 2) x (n - 2) such that:

        - maxLocal[i][j] is equal to the largest value of the 3 x 3 matrix in
          grid centered around row i + 1 and column j + 1.

    In other words, we want to find the largest value in every contiguous 3 x 3
    matrix in grid.

    Return the generated matrix.
Link: https://leetcode.com/problems/largest-local-values-in-a-matrix/
Notes:
    - brute force
"""
def largestLocal(grid: list[list[int]]) -> list[list[int]]:
    N = len(grid)
    n = N - 2
    res = [[0]*n for _ in range(n)]
    dirs = [(-1, -1), (-1, 0), (-1, 1),
            (0, -1), (0, 0), (0, 1),
            (1, -1), (1, 0), (1, 1)]

    for i in range(1, N-1):
        for j in range(1, N-1):
            max_local = 0
            for x, y in dirs:
                dx, dy = i + x, j + y
                max_local = max(max_local, grid[dx][dy])
            res[i-1][j-1] = max_local
    return res

if __name__ == '__main__':
    g1 = [[9,9,8,1],[5,6,2,6],[8,2,6,4],[6,2,2,2]]
    g2 = [[1,1,1,1,1],[1,1,1,1,1],[1,1,2,1,1],[1,1,1,1,1],[1,1,1,1,1]]

    print(largestLocal(g1))
    print(largestLocal(g2))
