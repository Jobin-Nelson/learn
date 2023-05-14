'''
Created Date: 2023-05-09
Qn: Given an m x n matrix, return all elements of the matrix in spiral order.
Link: https://leetcode.com/problems/spiral-matrix/
Notes:
    - declare four variables for top, bottom, left and right
    - after every iterating each edge decrement the necessary variable
'''
def spiralOrder(matrix: list[list[int]]) -> list[int]:
    res = []
    l, r = 0, len(matrix[0])
    t, b = 0, len(matrix)

    while l < r and t < b:
        # Top row
        for i in range(l, r):
            res.append(matrix[t][i])
        t += 1

        # Right col
        for i in range(t, b):
            res.append(matrix[i][r-1])
        r -= 1

        if not (l < r and t < b): break

        # Bottom row
        for i in range(r-1, l-1, -1):
            res.append(matrix[b-1][i])
        b -= 1

        # Left col
        for i in range(b-1, t-1, -1):
            res.append(matrix[i][l])
        l += 1
    return res

if __name__ == '__main__':
    m1 = [[1,2,3],[4,5,6],[7,8,9]]
    m2 = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]

    print(spiralOrder(m1))
    print(spiralOrder(m2))
