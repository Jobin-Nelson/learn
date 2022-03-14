'''
Qn: Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.
You must do it in place.
Link: https://leetcode.com/problems/set-matrix-zeroes/
Notes:
- set zero of first row and col since we already passed them
- a variable to store the overlapping index[0][0]
- set matrix to zero based on first row and col
'''

def set_zeroes(matrix):
    rows, cols = len(matrix), len(matrix[0])
    row_zero = False

    # setting zero to first row and col
    for r in range(rows):
        for c in range(cols):
            if matrix[r][c] == 0:
                matrix[0][c] = 0
                if r > 0:
                    matrix[r][0] = 0
                else:
                    row_zero = True # special case for overlapping index
    
    # setting matrix zero based on first row and col
    for r in range(1, rows):
        for c in range(1, cols):
            if matrix[0][c] == 0 or matrix[r][0] == 0:
                matrix[r][c] = 0

    if matrix[0][0] == 0:
        for r in range(rows):
            matrix[r][0] = 0

    if row_zero == 0:
        for c in range(cols):
            matrix[0][c] = 0

    

if __name__ == '__main__':
    m1 = [[1,1,1],[1,0,1],[1,1,1]]
    m2 = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
    set_zeroes(m1)
    set_zeroes(m2)
    print(m1)
    print(m2)
