'''
Created Date: 2022-11-23
Qn: Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to
    be validated according to the following rules:

        - Each row must contain the digits 1-9 without repetition. 
        - Each column must contain the digits 1-9 without repetition. 
        - Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition. 

    Note:

        - A Sudoku board (partially filled) could be valid but is not
          necessarily solvable. 
        - Only the filled cells need to be validated according to the mentioned
          rules.
Link: https://leetcode.com/problems/valid-sudoku/
Notes:
    - maintain three sets to check row, col and squares
'''
from collections import defaultdict

def isValidSudoku(board: list[list[str]]) -> bool:
    cols = defaultdict(set)
    rows = defaultdict(set)
    squares = defaultdict(set)

    for r in range(9):
        for c in range(9):
            val = board[r][c]
            if val == '.': continue
            if val in rows[r] or val in cols[c] or val in squares[r//3, c//3]:
                return False
            rows[r].add(val)
            cols[c].add(val)
            squares[r//3, c//3].add(val)
    return True

if __name__ == '__main__':
    b1 = [["5","3",".",".","7",".",".",".","."]
          ,["6",".",".","1","9","5",".",".","."]
          ,[".","9","8",".",".",".",".","6","."]
          ,["8",".",".",".","6",".",".",".","3"]
          ,["4",".",".","8",".","3",".",".","1"]
          ,["7",".",".",".","2",".",".",".","6"]
          ,[".","6",".",".",".",".","2","8","."]
          ,[".",".",".","4","1","9",".",".","5"]
          ,[".",".",".",".","8",".",".","7","9"]]
    b2 = [["8","3",".",".","7",".",".",".","."]
          ,["6",".",".","1","9","5",".",".","."]
          ,[".","9","8",".",".",".",".","6","."]
          ,["8",".",".",".","6",".",".",".","3"]
          ,["4",".",".","8",".","3",".",".","1"]
          ,["7",".",".",".","2",".",".",".","6"]
          ,[".","6",".",".",".",".","2","8","."]
          ,[".",".",".","4","1","9",".",".","5"]
          ,[".",".",".",".","8",".",".","7","9"]]

    print(isValidSudoku(b1))
    print(isValidSudoku(b2))
