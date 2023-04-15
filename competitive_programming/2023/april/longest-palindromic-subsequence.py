'''
Created Date: 2023-04-14
Qn: Given a string s, find the longest palindromic subsequence's length in s.

    A subsequence is a sequence that can be derived from another sequence by
    deleting some or no elements without changing the order of the remaining
    elements.
Link: https://leetcode.com/problems/longest-palindromic-subsequence/
Notes:
    - use 2d dp or two arrays because we only need to rows at a time
'''
def longestPalindromeSubseq(s: str) -> int:
    n = len(s)
    dp = [0] * n

    for i in range(n-1, -1, -1):
        new_dp = [0] * n
        new_dp[i] = 1

        for j in range(i+1, n):
            if s[i] == s[j]:
                new_dp[j] = 2 + dp[j-1]
            else:
                new_dp[j] = max(dp[j], new_dp[j-1])
        dp = new_dp
    return dp[-1]

if __name__ == '__main__':
    s1 = "bbab"
    s2 = "cbbd"

    print(longestPalindromeSubseq(s1))
    print(longestPalindromeSubseq(s2))
