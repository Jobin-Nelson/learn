#!/usr/bin/env python3
'''This program solves cracks sudoku puzzle for you'''

from pprint import pprint

def main():
    grid = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
            [6, 0, 0, 1, 9, 5, 0, 0, 0],
            [0, 9, 8, 0, 0, 0, 0, 6, 0],
            [8, 0, 0, 0, 6, 0, 0, 0, 3],
            [4, 0, 0, 8, 0, 3, 0, 0, 1],
            [7, 0, 0, 0, 2, 0, 0, 0, 6],
            [0, 6, 0, 0, 0, 0, 2, 8, 0],
            [0, 0, 0, 4, 1, 9, 0, 0, 5],
            [0, 0, 0, 0, 8, 0, 0, 7, 9]]

    solve(grid)
    return 0

def solve(board: list[list[int]]) -> None:

    for y in range(9):
        for x in range(9):
            if board[y][x] == 0:
                for n in range(1, 10):
                    if possible(board, y, x, n):
                        board[y][x] = n
                        solve(board)
                        board[y][x] = 0
                return 
    pprint(board)
    input("More?")
    return

def possible(board: list[list[int]], y: int, x: int, n: int) -> bool:
    for i in range(9):
        if board[y][i] == n or board[i][x] == n:
            return False

    x0 = (x // 3) * 3
    y0 = (y // 3) * 3

    for i in range(3):
        for j in range(3):
            if board[y0+i][x0+j] == n:
                return False
    return True

if __name__ == '__main__':
    raise SystemExit(main())
