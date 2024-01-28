"""
Created Date: 2024-01-20
Qn: Given an array of integers arr, find the sum of min(b), where b ranges over
    every (contiguous) subarray of arr. Since the answer may be large, return
    the answer modulo 109 + 7.
Link: https://leetcode.com/problems/sum-of-subarray-minimums/
Notes:
    - use monotonic stack
"""
def sumSubarrayMins(arr: list[int]) -> int:
    res = 0
    mod = 10 ** 9 + 7
    arr = [float('-inf')] + arr + [float('-inf')]
    stack = []
    for i, n in enumerate(arr):
        while stack and n < stack[-1][1]:
            j, m = stack.pop()
            left = j - stack[-1][0] if stack else j+1
            right = i - j
            res = (res + m * left * right) % mod
        stack.append((i, n))
    return res % mod

if __name__ == '__main__':
    a1 = [3, 1, 2, 4]
    a2 = [11, 81, 94, 43, 3]

    print(sumSubarrayMins(a1))
    print(sumSubarrayMins(a2))
