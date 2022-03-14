'''
Qn: Given an m x n matrix, return all elements of the matrix in a spiral order
Link: https://leetcode.com/problems/spiral-matrix/
Notes:
- traverse around the borders of the matrix, appending to the result till you run out of the border
'''

def spiral_order(matrix):
    l, r = 0, len(matrix[0])
    t, b = 0, len(matrix)
    res = []

    while l < r and t < b:
        # top row
        for i in range(l, r):
            res.append(matrix[t][i])
        t += 1

        # right col
        for i in range(t, b):
            res.append(matrix[i][r-1])
        r -= 1

        if not (l < r and t < b):
            break

        # bottom row
        for i in range(r-1, l-1, -1):
            res.append(matrix[b-1][i])
        b -= 1

        # left col
        for i in range(b-1, t-1, -1):
            res.append(matrix[i][l])
        l += 1
    return res

    
if __name__ == '__main__':
    i1, i2 = [[1,2,3],[4,5,6],[7,8,9]], [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
    print(spiral_order(i1))
    print(spiral_order(i2))