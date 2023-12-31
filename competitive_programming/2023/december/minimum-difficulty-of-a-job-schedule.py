"""
Created Date: 2023-12-29
Qn: You want to schedule a list of jobs in d days. Jobs are dependent (i.e To
    work on the ith job, you have to finish all the jobs j where 0 <= j < i).

    You have to finish at least one task every day. The difficulty of a job
    schedule is the sum of difficulties of each day of the d days. The
    difficulty of a day is the maximum difficulty of a job done on that day.

    You are given an integer array jobDifficulty and an integer d. The
    difficulty of the ith job is jobDifficulty[i].

    Return the minimum difficulty of a job schedule. If you cannot find a
    schedule for the jobs return -1.
Link: https://leetcode.com/problems/minimum-difficulty-of-a-job-schedule/
Notes:
"""
from functools import cache

def minDifficulty(jobDifficulty: list[int], d: int) -> int:
    if len(jobDifficulty) < d: return -1
    @cache
    def dfs(i: int, d: int, cur_max: int) -> int:
        if i == len(jobDifficulty):
            return 0 if d == 0 else float('inf')
        if d == 0:
            return float('inf')

        cur_max = max(cur_max, jobDifficulty[i])

        res = min(
            dfs(i+1, d, cur_max),
            cur_max + dfs(i+1, d-1, -1)
        )
        return res
    return dfs(0, d, -1)

if __name__ == '__main__':
    j1, d1 = [6,5,4,3,2,1], 2
    j2, d2 = [9,9,9], 4
    j3, d3 = [1,1,1], 3
    j4, d4 = [11,111,22,222,33,333,44,444], 6

    print(minDifficulty(j1, d1))
    print(minDifficulty(j2, d2))
    print(minDifficulty(j3, d3))
    print(minDifficulty(j4, d4))
