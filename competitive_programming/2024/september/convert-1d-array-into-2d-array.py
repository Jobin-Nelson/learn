"""
Created Date: 2024-09-01
Qn: You are given a 0-indexed 1-dimensional (1D) integer array original, and
    two integers, m and n. You are tasked with creating a 2-dimensional (2D)
    array with  m rows and n columns using all the elements from original.

    The elements from indices 0 to n - 1 (inclusive) of original should form
    the first row of the constructed 2D array, the elements from indices n to 2
    * n - 1 (inclusive) should form the second row of the constructed 2D array,
    and so on.

    Return an m x n 2D array constructed according to the above procedure, or
    an empty 2D array if it is impossible.
Link: https://leetcode.com/problems/convert-1d-array-into-2d-array/
Notes:
"""


def construct2DArray(original: list[int], m: int, n: int) -> list[list[int]]:
    if len(original) != m * n:
        return []
    return [[original[(r * n) + c] for c in range(n)] for r in range(m)]


if __name__ == '__main__':
    o1, m1, n1 = list(range(1, 5)), 2, 2
    o2, m2, n2 = list(range(1, 4)), 1, 3
    o3, m3, n3 = list(range(1, 3)), 1, 1

    print(construct2DArray(o1, m1, n1))
    print(construct2DArray(o2, m2, n2))
    print(construct2DArray(o3, m3, n3))
