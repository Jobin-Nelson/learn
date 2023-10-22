'''
Created Date: 2023-10-21
Qn: Given an integer array nums and an integer k, return the maximum sum of a
    non-empty subsequence of that array such that for every two consecutive
    integers in the subsequence, nums[i] and nums[j], where i < j, the
    condition j
    - i <= k is satisfied.

    A subsequence of an array is obtained by deleting some number of elements
    (can be zero) from the array, leaving the remaining elements in their
    original order.
Link: https://leetcode.com/problems/constrained-subsequence-sum/
Notes:
    - use a monotonic queue to keep track of the largest sum/dp for the last k
      numbers
'''
from collections import deque

def constrainedSubsetSum(nums: list[int], k: int) -> int:
    q = deque([])
    dp = [0] * len(nums)

    for i in range(len(nums)):
        while q and i - q[0] > k:
            q.popleft()
        dp[i] = nums[i] + (dp[q[0]] if q else 0)
        while q and dp[q[-1]] < dp[i]:
            q.pop()
        if dp[i] > 0: q.append(i)
    return max(dp)

if __name__ == '__main__':
    n1, k1 = [10,2,-10,5,20], 2
    n2, k2 = [-1,-2,-3], 1
    n3, k3 = [10,-2,-10,-5,20], 2

    print(constrainedSubsetSum(n1, k1))
    print(constrainedSubsetSum(n2, k2))
    print(constrainedSubsetSum(n3, k3))
