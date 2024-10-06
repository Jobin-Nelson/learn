"""
Created Date: 2024-10-06
Qn: You are given two strings sentence1 and sentence2, each representing a
    sentence composed of words. A sentence is a list of words that are
    separated by a single space with no leading or trailing spaces. Each word
    consists of only uppercase and lowercase English characters.

    Two sentences s1 and s2 are considered similar if it is possible to insert
    an arbitrary sentence (possibly empty) inside one of these sentences such
    that the two sentences become equal. Note that the inserted sentence must
    be separated from existing words by spaces.
Link: https://leetcode.com/problems/sentence-similarity-iii/
Notes:
    - use two pointer
"""


def areSentencesSimilar(sentence1: str, sentence2: str) -> bool:
    s1 = sentence1.split()
    s2 = sentence2.split()
    if len(s2) < len(s1):
        s1, s2 = s2, s1

    l1 = 0
    while l1 < len(s1) and s1[l1] == s2[l1]:
        l1 += 1

    r1, r2 = len(s1) - 1, len(s2) - 1
    while r1 >= l1 and r2 >= 0 and s1[r1] == s2[r2]:
        r1, r2 = r1 - 1, r2 - 1
    return l1 > r1


if __name__ == '__main__':
    s11, s12 = "My name is Haley", "My Haley"
    s21, s22 = "of", "A lot of words"
    s31, s32 = "of", "A lot of words"

    print(areSentencesSimilar(s11, s12))
    print(areSentencesSimilar(s21, s22))
    print(areSentencesSimilar(s31, s32))
