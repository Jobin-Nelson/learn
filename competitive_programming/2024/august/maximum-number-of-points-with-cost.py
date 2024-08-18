"""
Created Date: 2024-08-17
Qn: You are given an m x n integer matrix points (0-indexed). Starting with 0
    points, you want to maximize the number of points you can get from the
    matrix.

    To gain points, you must pick one cell in each row. Picking the cell at
    coordinates (r, c) will add points[r][c] to your score.

    However, you will lose points if you pick a cell too far from the cell that
    you picked in the previous row. For every two adjacent rows r and r + 1
    (where 0 <= r < m - 1), picking cells at coordinates (r, c1) and (r + 1,
    c2) will subtract abs(c1 - c2) from your score.

    Return the maximum number of points you can achieve.

    abs(x) is defined as:

    - x for x >= 0.
    - -x for x < 0.
Link: https://leetcode.com/problems/maximum-number-of-points-with-cost/
Notes:
    - use dynamic programming
    - you only need to look at previous left, centre and right elements
"""


def maxPoints(points: list[list[int]]) -> int:
    R, C = len(points), len(points[0])

    prev_row = points[0]

    for r in range(1, R):
        cur_row = [0] * C
        left = [0] * C
        right = [0] * C

        left[0] = prev_row[0]
        for c in range(1, C):
            left[c] = max(prev_row[c], left[c - 1] - 1)

        right[C - 1] = prev_row[C - 1]
        for c in range(C - 2, -1, -1):
            right[c] = max(prev_row[c], right[c + 1] - 1)

        for c in range(C):
            cur_row[c] = points[r][c] + max(left[c], right[c])
        prev_row = cur_row
    return max(prev_row)


if __name__ == '__main__':
    p1 = [[1, 2, 3], [1, 5, 1], [3, 1, 1]]
    p2 = [[1, 5], [2, 3], [4, 2]]
    p3 = [[1,5],[2,3],[4,2]]

    print(maxPoints(p1))
    print(maxPoints(p2))
    print(maxPoints(p3))
