"""
Created Date: 2024-06-18
Qn: You have n jobs and m workers. You are given three arrays: difficulty,
    profit, and worker where:

        - difficulty[i] and profit[i] are the difficulty and the profit of the
          ith job, and
        - worker[j] is the ability of jth worker (i.e., the jth worker can only
          complete a job with difficulty at most worker[j]).

    Every worker can be assigned at most one job, but one job can be completed
    multiple times.

        - For example, if three workers attempt the same job that pays $1, then
          the total profit will be $3. If a worker cannot complete any job,
          their profit is $0.

    Return the maximum profit we can achieve after assigning the workers to the
    jobs.
Link: https://leetcode.com/problems/most-profit-assigning-work/
Notes:
    - use dp
"""
def maxProfitAssigment(difficulty: list[int], profit: list[int], worker: list[int]) -> int:
    max_ability = max(worker)
    jobs = [0] * (max_ability + 1)
    for i in range(len(difficulty)):
        if difficulty[i] <= max_ability:
            jobs[difficulty[i]] = max(jobs[difficulty[i]], profit[i])
    for i in range(1, max_ability+1):
        jobs[i] = max(jobs[i], jobs[i-1])
    res = 0
    for ability in worker:
        res += jobs[ability]
    return res

if __name__ == '__main__':
    d1, p1, w1 = [2,4,6,8,10], [10,20,30,40,50], [4,5,6,7]
    d2, p2, w2 = [85,47,57], [24,66,99], [40,25,25]

    print(maxProfitAssigment(d1, p1, w1))
    print(maxProfitAssigment(d1, p1, w1))
