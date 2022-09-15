'''
Created Date: 2022-08-28
Qn: A matrix diagonal is a diagonal line of cells starting from some cell in
    either the topmost row or leftmost column and going in the bottom-right
    direction until reaching the matrix's end. For example, the matrix diagonal
    starting from mat[2][0], where mat is a 6 x 3 matrix, includes cells mat[2][0],
    mat[3][1], and mat[4][2].

    Given an m x n matrix mat of integers, sort each matrix diagonal in ascending
    order and return the resulting matrix.
Link: https://leetcode.com/problems/sort-the-matrix-diagonally/
Notes:
    - Only thing that's consistent across diagonals are r - c
    - we can use them as keys to store the diagonals in a list
    - and while iterating over the matrix popping off the heap 
    - so that you'll get the min value for that particular diagonal
'''
from collections import defaultdict
from heapq import heappush, heappop
from pprint import pprint

def diagonalSort(mat: list[list[int]]) -> list[list[int]]:
    R, C = len(mat), len(mat[0])
    new_mat = defaultdict(list)

    for r in range(R):
        for c in range(C):
            heappush(new_mat[r-c], mat[r][c])

    for r in range(R):
        for c in range(C):
            mat[r][c] = heappop(new_mat[r-c])
    return mat

if __name__ == '__main__':
    m1 = [[3,3,1,1],[2,2,1,2],[1,1,1,2]]
    m2 = [
        [11,25,66,1,69,7],
        [23,55,17,45,15,52],
        [75,31,36,44,58,8],
        [22,27,33,25,68,4],
        [84,28,14,11,5,50]
        ]
    m3 = [
        [3, 3, 1, 1],
        [2, 2, 1, 2],
        [1, 1, 1, 2],
        ]

    pprint(diagonalSort(m1))
    pprint(diagonalSort(m2))
    pprint(diagonalSort(m3))
