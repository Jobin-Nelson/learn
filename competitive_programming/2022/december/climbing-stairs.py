'''
Created Date: 2022-12-12
Qn: You are climbing a staircase. It takes n steps to reach the top.

    Each time you can either climb 1 or 2 steps. In how many distinct ways can
    you climb to the top?
Link: https://leetcode.com/problems/climbing-stairs/
Notes:
    - fibonacci problem
    - use two variables
'''
def climbStairs(n: int) -> int:
    l, r = 0, 1

    for _ in range(n):
        l, r = r, l + r
    return r

if __name__ == '__main__':
    n1 = 2
    n2 = 3

    print(climbStairs(n1))
    print(climbStairs(n2))
