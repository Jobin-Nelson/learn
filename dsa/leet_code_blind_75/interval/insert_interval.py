'''
Qn: Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).

Return intervals after the insertion.
Link: https://leetcode.com/problems/insert-interval/
Notes: 
- we have to worry about only three cases
- inserting before, after and merging when overlapping
'''

def insert(intervals, newInterval):
    res = []

    i = 0
    while i < len(intervals):
        if newInterval[1] < intervals[i][0]:
            res.append(newInterval)
            return res + intervals[i:]
        elif newInterval[0] > intervals[i][1]:
            res.append(intervals[i])
        else:
            newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]
        i += 1
    res.append(newInterval)
    return res

if __name__ == '__main__':
    intervals1, newInterval1 = [[1,3],[6,9]], [2,5]
    intervals2 , newInterval2 = [[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8]
    print(insert(intervals1, newInterval1))
    print(insert(intervals2, newInterval2))