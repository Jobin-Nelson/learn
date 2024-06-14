"""
Created Date: 2024-05-28
Qn: You are given two strings s and t of the same length and an integer
    maxCost.

    You want to change s to t. Changing the ith character of s to ith character
    of t costs |s[i] - t[i]| (i.e., the absolute difference between the ASCII
    values of the characters).

    Return the maximum length of a substring of s that can be changed to be the
    same as the corresponding substring of t with a cost less than or equal to
    maxCost. If there is no substring from s that can be changed to its
    corresponding substring from t, return 0.
Link: https://leetcode.com/problems/get-equal-substrings-within-budget/
Notes:
    - use sliding window
"""
def equalSubstring(s: str, t: str, maxCost: int) -> int:
    N = len(s)
    l = 0
    res = 0
    cur_cost = 0

    for r in range(N):
        cur_cost += abs(ord(s[r]) - ord(t[r]))
        while cur_cost > maxCost:
            cur_cost -= abs(ord(s[l]) - ord(t[l]))
            l += 1
        res = max(res, r-l+1)
    return res

if __name__ == '__main__':
    s1, t1, m1 = "abcd", "bcdf", 3
    s2, t2, m2 = "abcd", "cdef", 3
    s3, t3, m3 = "abcd", "acde", 0

    print(equalSubstring(s1, t1, m1))
    print(equalSubstring(s2, t2, m2))
    print(equalSubstring(s3, t3, m3))
