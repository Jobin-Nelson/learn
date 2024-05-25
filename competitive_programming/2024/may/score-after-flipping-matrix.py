"""
Created Date: 2024-05-13
Qn: You are given an m x n binary matrix grid.

    A move consists of choosing any row or column and toggling each value in
    that row or column (i.e., changing all 0's to 1's, and all 1's to 0's).

    Every row of the matrix is interpreted as a binary number, and the score of
    the matrix is the sum of these numbers.

    Return the highest possible score after making any number of moves
    (including zero moves).


Link: https://leetcode.com/problems/score-after-flipping-matrix/
Notes:
"""
def matrixScore(grid: list[list[int]]) -> int:
    R, C = len(grid), len(grid[0])
    col_sum = [0] * C
    for r in range(R):
        flip = grid[r][0] == 0
        for c in range(C):
            if flip: grid[r][c] ^= 1
            col_sum[c] += grid[r][c]

    total_sum = 0 
    for c in range(C):
        flip = col_sum[c] < (R - col_sum[c])
        for r in range(R):
            if flip: grid[r][c] ^= 1
            if grid[r][c] == 1:
                total_sum += (1 << (C-c-1))
    return total_sum

if __name__ == '__main__':
    g1 = [[0,0,1,1],[1,0,1,0],[1,1,0,0]]
    g2 = [[0]]

    print(matrixScore(g1))
    print(matrixScore(g2))
