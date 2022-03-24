def min_window(s: str, t: str) -> str:
    if t == '': return ''
    l,r = 0, 0
    res, res_len = [-1, -1], len(s)+1
    count_s, count_t = {}, {}

    for c in t:
        count_t[c] = 1 + count_t.get(c, 0)
    have, need = 0, len(count_t)
    
    while r < len(s):
        count_s[s[r]] = 1 + count_s.get(s[r], 0)
        if s[r] in count_t and count_s[s[r]] == count_t[s[r]]:
            have += 1
        while have == need:
            if (r-l+1) < res_len:
                res = [l, r]
                res_len = r-l+1
            count_s[s[l]] -= 1
            if s[l] in count_t and count_s[s[l]] < count_t[s[l]]:
                have -= 1
            l += 1
        r += 1
    l, r = res
    return s[l:r+1] if res_len != (len(s)+1) else ''


if __name__ == '__main__':
    s1, t1 = "ADOBECODEBANC", "ABC"
    s2, t2 = "a", "a"
    s3, t3 = "a", "aa"
    print(min_window(s1, t1))
    print(min_window(s2, t2))
    print(min_window(s3, t3))