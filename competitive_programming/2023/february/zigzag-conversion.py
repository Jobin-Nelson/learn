'''
Created Date: 2023-02-03
Qn: The string "PAYPALISHIRING" is written in a zigzag pattern on a given
    number of rows like this: (you may want to display this pattern in a 
    fixed font for better legibility)
Link: https://leetcode.com/problems/zigzag-conversion/
Notes:
    - use 2d array to simulate zigzag behaviour
    - figure out the dimensions
    - move down
    - move up right
    - concat by row
'''
import math

def convert(s: str, num_rows: int) -> str:
    if num_rows == 1: return s

    n = len(s)
    sections = math.ceil(n / (2 * num_rows - 2.0))
    num_cols = sections * (num_rows - 1)

    matrix = [[' '] * num_cols for _ in range(num_rows)]

    cur_row, cur_col = 0, 0
    cur_string_index = 0

    while cur_string_index < n:
        # move down
        while cur_row < num_rows and cur_string_index < n:
            matrix[cur_row][cur_col] = s[cur_string_index]
            cur_row += 1
            cur_string_index += 1

        cur_row -= 2
        cur_col += 1

        # move up right
        while cur_row > 0 and cur_col < num_cols and cur_string_index < n:
            matrix[cur_row][cur_col] = s[cur_string_index]
            cur_row -= 1
            cur_col += 1
            cur_string_index += 1
    res = ''

    for row in matrix:
        res += ''.join(row)
    return res.replace(' ', '')

if __name__ == '__main__':
    s1, n1 = "PAYPALISHIRING", 3
    s2, n2 = "PAYPALISHIRING", 4
    s3, n3 = "A", 1

    print(convert(s1, n1))
    print(convert(s2, n2))
    print(convert(s3, n3))
