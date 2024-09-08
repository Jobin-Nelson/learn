"""
Created Date: 2024-09-02
Qn: There are n students in a class numbered from 0 to n - 1. The teacher will
    give each student a problem starting with the student number 0, then the
    student number 1, and so on until the teacher reaches the student number n
    - 1. After that, the teacher will restart the process, starting with the
    student number 0 again.

    You are given a 0-indexed integer array chalk and an integer k. There are
    initially k pieces of chalk. When the student number i is given a problem
    to solve, they will use chalk[i] pieces of chalk to solve that problem.
    However, if the current number of chalk pieces is strictly less than
    chalk[i], then the student number i will be asked to replace the chalk.

    Return the index of the student that will replace the chalk pieces.
Link: https://leetcode.com/problems/find-the-student-that-will-replace-the-chalk/
Notes:
    - use binary search
"""


def chalkReplacer(chalk: list[int], k: int) -> int:
    n = len(chalk)
    prefix_sum = [0] * n
    prefix_sum[0] = chalk[0]
    for i in range(1, n):
        prefix_sum[i] = prefix_sum[i - 1] + chalk[i]

    sum_chalk = prefix_sum[n-1]
    remaining_chalk = k % sum_chalk
    l, r = 0, n - 1
    while l < r:
        m = l + ((r - l) >> 1)
        if prefix_sum[m] > remaining_chalk:
            r = m
        else:
            l = m + 1
    return r


if __name__ == '__main__':
    c1, k1 = [5, 1, 5], 22
    c2, k2 = [3, 4, 1, 2], 25

    print(chalkReplacer(c1, k1))
    print(chalkReplacer(c2, k2))
