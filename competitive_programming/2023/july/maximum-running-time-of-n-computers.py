'''
Created Date: 2023-07-27
Qn: You have n computers. You are given the integer n and a 0-indexed integer
    array batteries where the ith battery can run a computer for batteries[i]
    minutes. You are interested in running all n computers simultaneously using
    the given batteries.

    Initially, you can insert at most one battery into each computer. After
    that and at any integer time moment, you can remove a battery from a
    computer and insert another battery any number of times. The inserted
    battery can be a totally new battery or a battery from another computer.
    You may assume that the removing and inserting processes take no time.

    Note that the batteries cannot be recharged.

    Return the maximum number of minutes you can run all the n computers
    simultaneously.
Link: https://leetcode.com/problems/maximum-running-time-of-n-computers/
Notes:
    - use binary search
'''
def maxRunTime(n: int, batteries: list[int]) -> int:
    l, r = 1, sum(batteries) // n

    while l < r:
        target = r - ((r - l) >> 1)
        extra = sum(min(power, target) for power in batteries)
        if extra // n >= target:
            l = target
        else:
            r = target - 1
    return l

if __name__ == '__main__':
    n1, b1 = 2, [3,3,3]
    n2, b2 = 2, [1,1,1,1]
    n3, b3 = 3, [10,10,3,5]

    print(maxRunTime(n1, b1))
    print(maxRunTime(n2, b2))
    print(maxRunTime(n3, b3))
