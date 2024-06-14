"""
Created Date: 2024-06-03
Qn: You are given two strings s and t consisting of only lowercase English
    letters.

    Return the minimum number of characters that need to be appended to the end
    of s so that t becomes a subsequence of s.

    A subsequence is a string that can be derived from another string by
    deleting some or no characters without changing the order of the remaining
    characters.
Link: https://leetcode.com/problems/append-characters-to-string-to-make-subsequence/
Notes:
    - use two pointers
"""
def appendCharacters(s: str, t: str) -> int:
    i, j = 0, 0
    len_t, len_s = len(t), len(s)
    while i < len_s and j < len_t:
        if s[i] == t[j]:
            j += 1
        i += 1
    return len_t - j

if __name__ == '__main__':
    s1, t1 = "coaching", "coding"
    s2, t2 = "abcde", "a"
    s3, t3 = "z", "abcde"

    print(appendCharacters(s1, t1))
    print(appendCharacters(s2, t2))
    print(appendCharacters(s3, t3))
