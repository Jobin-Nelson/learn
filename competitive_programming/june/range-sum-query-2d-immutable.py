'''
Created Date: 03-06-2022
Qn: Given a 2D matrix matrix, handle multiple queries of the following type:
        Calculate the sum of the elements of matrix inside the rectangle defined 
        by its upper left corner (row1, col1) and lower right corner (row2, col2).
Link: https://leetcode.com/problems/range-sum-query-2d-immutable/
Notes:
- store prefix sum and subtract the non-overlapping sums
'''
class NumMatrix:
    def __init__(self, matrix: list[list[int]]):
        row, col = len(matrix), len(matrix[0])
        self.m = [[0]*(col+1) for c in range(row+1)]
        for r in range(row):
            prefix = 0
            for c in range(col):
                prefix += matrix[r][c]
                self.m[r+1][c+1] = prefix + self.m[r][c+1]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        r1, r2, c1, c2 = row1+1, row2+1, col1+1, col2+1
        return self.m[r2][c2] - self.m[r1-1][c2] - self.m[r2][c1-1] + self.m[r1-1][c1-1]

if __name__ == '__main__':
    m = [[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]
    r11, r12, c11, c12 = [2, 1, 4, 3]
    r21, r22, c21, c22 = [1, 1, 2, 2]
    r31, r32, c31, c32 = [1, 2, 2, 4]
    obj = NumMatrix(m)
    print(obj.sumRegion(r11, r12, c11, c12))
    print(obj.sumRegion(r21, r22, c21, c22))
    print(obj.sumRegion(r21, r32, c31, c32))
