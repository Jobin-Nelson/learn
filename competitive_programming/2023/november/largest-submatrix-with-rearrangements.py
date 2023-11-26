'''
Created Date: 2023-11-26
Qn: You are given a binary matrix matrix of size m x n, and you are allowed to
    rearrange the columns of the matrix in any order.

    Return the area of the largest submatrix within matrix where every element
    of the submatrix is 1 after reordering the columns optimally.
Link: https://leetcode.com/problems/largest-submatrix-with-rearrangements/
Notes:
    - store the heights of consecutive one's in each cell
'''
def largestSubmatrix(matrix: list[list[int]]) -> int:
    m, n = len(matrix), len(matrix[0])
    prev_heights = []
    res = 0

    for row in range(m):
        heights = []
        seen = [False] * n
        for height, col in prev_heights:
            if matrix[row][col] == 1:
                heights.append((height+1, col))
                seen[col] = True
        for col in range(n):
            if seen[col] is False and matrix[row][col] == 1:
                heights.append((1, col))
        for i in range(len(heights)):
            res = max(res, heights[i][0] * (i+1))
        prev_heights = heights
    return res

if __name__ == '__main__':
    m1 = [[0,0,1],[1,1,1],[1,0,1]]
    m2 = [[1,0,1,0,1]]
    m3 = [[1,1,0],[1,0,1]]

    print(largestSubmatrix(m1))
    print(largestSubmatrix(m2))
    print(largestSubmatrix(m3))
