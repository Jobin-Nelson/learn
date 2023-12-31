"""
Created Date: 2023-12-31
Qn: Given a string s, return the length of the longest substring between two
    equal characters, excluding the two characters. If there is no such
    substring return -1.

    A substring is a contiguous sequence of characters within a string.
Link: https://leetcode.com/problems/largest-substring-between-two-equal-characters/
Notes:
    - use stack to track the first index, and get the max length afterwards
"""
def maxLengthBetweenEqualCharacters(s: str) -> int:
    start = [-1] * 26
    res = -1

    for i, c in enumerate(s):
        id = ord(c) - ord('a')
        if start[id] == -1:
            start[id] = i
        else:
            res = max(res, i-start[id]-1)
    return res



if __name__ == '__main__':
    s1 = "aa"
    s2 = "abca"
    s3 = "cbxy"

    print(maxLengthBetweenEqualCharacters(s1))
    print(maxLengthBetweenEqualCharacters(s2))
    print(maxLengthBetweenEqualCharacters(s3))
