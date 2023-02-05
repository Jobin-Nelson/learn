'''
Created Date: 2023-02-04
Qn: Given two strings s1 and s2, return true if s2 contains a permutation of
    s1, or false otherwise.

    In other words, return true if one of s1's permutations is the substring of
    s2.
Link: https://leetcode.com/problems/permutation-in-string/
Notes:
    - use an array to hold the count of each characters
    - use integer variable to hold the frequency of matched characters
    - return frequency == 26
'''
def checkInclusion(s1: str, s2: str) -> bool:
    if len(s2) < len(s1): return False
    s1_count = [0] * 26
    s2_count = [0] * 26
    n = len(s1)
    for i in range(n):
        s1_count[ord(s1[i]) - 97] += 1
        s2_count[ord(s2[i]) - 97] += 1

    count = 0

    for i in range(26):
        if s1_count[i] == s2_count[i]:
            count += 1

    for i in range(len(s2) - n):
        l, r = ord(s2[i]) - 97, ord(s2[i+n]) - 97
        if count == 26: return True

        s2_count[r] += 1
        if s1_count[r] == s2_count[r]:
            count += 1
        elif s1_count[r] + 1 == s2_count[r]:
            count -= 1

        s2_count[l] -= 1
        if s1_count[l] == s2_count[l]:
            count += 1
        elif s1_count[l] - 1 == s2_count[l]:
            count -= 1
    return count == 26

if __name__ == '__main__':
    s11, s12 = "ab", "eidbaooo"
    s21, s22 = "ab", "eidboaoo"

    print(checkInclusion(s11, s12))
    print(checkInclusion(s21, s22))
