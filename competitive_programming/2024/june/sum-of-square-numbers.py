"""
Created Date: 2024-06-17
Qn: Given a non-negative integer c, decide whether there're two integers a and
    b such that a2 + b2 = c.
Link: https://leetcode.com/problems/sum-of-square-numbers/
Notes:
    - iterate from 0, sqrt(c) and use two sum problem solution
"""
from math import sqrt

def judgeSquareSum(c: int) -> bool:
    l, r = 0, int(sqrt(c))
    while l <= r:
        total = l * l + r * r
        if total < c:
            l += 1
        elif total > c:
            r -= 1
        else:
            return True
    return False

if __name__ == '__main__':
    c1 = 5
    c2 = 3

    print(judgeSquareSum(c1))
    print(judgeSquareSum(c2))
