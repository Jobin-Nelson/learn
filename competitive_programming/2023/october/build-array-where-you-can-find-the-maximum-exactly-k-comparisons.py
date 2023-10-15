'''
Created Date: 2023-10-07
Qn: You are given three integers n, m and k. Consider the following algorithm
    to find the maximum element of an array of positive integers:
    You should build the array arr which has the following properties:

    - arr has exactly n integers.
    - 1 <= arr[i] <= m where (0 <= i < n).
    - After applying the mentioned algorithm to arr, the value search_cost is
      equal to k.

    Return the number of ways to build the array arr under the mentioned
    conditions. As the answer may grow large, the answer must be computed
    modulo 109 + 7.
Link: https://leetcode.com/problems/build-array-where-you-can-find-the-maximum-exactly-k-comparisons/
Notes:
    - use dfs
'''
from functools import cache

def numOfArray(n: int, m: int, k: int) -> int:
    mod = 10**9 + 7

    @cache
    def dp(i: int, max_so_far: int, remain: int) -> int:
        if i == n:
            if remain == 0: return 1
            return 0
        ans = (max_so_far * dp(i+1, max_so_far, remain)) % mod
        for num in range(max_so_far+1, m+1):
            ans = (ans + dp(i+1, num, remain-1)) % mod
        return ans
    return dp(0, 0, k)

if __name__ == '__main__':
    n1, m1 , k1 = 2, 3, 1
    n2, m2 , k2 = 5, 2, 3
    n3, m3 , k3 = 9, 1, 1

    print(numOfArray(n1, m1, k1))
    print(numOfArray(n2, m2, k2))
    print(numOfArray(n3, m3, k3))
