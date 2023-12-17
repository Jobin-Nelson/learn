"""
Created Date: 2023-12-16
Qn: Given two strings s and t, return true if t is an anagram of s, and false
    otherwise.

    An Anagram is a word or phrase formed by rearranging the letters of a
    different word or phrase, typically using all the original letters exactly
    once.
Link: https://leetcode.com/problems/valid-anagram/
Notes:
    - use array to count the number of characters in each string
"""
def isAnagram(s: str, t: str) -> bool:
    sc, tc = [0] * 26, [0] * 26
    for c in s:
        sc[ord(c) - ord('a')] += 1
    for c in t:
        tc[ord(c) - ord('a')] += 1
    return tc == sc
 
if __name__ == '__main__':
    s1, t1 = "anagram", "nagaram"
    s2, t2 = "rat", "car"

    print(isAnagram(s1, t1))
    print(isAnagram(s2, t2))
