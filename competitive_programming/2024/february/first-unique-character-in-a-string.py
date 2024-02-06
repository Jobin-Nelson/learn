"""
Created Date: 2024-02-05
Qn: Given a string s, find the first non-repeating character in it and return
    its index. If it does not exist, return -1.
Link: https://leetcode.com/problems/first-unique-character-in-a-string/
Notes:
    - use counter and get the first index that has frequency of 1
"""
def first_uniq_char(s: str) -> int:
    counts = [0] * 26
    offset = ord('a')

    for i, c in enumerate(s):
        counts[ord(c)-offset] += 1

    for i, c in enumerate(s):
        if counts[ord(c)-offset] == 1: return i

    return -1

if __name__ == '__main__':
    s1 = "leetcode"
    s2 = "loveleetcode"
    s3 = "aabb"

    print(first_uniq_char(s1))
    print(first_uniq_char(s2))
    print(first_uniq_char(s3))
