'''
Created Date: 2022-12-15 
Qn: Given two strings text1 and text2, return the length of their longest
    common subsequence. If there is no common subsequence, return 0.

    A subsequence of a string is a new string generated from the original
    string with some characters (can be none) deleted without changing the
    relative order of the remaining characters.

    For example, "ace" is a subsequence of "abcde". A common subsequence of two
    strings is a subsequence that is common to both strings.
Link: https://leetcode.com/problems/longest-common-subsequence/
Notes:
    - use 2d matrix dp
    - add one if equal character else maintain max
'''
def longestCommonSubsequence(text1: str, text2: str) -> int:
    dp = [[0] * (len(text2)+1) for _ in range(len(text1)+1)]

    for i in range(len(text1)-1, -1, -1):
        for j in range(len(text2)-1, -1, -1):
            if text1[i] == text2[j]:
                dp[i][j] = 1 + dp[i+1][j+1]
            else:
                dp[i][j] = max(dp[i+1][j], dp[i][j+1])
    return dp[0][0]

if __name__ == '__main__':
    t11, t12 = "abcde", "ace"
    t21, t22 = "abc", "abc"
    t31, t32 = "abc", "def"

    print(longestCommonSubsequence(t11, t12))
    print(longestCommonSubsequence(t21, t22))
    print(longestCommonSubsequence(t31, t32))
