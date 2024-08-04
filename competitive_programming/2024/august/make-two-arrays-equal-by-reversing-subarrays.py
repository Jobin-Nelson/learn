"""
Created Date: 2024-08-03
Qn: You are given two integer arrays of equal length target and arr. In one
    step, you can select any non-empty subarray of arr and reverse it. You are
    allowed to make any number of steps.

    Return true if you can make arr equal to target or false otherwise.
Link: https://leetcode.com/problems/make-two-arrays-equal-by-reversing-subarrays/
Notes:
    - use hashmap
"""

from collections import Counter


def canBeEqual(target: list[int], arr: list[int]) -> bool:
    ct = Counter(target)
    ca = Counter(arr)
    return ct == ca


if __name__ == '__main__':
    t1, a1 = list(range(1, 5)), [2, 4, 1, 3]
    t2, a2 = [7], [7]
    t3, a3 = [3, 7, 9], [3, 7, 11]

    print(canBeEqual(t1, a1))
    print(canBeEqual(t2, a2))
    print(canBeEqual(t3, a3))
