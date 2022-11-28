'''
Created Date: 2022-10-31
Qn: Given an m x n matrix, return true if the matrix is Toeplitz. Otherwise,
    return false.

    A matrix is Toeplitz if every diagonal from top-left to bottom-right has
    the same elements.
Link: https://leetcode.com/problems/toeplitz-matrix/
Notes:
    - check diagonals from bottom left to top left
    - check diagonals from top left to top right
'''
def isToeplitzMatrix(matrix: list[list[int]]) -> bool:
    m, n = len(matrix), len(matrix[0])

    def check_diagonal(i, j):
        val = matrix[i][j]
        while i < m and j < n:
            if matrix[i][j] != val: return False
            i += 1
            j += 1
        return True

    for c in range(n):
        if not check_diagonal(0, c): return False

    for r in range(m):
        if not check_diagonal(r, 0): return False

    return True

if __name__ == '__main__':
    m1 = [[1,2,3,4],[5,1,2,3],[9,5,1,2]]
    m2 = [[1,2],[2,2]]

    print(isToeplitzMatrix(m1))
    print(isToeplitzMatrix(m2))
