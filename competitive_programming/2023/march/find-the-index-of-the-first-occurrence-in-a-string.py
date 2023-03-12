'''
Created Date: 2023-03-03
Qn: Given two strings needle and haystack, return the index of the first
    occurrence of needle in haystack, or -1 if needle is not part of haystack.
Link: https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/
Notes:
    - use two pointers
'''
def strStr(haystack: str, needle: str) -> int:
    N, M = len(haystack), len(needle) - 1
    i = j = 0

    while i < N:
        while i < N and haystack[i] == needle[j]:
            if j == M: return i - j
            i += 1
            j += 1
        i = i - j + 1
        j = 0

    return -1

if __name__ == '__main__':
    h1, n1 = "sadbutsad", "sad"
    h2, n2 = "leetcode", "leeto"
    h3, n3 = "mississippi", "issip"

    print(strStr(h1, n1))
    print(strStr(h2, n2))
    print(strStr(h3, n3))
