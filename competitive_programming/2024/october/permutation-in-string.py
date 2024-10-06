"""
Created Date: 2024-10-05
Qn: Given two strings s1 and s2, return true if s2 contains a permutation of
    s1, or false otherwise.

    In other words, return true if one of s1's permutations is the substring of
    s2.
Link: https://leetcode.com/problems/permutation-in-string/
Notes:
    - use sliding window
"""


def checkInclusion(s1: str, s2: str) -> bool:
    if len(s1) > len(s2):
        return False
    s1len = len(s1)
    s2len = len(s2)
    s1count = [0] * 26
    s2count = [0] * 26
    ord_a = ord('a')

    for i in range(s1len):
        s1count[ord(s1[i]) - ord_a] += 1
        s2count[ord(s2[i]) - ord_a] += 1


    count = sum(s1count[i] == s2count[i] for i in range(26))

    for i in range(s2len - s1len):
        if count == 26:
            return True
        l = ord(s2[i]) - ord_a
        r = ord(s2[i + s1len]) - ord_a

        s2count[r] += 1
        if s1count[r] == s2count[r]:
            count += 1
        elif s1count[r] + 1 == s2count[r]:
            count -= 1

        s2count[l] -= 1
        if s1count[l] == s2count[l]:
            count += 1
        elif s1count[l] - 1 == s2count[l]:
            count -= 1
    return count == 26


if __name__ == '__main__':
    s11, s12 = "ab", "eidbaooo"
    s21, s22 = "ab", "eidboaoo"
    s31, s32 = "abc", "ccccbbbbaaaa"
    s41, s42 = "adc", "dcda"

    print(checkInclusion(s11, s12))
    print(checkInclusion(s21, s22))
    print(checkInclusion(s31, s32))
    print(checkInclusion(s41, s42))
