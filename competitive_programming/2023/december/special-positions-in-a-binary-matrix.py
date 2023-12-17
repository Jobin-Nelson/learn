"""
Created Date: 2023-12-13
Qn: Given an m x n binary matrix mat, return the number of special positions in
    mat.

    A position (i, j) is called special if mat[i][j] == 1 and all other
    elements in row i and column j are 0 (rows and columns are 0-indexed).
Link: https://leetcode.com/problems/special-positions-in-a-binary-matrix/
Notes:
    - calculate the rowCount and colCount
    - return the number of cells that have rowCount and colCount as 1
"""
def numSpecial(mat: list[list[int]]) -> int:
    m, n = len(mat), len(mat[0])
    res = 0
    rowCount = [0] * m
    colCount = [0] * n
    for i in range(m):
        for j in range(n):
            if mat[i][j] == 1:
                rowCount[i] += 1
                colCount[j] += 1
    for i in range(m):
        for j in range(n):
            if mat[i][j] == 1:
                if rowCount[i] == 1 and colCount[j] == 1:
                    res += 1
    return res

    # for i in range(m):
    #     if sum(mat[i]) != 1: continue
    #     for j in range(n):
    #         if mat[i][j] == 1:
    #             if sum(mat[r][j] for r in range(m)) == 1:
    #                 res += 1
    # return res

if __name__ == '__main__':
    m1 = [[1,0,0],[0,0,1],[1,0,0]]
    m2 = [[1,0,0],[0,1,0],[0,0,1]]

    print(numSpecial(m1))
    print(numSpecial(m2))
