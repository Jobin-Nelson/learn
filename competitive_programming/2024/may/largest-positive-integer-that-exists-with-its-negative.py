"""
Created Date: 2024-05-02
Qn: Given an integer array nums that does not contain any zeros, find the
    largest positive integer k such that -k also exists in the array.

    Return the positive integer k. If there is no such integer, return -1.
Link: https://leetcode.com/problems/largest-positive-integer-that-exists-with-its-negative/
Notes:
"""
def findMaxK(nums: list[int]) -> int:
    res = -1
    seen = set()
    for n in nums:
        if n * -1 in seen:
            res = max(res, n, n * -1)
        else:
            seen.add(n)
    return res

if __name__ == '__main__':
    n1 = [-1, 2, -3, 3]
    n2 = [-1, 10, 6, 7, -7, 1]
    n3 = [-10, 8, 6, 7, -2, -3]

    print(findMaxK(n1))
    print(findMaxK(n2))
    print(findMaxK(n3))
