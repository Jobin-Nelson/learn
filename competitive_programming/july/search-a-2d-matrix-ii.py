'''
Created Date: 24-07-2022
Qn: Write an efficient algorithm that searches for a value target in an m x n
    integer matrix matrix. This matrix has the following properties: 
    - Integers in each row are sorted in ascending from left to right.
    - Integers in each column are sorted in ascending from top to bottom.
Link: https://leetcode.com/problems/search-a-2d-matrix-ii/
Notes:
- check values from left bottom [m][0] 
'''
def searchMatrix(matrix: list[list[int]], target: int) -> bool:
    m, n = len(matrix), len(matrix[0])

    r, c = m - 1, 0

    while r >= 0 and c < m:
        if matrix[r][c] == target:
            return True
        elif matrix[r][c] < target:
            c += 1
        else:
            r -= 1
    return False

if __name__ == '__main__':
    m1, t1  = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], 5
    m2, t2 = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], 20
    print(searchMatrix(m1, t1))
    print(searchMatrix(m2, t2))
