"""
Created Date: 2024-01-06
Qn: We have n jobs, where every job is scheduled to be done from startTime[i]
    to endTime[i], obtaining a profit of profit[i].

    You're given the startTime, endTime and profit arrays, return the maximum
    profit you can take such that there are no two jobs in the subset with
    overlapping time range.

    If you choose a job that ends at time X you will be able to start another
    job that starts at time X.
Link: https://leetcode.com/problems/maximum-profit-in-job-scheduling/
Notes:
    - use recursion or binary search
"""
import bisect

def jobScheduling(startTime: list[int], endTime: list[int], profit: list[int]) -> int:
    # intervals = sorted(zip(startTime, endTime, profit))
    # memo = {}
    #
    # def dfs(i: int) -> int:
    #     if i == len(startTime): return 0
    #     if i in memo: return memo[i]
    #
    #     # skip the current job
    #     res = dfs(i+1)
    #
    #     # taking the current job
    #     j = bisect.bisect(intervals, (intervals[i][1], -1 ,-1))
    #     res = max(res, intervals[i][2] + dfs(j))
    #     memo[i] = res
    #     return res
    # return dfs(0)

    # binary search
    jobs = sorted(zip(startTime, endTime, profit), key=lambda x: x[1])
    N = len(startTime)
    endTimes = [i[1] for i in jobs]

    dp = [0] * N
    dp[0] = jobs[0][2]

    for i in range(1, N):
        s, e, p = jobs[i]
        # skip the current job
        dp[i] = dp[i-1]

        # take the current job
        ind = bisect.bisect_right(endTimes, s) -1
        dp[i] = max(dp[i], (dp[ind] if ind >=0 else 0) + p)
    return dp[-1]


if __name__ == '__main__':
    s1, e1, p1 = [1,2,3,3], [3,4,5,6], [50,10,40,70]
    s2, e2, p2 = [1,2,3,4,6], [3,5,10,6,9], [20,20,100,70,60]
    s3, e3, p3 = [1,1,1], [2,3,4], [5,6,4]

    print(jobScheduling(s1, e1, p1))
    print(jobScheduling(s2, e2, p2))
    print(jobScheduling(s3, e3, p3))


