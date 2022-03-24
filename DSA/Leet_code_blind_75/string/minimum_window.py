'''
Qn: Given two strings s and t of lengths m and n respectively, 
return the minimum window substring of s such that every character in t (including duplicates) is included in the window. 
If there is no such substring, return the empty string "".
Link: https://leetcode.com/problems/minimum-window-substring/
Notes: 
- keep track of two counters for both strings
- once both counters are the same, update the result and slide the window till they aren't the same
'''

def min_window(s, t) -> str:
    if t == '':
        return ''

    l, r = 0, 0
    count_window, count_t = {}, {}
    res, res_len = [-1, -1], len(s)+1

    for i in t:
        count_t[i] = 1 + count_t.get(i, 0)

    have, need = 0, len(count_t)

    while r < len(s):
        count_window[s[r]] = 1 + count_window.get(s[r], 0)

        if s[r] in count_t and count_window[s[r]] == count_t[s[r]]:
            have += 1
        
        while have == need:
            if (r-l+1) < res_len:  # update our result
                res = [l, r]
                res_len = r - l + 1
            
            count_window[s[l]] -= 1  # removing from the left of window

            if s[l] in count_t and count_window[s[l]] < count_t[s[l]]:
                have -= 1
            l += 1
        r += 1
    
    l, r = res
    return s[l:r+1] if res_len != (len(s)+1) else ""


if __name__ == '__main__':
    s1, t1 = "ADOBECODEBANC", "ABC"
    s2, t2 = "a", "a"
    s3, t3 = "a", "aa"
    print(min_window(s1, t1))
    print(min_window(s2, t2))
    print(min_window(s3, t3))