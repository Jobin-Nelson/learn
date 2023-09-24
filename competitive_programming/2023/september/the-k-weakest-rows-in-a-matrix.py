'''
Created Date: 2023-09-18
Qn: You are given an m x n binary matrix mat of 1's (representing soldiers) and
    0's (representing civilians). The soldiers are positioned in front of the
    civilians. That is, all the 1's will appear to the left of all the 0's in
    each row.

    A row i is weaker than a row j if one of the following is true:

        - The number of soldiers in row i is less than the number of soldiers
          in row j. 
        - Both rows have the same number of soldiers and i < j.

    Return the indices of the k weakest rows in the matrix ordered from weakest
    to strongest.
Link: https://leetcode.com/problems/the-k-weakest-rows-in-a-matrix/
Notes:
    - use tuple with count of 1's and index and sort
'''
def kWeakestRows(mat: list[list[int]], k: int) -> list[int]:
    res = [(sum(m), i) for i, m in enumerate(mat)]
    return [r[1] for r in sorted(res)[:k]]


if __name__ == '__main__':
    m1, k1 = [[1,1,0,0,0],
 [1,1,1,1,0],
 [1,0,0,0,0],
 [1,1,0,0,0],
 [1,1,1,1,1]], 3

    m2, k2 = [[1,0,0,0],
 [1,1,1,1],
 [1,0,0,0],
 [1,0,0,0]], 2

    print(kWeakestRows(m1, k1))
    print(kWeakestRows(m2, k2))
