'''
Created Date: 2022-11-18
Qn: An ugly number is a positive integer whose prime factors are limited to 2,
    3, and 5.

    Given an integer n, return true if n is an ugly number.
Link: https://leetcode.com/problems/ugly-number/
Notes:
    - divide by 2, 3, 5 while the num is divisible by them
    - if the result equals 1 return True otherwise False
'''
def isUgly(n: int) -> bool:
    if n <= 0: return False

    for i in [2, 3, 5]:
        while n % i == 0:
            n /= i
    return n == 1

if __name__ == '__main__':
    n1 = 6
    n2 = 1
    n3 = 14

    print(isUgly(n1))
    print(isUgly(n2))
    print(isUgly(n3))
