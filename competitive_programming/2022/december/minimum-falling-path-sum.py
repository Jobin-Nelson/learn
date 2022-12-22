'''
Created Date: 2022-12-13
Qn: Given an n x n array of integers matrix, return the minimum sum of any
    falling path through matrix.

    A falling path starts at any element in the first row and chooses the
    element in the next row that is either directly below or diagonally
    left/right. Specifically, the next element from position (row, col) will be 
    (row + 1, col - 1), (row + 1, col), or (row + 1, col + 1).
Link: https://leetcode.com/problems/minimum-falling-path-sum/
Notes:
    - use the matrix for memo
'''
def minFallingPathSum(matrix: list[list[int]]) -> int:
    R, C = len(matrix), len(matrix[0])
    if R == 0: return 0
    if R == 1: return matrix[0][0]

    for r in range(1, R):
        for c in range(C):
            if c == 0:
                matrix[r][c] += min(matrix[r-1][c], matrix[r-1][c+1])
            elif c == C-1:
                matrix[r][c] += min(matrix[r-1][c-1], matrix[r-1][c])
            else:
                matrix[r][c] += min(matrix[r-1][c-1], matrix[r-1][c], matrix[r-1][c+1])
    return min(matrix[-1])

if __name__ == '__main__':
    m1 = [[2,1,3],[6,5,4],[7,8,9]]
    m2 = [[-19,57],[-40,-5]]

    print(minFallingPathSum(m1))
    print(minFallingPathSum(m2))

