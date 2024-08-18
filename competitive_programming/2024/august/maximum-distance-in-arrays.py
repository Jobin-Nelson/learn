"""
Created Date: 2024-08-16
Qn: You are given m arrays, where each array is sorted in ascending order.

    You can pick up two integers from two different arrays (each array picks
    one) and calculate the distance. We define the distance between two
    integers a and b to be their absolute difference |a - b|.

    Return the maximum distance.
Link: https://leetcode.com/problems/maximum-distance-in-arrays/
Notes:
    - use one pass and keep track of current
"""


def maxDistance(arrays: list[list[int]]) -> int:
    min_total, max_total = arrays[0][0], arrays[0][-1]
    res = 0
    for arr in arrays[1:]:
        min_cur, max_cur = arr[0], arr[-1]
        res = max(res, max_cur - min_total, max_total - min_cur)
        min_total = min(min_total, min_cur)
        max_total = max(max_total, max_cur)
    return res


if __name__ == '__main__':
    a1 = [[1, 2, 3], [4, 5], [1, 2, 3]]
    a2 = [[1], [1]]
    a3 = [[1, 4], [0, 5]]

    print(maxDistance(a1))
    print(maxDistance(a2))
    print(maxDistance(a3))
