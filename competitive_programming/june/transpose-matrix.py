'''
Created Date: 02-06-2022
Qn: Given a 2D integer array matrix, return the transpose of matrix.
    The transpose of a matrix is the matrix flipped over its main diagonal, 
    switching the matrix's row and column indices.
Link: https://leetcode.com/problems/transpose-matrix/
Notes:
- create a new matrix with n x m size
- reverse row and col indices to tranpose the matrix
'''
from pprint import pprint

def transpose(matrix: list[list[int]]) -> list[list[int]]:
    row, col = len(matrix), len(matrix[0])
    res = [[0 for r in range(row)] for c in range(col)]
    for r in range(row):
        for c in range(col):
            res[c][r] = matrix[r][c]
    return res

if __name__ == '__main__':
    m1 = [[1,2,3],[4,5,6],[7,8,9]]
    m2 = [[1,2,3],[4,5,6]]
    pprint(transpose(m1))
    pprint(transpose(m2))
