'''
Created Date: 2023-10-23
Qn: Given an integer n, return true if it is a power of four. Otherwise, return
    false.

    An integer n is a power of four, if there exists an integer x such that n
    == 4x.
Link: https://leetcode.com/problems/power-of-four/
Notes:
'''
import math
def isPowerOfFour(n: int) -> bool:
    return n > 0 and math.log(n, 4) % 1 == 0

if __name__ == '__main__':
    n1 = 16
    n2 = 5
    n3 = 1

    print(isPowerOfFour(n1))
    print(isPowerOfFour(n2))
    print(isPowerOfFour(n3))
