'''
Created Date: 2023-07-19
Qn: Given an array of intervals intervals where intervals[i] = [starti, endi],
    return the minimum number of intervals you need to remove to make the rest
    of the intervals non-overlapping.
Link: https://leetcode.com/problems/non-overlapping-intervals/
Notes:
    - sort the intervals with key as end values
    - update k to cur_end, when the start times are greater than k
    - else increment res
'''
def eraseOverlapIntervals(intervals: list[list[int]]) -> int:
    intervals.sort(key=lambda x: x[1])
    k, res = -1e9, 0
    for x, y in intervals:
        if x >= k: k = y
        else: res += 1
    return res
    # dfs approach
    # N = len(intervals)
    # def dfs(cur_ind: int, prev_end: int) -> int:
    #     if cur_ind == N: return 0
    #     if intervals[cur_ind][0] < prev_end: return dfs(cur_ind + 1, max(intervals[cur_ind][1], prev_end)) + 1
    #     return dfs(cur_ind + 1, intervals[cur_ind][1])
    # return dfs(0, -1)

if __name__ == '__main__':
    i1 = [[1,2],[2,3],[3,4],[1,3]]
    i2 = [[1,2],[1,2],[1,2]]
    i3 = [[1,2],[2,3]]

    print(eraseOverlapIntervals(i1))
    print(eraseOverlapIntervals(i2))
    print(eraseOverlapIntervals(i3))
