'''
Qn: Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.
Link: https://leetcode.com/problems/merge-intervals/
Notes:
- there are only two scenarios to keep in mind
- if the previous end is <= start of current or else
'''
def merge(intervals):
    intervals.sort(key=lambda x: x[0])
    # res = []
    # first = intervals[0]
    
    # for i, interval in enumerate(intervals[1:], 1):
    #     if first[1] < interval[0]:
    #         res.append(first)
    #         first = interval
    #     elif first[0] > interval[1]:
    #         res.append(interval)
    #     else:
    #         first = [min(first[0], interval[0]), max(first[1], interval[1])]
    # return res + [first]

    res = [intervals[0]]

    for start, end in intervals[1:]:
        last_end = res[-1][1]
        if start <= last_end:
            res[-1][1] = max(last_end, end)
        else:
            res.append([start, end])
            
    return res

if __name__ == '__main__':
    intervals1, intervals2 = [[1,3],[2,6],[8,10],[15,18]], [[1,4],[4,5]]
    print(merge(intervals1))
    print(merge(intervals2))

