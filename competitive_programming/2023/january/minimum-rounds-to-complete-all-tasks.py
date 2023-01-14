'''
Created Date: 2023-01-04
Qn: You are given a 0-indexed integer array tasks, where tasks[i] represents
    the difficulty level of a task. In each round, you can complete either 2 or
    3 tasks of the same difficulty level.

    Return the minimum rounds required to complete all the tasks, or -1 if it
    is not possible to complete all the tasks.
Link: https://leetcode.com/problems/minimum-rounds-to-complete-all-tasks/
Notes:
    - count the frequency of each values
    - if the count is 1 we can't complete the tasks since we can only complete
      2 or 3 at each round
    - increment result each time with the quotient frequency count by 3 if it
      is divisible by 3 else quotient + 1 to count for groups of 2
'''
from collections import Counter

def minimumRounds(tasks: list[int]) -> int:
    c = Counter(tasks)

    res = 0
    for v in c.values():
        if v == 1: return -1
        if v % 3 == 0:
            res += v // 3
        else:
            res += v // 3 + 1
    return res

if __name__ == '__main__':
    t1 = [2,2,3,3,2,4,4,4,4,4]
    t2 = [2,3,3]

    print(minimumRounds(t1))
    print(minimumRounds(t2))
