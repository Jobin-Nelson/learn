"""
Created Date: 2024-08-09
Qn: A 3 x 3 magic square is a 3 x 3 grid filled with distinct numbers from 1 to
    9 such that each row, column, and both diagonals all have the same sum.

    Given a row x col grid of integers, how many 3 x 3 contiguous magic square
    subgrids are there?

    Note: while a magic square can only contain numbers from 1 to 9, grid may
    contain numbers up to 15.
Link: https://leetcode.com/problems/magic-squares-in-grid/
Notes:
    - use brute force
"""


def numMagicSquaresInside(grid: list[list[int]]) -> int:
    R, C = len(grid), len(grid[0])

    def isMagic(row: int, col: int) -> bool:
        values = [0] * 10
        for r in range(row, row + 3):
            for c in range(col, col + 3):
                value = grid[r][c]
                if not (1 <= value <= 9) or values[value]:
                    return False
                values[value] = 1

        if sum(grid[row + i][col + i] for i in range(3)) != 15:
            return False
        if sum(grid[row + i][col + 2 - i] for i in range(3)) != 15:
            return False
        for c in range(col, col + 3):
            if grid[row][c] + grid[row + 1][c] + grid[row + 2][c] != 15:
                return False
        for r in range(row, row + 3):
            if sum(grid[r][col : col + 3]) != 15:
                return False
        return True

    res = 0
    for r in range(R - 2):
        for c in range(C - 2):
            if isMagic(r, c):
                res += 1
    return res


if __name__ == '__main__':
    g1 = [[4, 3, 8, 4], [9, 5, 1, 9], [2, 7, 6, 2]]
    g2 = [[8]]
    g3 = [[5, 5, 5], [5, 5, 5], [5, 5, 5]]

    print(numMagicSquaresInside(g1))
    print(numMagicSquaresInside(g2))
    print(numMagicSquaresInside(g3))
