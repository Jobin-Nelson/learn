'''
Created Date: 2022-11-22
Qn: Given an integer n, return the least number of perfect square numbers that
    sum to n.

    A perfect square is an integer that is the square of an integer; in other
    words, it is the product of some integer with itself. For example, 1, 4, 9,
    and 16 are perfect squares while 3 and 11 are not.
Link: https://leetcode.com/problems/perfect-squares/
Notes:
    - Any number can be represented as a sum of 4 squares, proof can be found
      in https://en.wikipedia.org/wiki/Lagrange's_four-square_theorem
    - check num is a full square: compare square of integer part of root with
      the number
    - check num is a sum of 2 square: iterate over all 0 <= i <= sqrt(n) and
      check n - i*i is a full square
    - check num is a sum of 4 sqaure: if the number is in the form of 
      4^k(8m + 7) for integers k and m
    - check num is a sum of 3 sqaure: else answer is 3
'''
from math import sqrt

def numSquares(n: int) -> int:
    if int(sqrt(n))**2 == n: return 1
    for i in range(int(sqrt(n) + 1)):
        if int(sqrt(n - i*i))**2 == n - i*i: return 2
    while n % 4 == 0:
        n >>= 2
    if n % 8 == 7: return 4
    return 3

if __name__ == '__main__':
    n1 = 12
    n2 = 13

    print(numSquares(n1))
    print(numSquares(n2))
