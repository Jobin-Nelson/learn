"""
Created Date: 2024-01-28
Qn: Given a matrix and a target, return the number of non-empty submatrices
    that sum to target.

    A submatrix x1, y1, x2, y2 is the set of all cells matrix[x][y] with x1 <=
    x <= x2 and y1 <= y <= y2.

    Two submatrices (x1, y1, x2, y2) and (x1', y1', x2', y2') are different if
    they have some coordinate that is different: for example, if x1 != x1'.
Link: https://leetcode.com/problems/number-of-submatrices-that-sum-to-target/
Notes:
    - use prefix sum and hashmap to pre-process sums for easy target calculation
"""
from collections import defaultdict

def numSubmatrixSumTarget(matrix: list[list[int]], target: int) -> int:
    M, N = len(matrix), len(matrix[0])
    sub_sum = [[0] * N for _ in range(M)]

    for r in range(M):
        for c in range(N):
            top = sub_sum[r-1][c] if r > 0 else 0
            left = sub_sum[r][c-1] if c > 0 else 0
            top_left = sub_sum[r-1][c-1] if min(r, c) > 0 else 0
            sub_sum[r][c] = matrix[r][c] + top + left - top_left

    res = 0
    for r1 in range(M):
        for r2 in range(r1, M):
            count = defaultdict(int)
            count[0] = 1
            for c in range(N):
                cur_sum = sub_sum[r2][c] - (sub_sum[r1-1][c] if r1 > 0 else 0)
                diff = cur_sum - target
                res += count[diff]
                count[cur_sum] += 1
    return res

if __name__ == '__main__':
    m1, t1 = [[0,1,0],[1,1,1],[0,1,0]], 0
    m2, t2 = [[1,-1],[-1,1]], 0
    m3, t3 = [[904]], 0

    print(numSubmatrixSumTarget(m1, t1))
    print(numSubmatrixSumTarget(m2, t2))
    print(numSubmatrixSumTarget(m3, t3))
