"""
Created Date: 2024-01-25
Qn: Given two strings text1 and text2, return the length of their longest
    common subsequence. If there is no common subsequence, return 0.

    A subsequence of a string is a new string generated from the original
    string with some characters (can be none) deleted without changing the
    relative order of the remaining characters.

        For example, "ace" is a subsequence of "abcde".

    A common subsequence of two strings is a subsequence that is common to both
    strings.
Link: https://leetcode.com/problems/longest-common-subsequence/
Notes:
    - use dynamic programming and use two lists to optimize space
"""
def longestCommonSubsequence(text1: str, text2: str) -> int:
    m, n = len(text1), len(text2)
    prev = [0] * (n+1)
    for i in range(m-1, -1, -1):
        cur = [0] * (n+1)
        for j in range(n-1, -1, -1):
            if text1[i] == text2[j]:
                cur[j] = prev[j+1] + 1
            else:
                cur[j] = max(cur[j+1], prev[j])
        prev = cur
    return prev[0]

if __name__ == '__main__':
    t11, t12 = "abcde", "ace"
    t21, t22 = "abc", "abc"
    t31, t32 = "abc", "def"

    print(longestCommonSubsequence(t11, t12))
    print(longestCommonSubsequence(t21, t22))
    print(longestCommonSubsequence(t31, t32))
