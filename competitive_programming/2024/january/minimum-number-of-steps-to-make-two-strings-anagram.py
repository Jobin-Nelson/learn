"""
Created Date: 2024-01-13
Qn: You are given two strings of the same length s and t. In one step you can
    choose any character of t and replace it with another character.

    Return the minimum number of steps to make t an anagram of s.

    An Anagram of a string is a string that contains the same characters with a
    different (or the same) ordering.
Link: https://leetcode.com/problems/minimum-number-of-steps-to-make-two-strings-anagram/
Notes:
    - use counter
"""
def minSteps(s: str, t: str) -> int:
    n = 26
    cs, ct = [0] * n, [0] * n

    for i in range(len(s)):
        cs[ord(s[i]) - ord('a')] += 1
        ct[ord(t[i]) - ord('a')] += 1
    return sum(ct[i]-cs[i] for i in range(n) if ct[i] - cs[i] > 0)

if __name__ == '__main__':
    s1, t1 = "bab", "aba"
    s2, t2 = "leetcode", "practice"
    s3, t3 = "anagram", "mangaar"

    print(minSteps(s1, t1))
    print(minSteps(s2, t2))
    print(minSteps(s3, t3))
