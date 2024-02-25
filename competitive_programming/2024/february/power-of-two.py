"""
Created Date: 2024-02-19
Qn: Given an integer n, return true if it is a power of two. Otherwise, return
    false. An integer n is a power of two, if there exists an integer x such that
    n == 2x.
Link: https://leetcode.com/problems/power-of-two/
Notes:
    - the number should be positive and bit count should be one
"""
def isPowerOfTwo(n: int) -> bool:
    return n > 0 and n & (n-1) == 0

if __name__ == '__main__':
    n1 = 1
    n2 = 16
    n3 = 3
    
    print(isPowerOfTwo(n1))
    print(isPowerOfTwo(n2))
    print(isPowerOfTwo(n3))
