"""
Created Date: 2024-01-04
Qn: You are given a 0-indexed array nums consisting of positive integers.

    There are two types of operations that you can apply on the array any
    number of times:

        - Choose two elements with equal values and delete them from the array.
        - Choose three elements with equal values and delete them from the
          array.

    Return the minimum number of operations required to make the array empty,
    or -1 if it is not possible.
Link: https://leetcode.com/problems/minimum-number-of-operations-to-make-array-empty/
Notes:
    - use ceiling division with 3
    - most effecient way is to always choose three elements if there are
      remainders it will always be a single addition that is accounted by
      ceiling division
"""
from collections import Counter
import math

def minOperation(nums: list[int]) -> int:
    res = 0
    for v in Counter(nums).values():
        if v == 1: return -1
        res += math.ceil(v/3)
    return res

if __name__ == '__main__':
    n1 = [2,3,3,2,2,4,2,3,4]
    n2 = [2,1,2,2,3,3]
    n3 = [14,12,14,14,12,14,14,12,12,12,12,14,14,12,14,14,14,12,12]

    print(minOperation(n1))
    print(minOperation(n2))
    print(minOperation(n3))
