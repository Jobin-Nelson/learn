"""
Created Date: 2024-01-18
Qn: You are climbing a staircase. It takes n steps to reach the top.

    Each time you can either climb 1 or 2 steps. In how many distinct ways can
    you climb to the top?
Link: https://leetcode.com/problems/climbing-stairs/
Notes:
    - use two variables to do dp solution
"""
def climbStairs(n: int) -> int:
    a, b = 0, 1

    for _ in range(n):
        a, b = b, a + b
    return b

if __name__ == '__main__':
    n1 = 2
    n2 = 3
    
    print(climbStairs(n1))
    print(climbStairs(n2))
