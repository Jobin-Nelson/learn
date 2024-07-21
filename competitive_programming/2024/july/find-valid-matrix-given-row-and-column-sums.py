"""
Created Date: 2024-07-20
Qn: You are given two arrays rowSum and colSum of non-negative integers where
    rowSum[i] is the sum of the elements in the ith row and colSum[j] is the
    sum of the elements of the jth column of a 2D matrix. In other words, you
    do not know the elements of the matrix, but you do know the sums of each
    row and column.

    Find any matrix of non-negative integers of size rowSum.length x
    colSum.length that satisfies the rowSum and colSum requirements.

    Return a 2D array representing any matrix that fulfills the requirements.
    It's guaranteed that at least one matrix that fulfills the requirements
    exists.
Link: https://leetcode.com/problems/find-valid-matrix-given-row-and-column-sums/
Notes:
    - populate each cell with min of rowSum and colSum
    - at each iteration one of them will be 0 because of taking the min between
      them
"""
def restoreMatrix(rowSum: list[int], colSum: list[int]) -> list[list[int]]:
    M, N = len(colSum), len(rowSum)

    matrix = [[0]* M for _ in range(N)]

    i, j = 0, 0

    while i < N and j < M:
        matrix[i][j] = min(rowSum[i], colSum[j])
        rowSum[i] -= matrix[i][j]
        colSum[j] -= matrix[i][j]
        if rowSum[i] == 0:
            i += 1
        else:
            j += 1
    return matrix

if __name__ == '__main__':
    r1, c1 = [3,8], [4,7]
    r2, c2 = [5,7,10], [8,6,8]

    print(restoreMatrix(r1, c1))
    print(restoreMatrix(r2, c2))
