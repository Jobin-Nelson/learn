'''
Created Date: 2022-10-22
Qn: Given two strings s and t of lengths m and n respectively, return the
    minimum window substring of s such that every character in t 
    (including duplicates) is included in the window. If there is no such
    substring, return the empty string "".

    The testcases will be generated such that the answer is unique.

    A substring is a contiguous sequence of characters within the string.
Link: https://leetcode.com/problems/minimum-window-substring/
Notes:
    - sliding window
    - keep track of the count of characters on both strings
    - motion similar to a worm 
'''
def minWindows(s: str, t: str) -> str:
    if t == '': return ''

    l, r, N = 0, 0, len(s)
    res, res_len = (-1, -1), N + 1
    s_count, t_count = {}, {}

    for ch in t:
        t_count[ch] = t_count.get(ch, 0) + 1
        
    have, need = 0, len(t_count)

    while r < N:
        rch = s[r]
        s_count[rch] = s_count.get(rch, 0) + 1
        if rch in t_count and s_count[rch] == t_count[rch]: have += 1

        while have == need:
            if r-l+1 < res_len:
                res_len = r-l+1
                res = (l, r)
            lch = s[l]
            s_count[lch] -= 1
            if lch in t_count and s_count[lch] < t_count[lch]: have -= 1
            l += 1
        r += 1
    l, r = res
    return s[l:r+1] if res_len != N + 1 else ''

if __name__ == '__main__':
    s1, t1 = "ADOBECODEBANC", "ABC"
    s2, t2 = "a", "a"
    s3, t3 = "a", "aa"

    print(minWindows(s1, t1))
    print(minWindows(s2, t2))
    print(minWindows(s3, t3))
