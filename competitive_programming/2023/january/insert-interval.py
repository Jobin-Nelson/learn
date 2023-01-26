'''
Created Date: 2023-01-16
Qn: You are given an array of non-overlapping intervals intervals where
    intervals[i] = [starti, endi] represent the start and the end of the ith
    interval and intervals is sorted in ascending order by starti. You are also
    given an interval newInterval = [start, end] that represents the start and
    end of another interval.

    Insert newInterval into intervals such that intervals is still sorted in
    ascending order by starti and intervals still does not have any overlapping
    intervals (merge overlapping intervals if necessary).

    Return intervals after the insertion.
Link: https://leetcode.com/problems/insert-interval/
Notes:
    - use stack and append new intervals
    - if overlapping change the new interval values with min of start and max
      of end
'''
def insert(intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
    res = []

    for i in range(len(intervals)):
        if newInterval[1] < intervals[i][0]:
            res.append(newInterval)
            return res + intervals[i:]
        elif newInterval[0] > intervals[i][1]:
            res.append(intervals[i])
        else:
            newInterval = [min(intervals[i][0], newInterval[0]), max(intervals[i][1], newInterval[1])]
    res.append(newInterval)
    return res

if __name__ == '__main__':
    i1, n1 = [[1,3],[6,9]], [2,5]
    i2, n2 = [[1,2],[3,5],[6,7],[8,10],[12,16]], [4, 8]
    
    print(insert(i1, n1))
    print(insert(i2, n2))
