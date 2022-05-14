'''
Qn: Given an array of intervals intervals where intervals[i] = [starti, endi], return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.
Link: https://leetcode.com/problems/non-overlapping-intervals/
Notes:
- after sorting we need to keep track of the end of each intervals and count the overlapping one's
'''
def erase_overlapping_intervals(intervals):
    intervals.sort(key=lambda x: x[0])
    prev_end = intervals[0][1]
    count = 0

    for start, end in intervals[1:]:
        if prev_end <= start:
            prev_end = end
        else:
            count += 1
            prev_end = min(prev_end, end)
    return count

if __name__ == '__main__':
    i1 = [[1,2],[2,3],[3,4],[1,3]]
    i2 = [[1,2],[1,2],[1,2]]
    i3 = [[1,2],[2,3]]
    print(erase_overlapping_intervals(i1))
    print(erase_overlapping_intervals(i2))
    print(erase_overlapping_intervals(i3))