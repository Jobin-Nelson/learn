'''
Qn: Given a positive integer n, generate an n x n matrix filled with elements from 1 to n2 in spiral order.
Link: https://leetcode.com/problems/spiral-matrix-ii/
Notes:
- t, b, l, r variables to get the boundary of matrix at each spiral
'''
import pprint

def generate_matrix(n: list[list[int]]) -> list[list[int]]:
    res = [[0]*n for i in range(n)]
    l, r = 0, n
    t, b = 0, n
    
    val = 0
    
    while l < r and t < b:
        for i in range(l, r):
            val += 1
            res[t][i] = val
        t += 1
        for i in range(t, b):
            val += 1
            res[i][r-1] = val
        r -= 1
        for i in range(r-1, l-1, -1):
            val += 1
            res[b-1][i] = val
        b -= 1
        for i in range(b-1, t-1, -1):
            val += 1
            res[i][l] = val
        l += 1
    return res

if __name__ == '__main__':
    n1, n2 = 3, 1
    pp = pprint.PrettyPrinter(width=12)
    pp.pprint(generate_matrix(n1))
    pp.pprint(generate_matrix(n2))