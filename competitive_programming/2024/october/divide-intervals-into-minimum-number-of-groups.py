"""
Created Date: 2024-10-12
Qn: You are given a 2D integer array intervals where intervals[i] = [lefti,
    righti] represents the inclusive interval [lefti, righti].

    You have to divide the intervals into one or more groups such that each
    interval is in exactly one group, and no two intervals that are in the same
    group intersect each other.

    Return the minimum number of groups you need to make.

    Two intervals intersect if there is at least one common number between
    them. For example, the intervals [1, 5] and [5, 8] intersect.
Link: https://leetcode.com/problems/divide-intervals-into-minimum-number-of-groups/
Notes:
    - count the number of intersection at any given time
"""


def minGroups(intervals: list[list[int]]) -> int:
    start, end = [], []
    for s, e in intervals:
        start.append(s)
        end.append(e)
    start.sort()
    end.sort()
    i, j = 0, 0
    res = 0
    while i < len(intervals):
        if start[i] <= end[j]:
            i += 1
        else:
            j += 1
        res = max(res, i - j)
    return res


if __name__ == '__main__':
    i1 = [[5, 10], [6, 8], [1, 5], [2, 3], [1, 10]]
    i2 = [[1, 3], [5, 6], [8, 10], [11, 13]]

    print(minGroups(i1))
    print(minGroups(i2))
