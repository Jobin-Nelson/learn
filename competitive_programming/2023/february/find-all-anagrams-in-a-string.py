'''
Created Date: 2023-02-05
Qn: Given two strings s and p, return an array of all the start indices of p's
    anagrams in s. You may return the answer in any order.

    An Anagram is a word or phrase formed by rearranging the letters of a
    different word or phrase, typically using all the original letters exactly
    once.
Link: https://leetcode.com/problems/find-all-anagrams-in-a-string/
Notes:
    - use sliding window technique
    - use array for storing count of each character
    - use integer variable to keep count of matched characters
'''
def findAnagrams(s: str, p: str) -> list[int]:
    pl, sl = len(p), len(s)
    if pl > sl: return []

    pmap = [0] * 26
    smap = [0] * 26
    l, r = 0 , pl

    for i in range(pl):
        pmap[ord(p[i]) - 97] += 1
        smap[ord(s[i]) - 97] += 1

    equals = sum(1 for i in range(26) if pmap[i] == smap[i])

    res = []
    while r < sl:
        l_val, r_val = ord(s[l]) - 97, ord(s[r]) - 97
        if equals == 26:
            res.append(l)

        smap[l_val] -= 1
        diff = smap[l_val] - pmap[l_val]
        if diff == 0:
            equals += 1
        elif diff == -1:
            equals -= 1

        smap[r_val] += 1
        diff = smap[r_val] - pmap[r_val]
        if diff == 0:
            equals += 1
        elif diff == 1:
            equals -= 1

        r += 1
        l += 1

    if equals == 26: res.append(l)
    return res
        
if __name__ == '__main__':
    s1, p1 = "cbaebabacd", "abc"
    s2, p2 = "abab", "ab"
    
    print(findAnagrams(s1, p1))
    print(findAnagrams(s2, p2))
