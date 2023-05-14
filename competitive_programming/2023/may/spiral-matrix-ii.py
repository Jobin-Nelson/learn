'''
Created Date: 2023-05-10
Qn: Given a positive integer n, generate an n x n matrix filled with elements
    from 1 to n2 in spiral order.
Link: https://leetcode.com/problems/spiral-matrix-ii/
Notes:
    - use four variables l, r, t, b to keep track of the boundaries
    - decrement the boundaries as a you finish each edge of the spiral
'''
def generateMatrix(n: int) -> list[list[int]]:
    res = [[0 for _ in range(n)] for _ in range(n)] 

    num = 1
    l, r = 0, n
    t, b = 0, n

    while l < r and t < b:
        # Top row
        for i in range(l, r):
            res[t][i] = num
            num += 1
        t += 1

        # Right col
        for i in range(t, b):
            res[i][r-1] = num
            num += 1
        r -= 1

        if not (l < r and t < b): break

        # Bottom row
        for i in range(r-1, l-1, -1):
            res[b-1][i] = num
            num += 1
        b -= 1

        # Left col
        for i in range(b-1, t-1, -1):
            res[i][l] = num
            num += 1
        l += 1
    return res

if __name__ == '__main__':
    n1 = 3
    n2 = 1

    print(generateMatrix(n1))
    print(generateMatrix(n2))

    # ~/playground/projects/learn/competitive_programming/2023/may/spiral-matrix-ii.py
