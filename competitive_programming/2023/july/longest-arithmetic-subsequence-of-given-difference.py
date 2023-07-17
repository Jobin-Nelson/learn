'''
Created Date: 2023-07-14
Qn: Given an integer array arr and an integer difference, return the length of
    the longest subsequence in arr which is an arithmetic sequence such that
    the difference between adjacent elements in the subsequence equals
    difference.

    A subsequence is a sequence that can be derived from arr by deleting some
    or no elements without changing the order of the remaining elements.
Link: https://leetcode.com/problems/longest-arithmetic-subsequence-of-given-difference/
Notes:
    - use dp
    - modification of 2 sum
'''
def longestSubsequence(arr: list[int], difference: int) -> int:
    dp = {}
    res = 1
    for a in arr:
        before_a = dp.get(a - difference, 0)
        dp[a] = before_a + 1
        res = max(res, dp[a])
    return res

if __name__ == '__main__':
    a1, d1 = [1,2,3,4], 1
    a2, d2 = [1,3,5,7], 1
    a3, d3 = [1,5,7,8,5,3,4,2,1], -2

    print(longestSubsequence(a1, d1))
    print(longestSubsequence(a2, d2))
    print(longestSubsequence(a3, d3))
