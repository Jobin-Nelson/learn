"""
Created Date: 2023-12-10
Qn: Given a 2D integer array matrix, return the transpose of matrix.

    The transpose of a matrix is the matrix flipped over its main diagonal,
    switching the matrix's row and column indices.
Link: https://leetcode.com/problems/transpose-matrix/
Notes:
    - use zip
    - or build a new matrix
"""
def transpose(matrix: list[list[int]]) -> list[list[int]]:
    R, C = len(matrix), len(matrix[0])
    res = [[0] * R for _ in range(C)]
    for r in range(R):
        for c in range(C):
            res[c][r] = matrix[r][c]
    return res
    # return list(zip(*matrix))

if __name__ == '__main__':
    m1 = [[1,2,3],[4,5,6],[7,8,9]]
    m2 = [[1,2,3],[4,5,6]]

    print(transpose(m1))
    print(transpose(m2))
