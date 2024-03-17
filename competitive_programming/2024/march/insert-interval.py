"""
Created Date: 2024-03-17
Qn: You are given an array of non-overlapping intervals intervals where
    intervals[i] = [starti, endi] represent the start and the end of the ith
    interval and intervals is sorted in ascending order by starti. You are also
    given an interval newInterval = [start, end] that represents the start and
    end of another interval.

    Insert newInterval into intervals such that intervals is still sorted in
    ascending order by starti and intervals still does not have any overlapping
    intervals (merge overlapping intervals if necessary).

    Return intervals after the insertion.

    Note that you don't need to modify intervals in-place. You can make a new
    array and return it.
Link: https://leetcode.com/problems/insert-interval/
Notes:
    - handle non-overlapping and overlapping scenarios seperately
"""
def insert(intervals: list[list[int]], newInterval: list[int]) -> list[int]:
    res = []
    newStart, newEnd = newInterval

    for i, (start, end) in enumerate(intervals):
        if newEnd < start:
            res.append([newStart, newEnd])
            return res + intervals[i:]
        elif newStart > end:
            res.append([start, end])
        else:
            newStart = min(newStart, start)
            newEnd = max(newEnd, end)
    res.append([newStart, newEnd])
    return res

if __name__ == '__main__':
    i1, n1 = [[1,3],[6,9]], [2,5]
    i2, n2 = [[1,2],[3,5],[6,7],[8,10],[12,16]], [4, 8]

    print(insert(i1, n1))
    print(insert(i2, n2))
