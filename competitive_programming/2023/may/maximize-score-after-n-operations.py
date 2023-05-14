'''
Created Date: 2023-05-14
Qn: You are given nums, an array of positive integers of size 2 * n. You must
    perform n operations on this array.

    In the ith operation (1-indexed), you will:

        - Choose two elements, x and y.
        - Receive a score of i * gcd(x, y).
        - Remove x and y from nums.

    Return the maximum score you can receive after performing n operations.

    The function gcd(x, y) is the greatest common divisor of x and y.
Link: https://leetcode.com/problems/maximize-score-after-n-operations/
Notes:
'''
import math

def maxScore(nums:list[int]) -> int:
    # def gcd(x: int, y: int) -> int:
    #     while y:
    #         x, y = y, x % y
    #     return x

if __name__ == '__main__':
    n1 = [1, 2]
    n2 = [3, 4, 6, 8]
    n3 = [1, 2, 3, 4, 5, 6]

    print(maxScore(n1))
    print(maxScore(n2))
    print(maxScore(n3))
