"""
Created Date: 2024-03-11
Qn: You are given two strings order and s. All the characters of order are
    unique and were sorted in some custom order previously.

    Permute the characters of s so that they match the order that order was
    sorted. More specifically, if a character x occurs before a character y in
    order, then x should occur before y in the permuted string.

    Return any permutation of s that satisfies this property.
Link: https://leetcode.com/problems/custom-sort-string/
Notes:
    - sort with key from order
    - use counter to create a new string
"""
from sys import maxsize
from collections import Counter

def customSortString(order: str, s: str) -> str:
    counter = Counter(s)
    res = []
    for c in order:
        res.append(c * counter[c])
        counter[c] = 0
    for k, v in counter.items():
        if v == 0: continue
        res.append(k * v)

    return ''.join(res)
    # sort with key
    # lookup = [maxsize] * 26
    # cutoff = ord('a')
    # for i, c in enumerate(order):
    #     lookup[ord(c) - cutoff] = i
    #
    # return ''.join(sorted(s, key=lambda x: lookup[ord(x)-cutoff]))

if __name__ == '__main__':
    o1, s1 = "cba", "abcd"
    o2, s2 = "bcafg", "abcd"

    print(customSortString(o1, s1))
    print(customSortString(o2, s2))
