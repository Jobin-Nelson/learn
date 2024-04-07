"""
Created Date: 2024-04-02
Qn: Given two strings s and t, determine if they are isomorphic.

    Two strings s and t are isomorphic if the characters in s can be replaced
    to get t.

    All occurrences of a character must be replaced with another character
    while preserving the order of characters. No two characters may map to the
    same character, but a character may map to itself.
Link: https://leetcode.com/problems/isomorphic-strings/
Notes:
    - use 2 hashmaps
"""
def isIsomorphic(s: str, t: str) -> bool:
    mapST, mapTS = {}, {}
    for c1, c2 in zip(s, t):
        if (c1 in mapST and mapST[c1] != c2) or (c2 in mapTS and mapTS[c2] != c1):
            return False
        mapST[c1] = c2
        mapTS[c2] = c1
    return True

if __name__ == '__main__':
    s1, t1 = "egg", "add"
    s2, t2 = "foo", "bar"
    s3, t3 = "paper", "title"

    print(isIsomorphic(s1, t1))
    print(isIsomorphic(s2, t2))
    print(isIsomorphic(s3, t3))
