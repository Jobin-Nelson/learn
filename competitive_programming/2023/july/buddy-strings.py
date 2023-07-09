'''
Created Date: 2023-07-03
Qn: Given two strings s and goal, return true if you can swap two letters in s
    so the result is equal to goal, otherwise, return false.

    Swapping letters is defined as taking two indices i and j (0-indexed) such
    that i != j and swapping the characters at s[i] and s[j].

        - For example, swapping at indices 0 and 2 in "abcd" results in "cbad".

Link: https://leetcode.com/problems/buddy-strings/
Notes:
    - two pointers
'''
def buddyStrings(s: str, goal: str) -> bool:
    if len(s) != len(goal): return False
    if s == goal:
        frequency = [0] * 26
        for c in s:
            id = ord(c) - ord('a')
            frequency[id] += 1
            if frequency[id] == 2: return True
        return False
    l = r = -1
    for i in range(len(s)):
        if s[i] != goal[i]:
            if l == -1:
                l = i
            elif r == -1:
                r = i
            else:
                return False
    if r == -1: return False
    return s[l] == goal[r] and s[r] == goal[l]

if __name__ == '__main__':
    s1, g1 = "ab", "ba"
    s2, g2 = "ab", "ab"
    s3, g3 = "aa", "aa"

    print(buddyStrings(s1, g1))
    print(buddyStrings(s2, g2))
    print(buddyStrings(s3, g3))
