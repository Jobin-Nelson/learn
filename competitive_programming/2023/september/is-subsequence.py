'''
Created Date: 2023-09-22
Qn: Given two strings s and t, return true if s is a subsequence of t, or false
    otherwise.

    A subsequence of a string is a new string that is formed from the original
    string by deleting some (can be none) of the characters without disturbing
    the relative positions of the remaining characters. (i.e., "ace" is a
    subsequence of "abcde" while "aec" is not).
Link: https://leetcode.com/problems/is-subsequence/
Notes:
    - use two pointers
'''
def isSubsequence(s: str, t: str) -> bool:
    i = j = 0

    while i < len(s) and j < len(t):
        if s[i] == t[j]: i += 1
        j += 1
    return i == len(s)

if __name__ == '__main__':
    s1, t1 = "abc", "ahbgdc"
    s2, t2 = "axc", "ahbgdc"

    print(isSubsequence(s1, t1))
    print(isSubsequence(s2, t2))
