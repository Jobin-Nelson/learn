from collections import defaultdict


def isValidSudoku(board: list[list[str]]) -> bool:
    rows = defaultdict(set)
    cols = defaultdict(set)
    squares = defaultdict(set)

    R, C = len(board), len(board[0])

    for r in range(R):
        for c in range(C):
            digit = board[r][c]
            if digit == '.':
                continue
            if (
                digit in rows[r]
                or digit in cols[c]
                or digit in squares[(r // 3, c // 3)]
            ):
                return False
            rows[r].add(digit)
            cols[c].add(digit)
            squares[(r // 3, c // 3)].add(digit)
    return True


# def isValidSudoku(board: list[list[str]]) -> bool:
#     def hasNineDigits(arr: list[str]) -> bool:
#         l = [0] * 10
#         str_digits = filter(lambda x: x != '.', arr)
#         digits = map(int, str_digits)
#         for d in digits:
#             if l[d] != 0:
#                 return False
#             l[d] = 1
#         return True
#
#     if not all(hasNineDigits(r) for r in board):
#         return False
#     if not all(hasNineDigits(c) for c in zip(*board)):
#         return False
#     if not all(
#         hasNineDigits(
#             [
#                 board[r][c]
#                 for r in range(row_start, row_start + 3)
#                 for c in range(col_start, col_start + 3)
#             ]
#         )
#         for row_start in range(0, 9, 3)
#         for col_start in range(0, 9, 3)
#     ):
#         return False
#     return True


if __name__ == "__main__":
    b1 = [
        ["1", "2", ".", ".", "3", ".", ".", ".", "."],
        ["4", ".", ".", "5", ".", ".", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", ".", "3"],
        ["5", ".", ".", ".", "6", ".", ".", ".", "4"],
        [".", ".", ".", "8", ".", "3", ".", ".", "5"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", ".", ".", ".", ".", ".", "2", ".", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "8"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"],
    ]
    b2 = [
        ["1", "2", ".", ".", "3", ".", ".", ".", "."],
        ["4", ".", ".", "5", ".", ".", ".", ".", "."],
        [".", "9", "1", ".", ".", ".", ".", ".", "3"],
        ["5", ".", ".", ".", "6", ".", ".", ".", "4"],
        [".", ".", ".", "8", ".", "3", ".", ".", "5"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", ".", ".", ".", ".", ".", "2", ".", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "8"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"],
    ]

    print(isValidSudoku(b1))
    print(isValidSudoku(b2))
