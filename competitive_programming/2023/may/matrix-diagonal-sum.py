'''
Created Date: 2023-05-08
Qn: Given a square matrix mat, return the sum of the matrix diagonals.

    Only include the sum of all the elements on the primary diagonal and all
    the elements on the secondary diagonal that are not part of the primary
    diagonal.
Link: https://leetcode.com/problems/matrix-diagonal-sum/
Notes:
    - use sum diagonal
    - if len of mat is odd decrement the middle value
'''
def diagonalSum(mat: list[list[int]]) -> int:
    n = len(mat)
    res = 0
    for i in range(n):
        res += mat[i][i] + mat[i][n-i-1]

    if n & 1 == 1:
        res -= mat[n//2][n//2]
    return res

if __name__ == '__main__':
    m1 = [[1,2,3],
          [4,5,6],
          [7,8,9]]
    m2 = [[1,1,1,1],
          [1,1,1,1],
          [1,1,1,1],
          [1,1,1,1]]
    m3 = [[5]]

    print(diagonalSum(m1))
    print(diagonalSum(m2))
    print(diagonalSum(m3))
