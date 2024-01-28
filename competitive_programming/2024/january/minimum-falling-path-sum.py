"""
Created Date: 2024-01-19
Qn: Given an n x n array of integers matrix, return the minimum sum of any
    falling path through matrix.

    A falling path starts at any element in the first row and chooses the
    element in the next row that is either directly below or diagonally
    left/right. Specifically, the next element from position (row, col) will be
    (row + 1, col - 1), (row + 1, col), or (row + 1, col + 1).
Link: https://leetcode.com/problems/minimum-falling-path-sum/
Notes:
    - use simulation
"""
def minFallingPathSum(matrix: list[list[int]]) -> int:
    n = len(matrix)
    prev = matrix[0]

    for i in range(1, n):
        cur = matrix[i]
        for j in range(n):
            l, r = 0 if j-1 < 0 else j-1, n-1 if j+1 >= n else j+1
            cur[j] += min(prev[l], prev[j], prev[r])
        prev = cur
    return min(prev)

if __name__ == '__main__':
    m1 = [[2,1,3],[6,5,4],[7,8,9]]
    m2 = [[-19,57],[-40,-5]]

    print(minFallingPathSum(m1))
    print(minFallingPathSum(m2))
