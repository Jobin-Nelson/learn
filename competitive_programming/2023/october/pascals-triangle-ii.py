'''
Created Date: 2023-10-16
Qn: Given an integer rowIndex, return the rowIndexth (0-indexed) row of the
    Pascal's triangle.

    In Pascal's triangle, each number is the sum of the two numbers directly
    above it as shown:
Link: https://leetcode.com/problems/pascals-triangle-ii/
Notes:
    - simulation
'''
from itertools import pairwise, islice

def getRows(rowIndex: int) -> list[int]:
    p = [1]
    for _ in range(rowIndex):
        np = [0] * (len(p)+1)
        for j in range(len(p)):
            np[j] += p[j]
            np[j+1] += p[j]
        p = np
    return p

if __name__ == '__main__':
    r1 = 3
    r2 = 0
    r3 = 1

    print(getRows(r1))
    print(getRows(r2))
    print(getRows(r3))
