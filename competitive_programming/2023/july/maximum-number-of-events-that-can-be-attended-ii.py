'''
Created Date: 2023-07-15
Qn: You are given an array of events where events[i] = [startDayi, endDayi,
    valuei]. The ith event starts at startDayi and ends at endDayi, and if you
    attend this event, you will receive a value of valuei. You are also given
    an integer k which represents the maximum number of events you can attend.

    You can only attend one event at a time. If you choose to attend an event,
    you must attend the entire event. Note that the end day is inclusive: that
    is, you cannot attend two events where one of them starts and the other
    ends on the same day.

    Return the maximum sum of values that you can receive by attending events.
Link: https://leetcode.com/problems/maximum-number-of-events-that-can-be-attended-ii/
Notes:
    - use dfs
    - at each event you have 2 choices, either attend or skip
'''
def maxValue(events: list[list[int]], k: int) -> int:
    events.sort()
    N = len(events)
    dp = [[-1] * N for _ in range(k+1)]
    
    def dfs(cur_index: int, count: int, prev_end_time: int) -> int:
        if count == k or cur_index == N: return 0
        if events[cur_index][0] <= prev_end_time: return dfs(cur_index+1, count, prev_end_time)
        if dp[count][cur_index] != -1: return dp[count][cur_index]
        res = max(dfs(cur_index+1, count, prev_end_time), events[cur_index][2] + dfs(cur_index+1, count+1, events[cur_index][1]))
        dp[count][cur_index] = res
        return res

    return dfs(0, 0, -1)

if __name__ == '__main__':
    e1, k1 = [[1,2,4],[3,4,3],[2,3,1]], 2
    e2, k2 = [[1,2,4],[3,4,3],[2,3,10]], 2
    e3, k3 = [[1,1,1],[2,2,2],[3,3,3],[4,4,4]], 3

    print(maxValue(e1, k1))
    print(maxValue(e2, k2))
    print(maxValue(e3, k3))


