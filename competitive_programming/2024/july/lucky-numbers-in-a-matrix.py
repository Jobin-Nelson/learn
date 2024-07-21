"""
Created Date: 2024-07-19
Qn: Given an m x n matrix of distinct numbers, return all lucky numbers in the
    matrix in any order.

    A lucky number is an element of the matrix such that it is the minimum
    element in its row and maximum in its column.
Link: https://leetcode.com/problems/lucky-numbers-in-a-matrix/
Notes:
    - use hashset
"""
from sys import maxsize

def luckyNumbers(matrix: list[list[int]]) -> list[int]:
    R, C  = len(matrix), len(matrix[0])
    min_row = [maxsize] * R
    max_col = [0] * C
    for r in range(R):
        for c in range(C):
            min_row[r] = min(min_row[r], matrix[r][c])
            max_col[c] = max(max_col[c], matrix[r][c])
    return list(set(min_row).intersection(set(max_col)))


if __name__ == '__main__':
    m1 = [[3,7,8],[9,11,13],[15,16,17]]
    m2 = [[1,10,4,2],[9,3,8,7],[15,16,17,12]]
    m3 = [[7,8],[1,2]]

    print(luckyNumbers(m1))
    print(luckyNumbers(m2))
    print(luckyNumbers(m3))
