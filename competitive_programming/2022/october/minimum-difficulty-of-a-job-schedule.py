'''
Created Date: 2022-10-16
Qn: You want to schedule a list of jobs in d days. Jobs are dependent 
    (i.e To work on the ith job, you have to finish all the jobs j where 0 <= j
     < i).

    You have to finish at least one task every day. The difficulty of a job
    schedule is the sum of difficulties of each day of the d days. The
    difficulty of a day is the maximum difficulty of a job done on that day.

    You are given an integer array jobDifficulty and an integer d. The
    difficulty of the ith job is jobDifficulty[i].

    Return the minimum difficulty of a job schedule. If you cannot find a
schedule for the jobs return -1.
Link: https://leetcode.com/problems/minimum-difficulty-of-a-job-schedule/
Notes:
    - recursion
'''
def minDifficult(jobDifficulty: list[int], d: int) -> int:
    num_jobs = len(jobDifficulty)
    if num_jobs < d: return -1
    memo = {}

    def dp(day: int, cut: int) -> int:
        if (day, cut) in memo: return memo[(day, cut)]
        if day == 1: return max(jobDifficulty[cut:])
        max_so_far = 0
        res = float('inf')

        for j in range(cut, num_jobs - day + 1):
            max_so_far = max(max_so_far, jobDifficulty[j])
            res = min(res, max_so_far + dp(day - 1, j + 1))
        memo[(day, cut)] = res
        return res
    return dp(d, 0)

if __name__ == '__main__':
    j1, d1 = [6, 5, 4, 3, 2, 1], 2
    j2, d2 = [9, 9, 9], 4
    j3, d3 = [1, 1, 1], 3
    
    print(minDifficult(j1, d1))
    print(minDifficult(j2, d2))
    print(minDifficult(j3, d3))
