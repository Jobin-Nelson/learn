"""
Created Date: 2024-08-08
Qn: You start at the cell (rStart, cStart) of an rows x cols grid facing east.
    The northwest corner is at the first row and column in the grid, and the
    southeast corner is at the last row and column.

    You will walk in a clockwise spiral shape to visit every position in this
    grid. Whenever you move outside the grid's boundary, we continue our walk
    outside the grid (but may return to the grid boundary later.). Eventually,
    we reach all rows * cols spaces of the grid.

    Return an array of coordinates representing the positions of the grid in
    the order you visited them.
Link: https://leetcode.com/problems/spiral-matrix-iii/
Notes:
    - use simulation
"""


def spiralMatrixIII(rows: int, cols: int, rStart: int, cStart: int) -> list[list[int]]:
    dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    traversed = [[rStart, cStart]]

    step = 1
    direction = 0

    while len(traversed) < rows * cols:
        for _ in range(2):
            for _ in range(step):
                r, c = dirs[direction]
                rStart += r
                cStart += c
                if 0 <= rStart < rows and 0 <= cStart < cols:
                    traversed.append([rStart, cStart])
            direction = (direction + 1) % 4
        step += 1
    return traversed


if __name__ == '__main__':
    r1, c1, rs1, cs1 = 1, 4, 0, 0
    r2, c2, rs2, cs2 = 5, 6, 1, 4

    print(spiralMatrixIII(r1, c1, rs1, cs1))
    print(spiralMatrixIII(r2, c2, rs2, cs2))
