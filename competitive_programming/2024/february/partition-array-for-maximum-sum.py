"""
Created Date: 2024-02-03
Qn: Given an integer array arr, partition the array into (contiguous) subarrays
    of length at most k. After partitioning, each subarray has their values
    changed to become the maximum value of that subarray.

    Return the largest sum of the given array after partitioning. Test cases
    are generated so that the answer fits in a 32-bit integer.
Link: https://leetcode.com/problems/partition-array-for-maximum-sum/
Notes:
    - use dfs with memoization or dp approach
"""
def maxSumAfterPartitioning(arr: list[int], k: int) -> int:
    # dp approach
    N = len(arr)
    dp = [0] * (N + 1)
    for start in range(N-1, -1, -1):
        cur_max = 0
        for i in range(start, min(N, start + k)):
            cur_max = max(cur_max, arr[i])
            dp[start] = max(dp[start], dp[i+1] + cur_max * (i-start+1))
    return dp[0]

    # dfs approach
    # memo = {}
    # def dfs(i: int) -> int:
    #     if i in memo: return memo[i]
    #     # if i >= len(arr): return 0  # reduntant as for loop won't run anyway
    #     cur_max = 0
    #     res = 0
    #     for j in range(i, min(len(arr), i+k)):
    #         cur_max = max(cur_max, arr[j])
    #         window_size = j - i + 1
    #         res = max(res, dfs(j + 1) + cur_max * window_size)
    #     memo[i] = res
    #     return res
    # return dfs(0)

if __name__ == '__main__':
    a1, k1 = [1,15,7,9,2,5,10], 3
    a2, k2 = [1,4,1,5,7,3,6,1,9,9,3], 4
    a3, k3 = [1], 1

    print(maxSumAfterPartitioning(a1, k1))
    print(maxSumAfterPartitioning(a2, k2))
    print(maxSumAfterPartitioning(a3, k3))
