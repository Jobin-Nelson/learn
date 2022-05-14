'''
Qn: Given two strings s and t, return true if t is an anagram of s, and false otherwise.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
Link: https://leetcode.com/problems/valid-anagram/
Notes: 
- compare counter for both strings
'''

def is_anagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    count_s, count_t = {}, {}

    for i in range(len(s)):
        count_t[s[i]] = 1 + count_t.get(s[i], 0)
        count_s[t[i]] = 1 + count_s.get(t[i], 0)
    
    for c in count_s:
        if count_s[c] != count_t.get(c, 0):
            return False
    return True


if __name__ == '__main__':
    s1, t1 = "anagram", "nagaram"
    s2, t2 = "rat", "car"
    print(is_anagram(s1, t1))
    print(is_anagram(s2, t2))