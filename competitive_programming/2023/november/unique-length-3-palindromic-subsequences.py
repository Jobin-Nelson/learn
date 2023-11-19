'''
Created Date: 2023-11-14
Qn: Given a string s, return the number of unique palindromes of length three
    that are a subsequence of s.

    Note that even if there are multiple ways to obtain the same subsequence, it is
    still only counted once.

    A palindrome is a string that reads the same forwards and backwards.

    A subsequence of a string is a new string generated from the original string
    with some characters (can be none) deleted without changing the relative order
    of the remaining characters.

        - For example, "ace" is a subsequence of "abcde".

Link: https://leetcode.com/problems/unique-length-3-palindromic-subsequences/
Notes:
    - pre count the first and last occurence of a letter
    - then count the letters in between them to get the sum of palindromes
'''

def countPalindromicSubsequence(s: str) -> int:
    first_count = [-1] * 26
    last_count = [-1] * 26

    for i in range(len(s)):
        cur = ord(s[i]) - ord('a')
        if first_count[cur] == -1:
            first_count[cur] = i
        last_count[cur] = i

    res = 0
    for i in range(26):
        if first_count[i] == -1: continue
        pals = set(s[j] for j in range(first_count[i]+1, last_count[i]))
        res += len(pals)
    return res

if __name__ == '__main__':
    s1 = "aabca"
    s2 = "adc"
    s3 = "bbcbaba"

    print(countPalindromicSubsequence(s1))
    print(countPalindromicSubsequence(s2))
    print(countPalindromicSubsequence(s3))
