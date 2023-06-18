'''
Created Date: 2023-06-17
Qn: Given two integer arrays arr1 and arr2, return the minimum number of
    operations (possibly zero) needed to make arr1 strictly increasing.

    In one operation, you can choose two indices 0 <= i < arr1.length and 0 <=
    j < arr2.length and do the assignment arr1[i] = arr2[j].

    If there is no way to make arr1 strictly increasing, return -1.
Link: https://leetcode.com/problems/make-array-strictly-increasing/
Notes:
    - use dp
'''
from collections import defaultdict
from bisect import bisect_right

def makeArrayIncreasing(arr1: list[int], arr2: list[int]) -> int:
    dp = {-1: 0}
    arr2.sort()
    n1, n2 = len(arr1), len(arr2)

    for i in range(n1):
        new_dp = defaultdict(lambda: float('inf'))
        for prev in dp:
            if arr1[i] > prev:
                new_dp[arr1[i]] = min(new_dp[arr1[i]], dp[prev])
            idx = bisect_right(arr2, prev)
            if idx < n2:
                new_dp[arr2[idx]] = min(new_dp[arr2[idx]], 1 + dp[prev])
        dp = new_dp
    return min(dp.values()) if dp else -1



if __name__ == '__main__':
    a11, a12 = [1,5,3,6,7], [1,3,2,4]
    a21, a22 = [1,5,3,6,7], [4,3,1]
    a31, a32 = [1,5,3,6,7], [1,6,3,3]

    print(makeArrayIncreasing(a11, a12))
    print(makeArrayIncreasing(a21, a22))
    print(makeArrayIncreasing(a31, a32))
