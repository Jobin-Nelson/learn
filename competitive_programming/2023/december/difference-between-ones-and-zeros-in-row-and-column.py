"""
Created Date: 2023-12-14
Qn: You are given a 0-indexed m x n binary matrix grid.

    A 0-indexed m x n difference matrix diff is created with the following procedure:

        - Let the number of ones in the ith row be onesRowi.
        - Let the number of ones in the jth column be onesColj.
        - Let the number of zeros in the ith row be zerosRowi.
        - Let the number of zeros in the jth column be zerosColj.
        - diff[i][j] = onesRowi + onesColj - zerosRowi - zerosColj

    Return the difference matrix diff.
Link: https://leetcode.com/problems/difference-between-ones-and-zeros-in-row-and-column/
Notes:
    - use a rowCount and colCount to get the number of ones in each row and col
    - diff = 2 * onesCount - number of elements
"""
from itertools import product

def onesMinusZeros(grid: list[list[int]]) -> list[list[int]]:
    M, N = len(grid), len(grid[0])
    def count(arr: list[int]) -> int: return 2*sum(arr) - len(arr)
    onesRow = list(map(count, zip(*grid)))
    onesCol = list(map(count, grid))
    # return [[onesRow[j] + onesCol[i] for j in range(N)] for i in range(M)]
    for i, j in product(range(M), range(N)):
        grid[i][j] = onesRow[j] + onesCol[i]
    return grid
    # M, N = len(grid), len(grid[0])
    # onesRow = [0] * N
    # onesCol = [0] * M
    #
    # for i in range(M):
    #     for j in range(N):
    #         if grid[i][j] == 1:
    #             onesRow[j] += 1
    #             onesCol[i] += 1
    # diff = [[0] * N for _ in range(M)]
    # for i in range(M):
    #     for j in range(N):
    #         diff[i][j] = (2 * onesRow[j]) + (2 * onesCol[i]) - M - N
    # return diff

if __name__ == '__main__':
    g1 = [[0,1,1],[1,0,1],[0,0,1]]
    g2 = [[1,1,1],[1,1,1]]

    print(onesMinusZeros(g1))
    print(onesMinusZeros(g2))
