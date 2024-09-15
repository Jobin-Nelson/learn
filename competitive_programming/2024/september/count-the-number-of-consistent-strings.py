"""
Created Date: 2024-09-12
Qn: You are given a string allowed consisting of distinct characters and an
    array of strings words. A string is consistent if all characters in the
    string appear in the string allowed.

    Return the number of consistent strings in the array words.
Link: https://leetcode.com/problems/count-the-number-of-consistent-strings/
Notes:
    - use boolean array or bit mask
"""


def countConsistentStrings(allowed: str, words: list[str]) -> int:
    allowed_bits = 0
    ord_a = ord('a')
    for c in allowed:
        allowed_bits |= 1 << (ord(c) - ord_a)

    return sum(all((allowed_bits >> (ord(c)-ord_a)) & 1 for c in s) for s in words)
    # Boolean array
    # lookup = [0] * 26
    # ord_a = ord('a')
    # for c in allowed:
    #     lookup[ord(c) - ord_a] = 1
    # return sum(all(lookup[ord(c) - ord_a] for c in s) for s in words)


if __name__ == '__main__':
    a1, w1 = "ab", ["ad", "bd", "aaab", "baa", "badab"]
    a2, w2 = "abc", ["a", "b", "c", "ab", "ac", "bc", "abc"]
    a3, w3 = "cad", ["cc", "acd", "b", "ba", "bac", "bad", "ac", "d"]

    print(countConsistentStrings(a1, w1))
    print(countConsistentStrings(a2, w2))
    print(countConsistentStrings(a3, w3))
