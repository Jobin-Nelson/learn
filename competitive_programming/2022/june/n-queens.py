'''
Created Date: 04-06-2022
Qn: The n-queens puzzle is the problem of placing n queens on an n x n 
    chessboard such that no two queens attack each other.
    Given an integer n, return all distinct solutions to the n-queens puzzle. 
    You may return the answer in any order.
Link: https://leetcode.com/problems/n-queens/
Notes:
    - backtrack avoiding queens in same in row, col & diagonals
'''
from pprint import pprint
def solveQueens(n: int) -> list[list[int]]:
    col = set()
    posDia = set() # r + c
    negDia = set() # r - c

    res = []
    board = [['.']*n for i in range(n)]

    def backtrack(r):
        if r == n:
            copy = [''.join(row) for row in board]
            res.append(copy)
            return
        for c in range(n):
            if c in col or (r+c) in posDia or (r-c) in negDia:
                continue
            col.add(c)
            posDia.add(r+c)
            negDia.add(r-c)
            board[r][c] = 'Q'

            backtrack(r+1)

            col.remove(c)
            posDia.remove(r+c)
            negDia.remove(r-c)
            board[r][c] = '.'
    backtrack(0)
    return res

if __name__ == '__main__':
    n1, n2 = 4, 1
    pprint(solveQueens(n1))
    pprint(solveQueens(n2))
