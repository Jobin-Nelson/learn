"""
Created Date: 2024-02-04
Qn: Given two strings s and t of lengths m and n respectively, return the
    minimum window substring of s such that every character in t (including
    duplicates) is included in the window. If there is no such substring,
    return the empty string "".

    The testcases will be generated such that the answer is unique.
Link: https://leetcode.com/problems/minimum-window-substring/
Notes:
    - use counters
"""
from collections import Counter
from sys import maxsize

def minWindow(s: str, t: str) -> str:
    if t == "": return ""
    count_t = Counter(t)
    count_s = Counter()

    l, max_len = 0, maxsize
    max_p = (0, 0)
    need, have = len(count_t), 0

    for r, c in enumerate(s):
        if c not in count_t: continue
        count_s[c] += 1
        if count_s[c] == count_t[c]: have += 1
        while have >= need:
            if r-l+1 < max_len:
                max_len = r-l+1
                max_p = (l, r)
            sc = s[l]
            if sc in count_t: count_s[sc] -= 1
            if count_s[sc] < count_t[sc]: have -= 1
            l += 1
    return s[max_p[0]:max_p[1]+1] if max_len < maxsize else ""

if __name__ == '__main__':
    s1, t1 = "ADOBECODEBANC", "ABC"
    s2, t2 = "a", "a"
    s3, t3 = "a", "aa"
    s4, t4 = "aa", "aa"

    print(minWindow(s1, t1))
    print(minWindow(s2, t2))
    print(minWindow(s3, t3))
    print(minWindow(s4, t4))
