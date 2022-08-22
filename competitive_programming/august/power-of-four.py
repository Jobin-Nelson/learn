'''
Created Date: 2022-08-22
Qn: Given an integer n, return true if it is a power of four. Otherwise, return
    false.

    An integer n is a power of four, if there exists an integer x such that
    n == 4x.
Link: https://leetcode.com/problems/power-of-four/
Notes:
- 4^2 = 16
- log4(16) = 2
'''
import math

def isPowerOfFour(n: int) -> bool:
    return False if n < 1 else 4 ** int(math.log(n, 4)) == n

if __name__ == '__main__':
    n1, n2, n3 = 16, 5, 1
    print(isPowerOfFour(n1))
    print(isPowerOfFour(n2))
    print(isPowerOfFour(n3))
