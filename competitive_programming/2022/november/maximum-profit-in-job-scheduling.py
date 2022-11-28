'''
Created Date: 2022-11-26
Qn: We have n jobs, where every job is scheduled to be done from startTime[i]
    to endTime[i], obtaining a profit of profit[i].

    You're given the startTime, endTime and profit arrays, return the maximum
    profit you can take such that there are no two jobs in the subset with
    overlapping time range.

    If you choose a job that ends at time X you will be able to start another
    job that starts at time X
Link: https://leetcode.com/problems/maximum-profit-in-job-scheduling/
Notes:
    - Sort start, end and profit according to the start time, some test cases
      are not sorted - the examples are misleading in this respect
    - If you choose to take job i skip all jobs that start before job i ends.
      jump is used to find the index of the first job that starts after job i
      ends.
    - Take a dynamic programming approach to determine the optimal profit. At
      each step you can choose
'''
import bisect

def jobScheduling(startTime: list[int], endTime: list[int], profit: list[int]) -> int:
    N = len(startTime)
    startTime, endTime, profit = zip(*sorted(zip(startTime, endTime, profit)))
    jump = {i: bisect.bisect_left(startTime, endTime[i]) for i in range(N)}

    dp = [0] * (N + 1)

    for i in range(N-1, -1, -1):
        dp[i] = max(dp[i+1], profit[i] + dp[jump[i]])

    return dp[0]

if __name__ == '__main__':
    s1, e1, p1 = [1, 2, 3, 3], [3, 4, 5, 6], [50, 10, 40, 70]
    s2, e2, p2 = [1, 2, 3, 4, 6], [3, 5, 10, 6, 9], [20, 20, 100, 70, 60]
    s3, e3, p3 = [1, 1, 1], [2, 3, 4], [5, 6, 4]
    
    print(jobScheduling(s1, e1, p1))
    print(jobScheduling(s2, e2, p2))
    print(jobScheduling(s3, e3, p3))
