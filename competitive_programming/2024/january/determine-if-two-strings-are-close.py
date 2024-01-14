"""
Created Date: 2024-01-14
Qn: Two strings are considered close if you can attain one from the other using
    the following operations:

        - Operation 1: Swap any two existing characters. 
            - For example, abcde -> aecdb
        - Operation 2: Transform every occurrence of one existing character
          into another existing character, and do the same with the other
          character.
            - For example, aacabb -> bbcbaa (all a's turn into b's, and all b's
              turn into a's)

    You can use the operations on either string as many times as necessary.

    Given two strings, word1 and word2, return true if word1 and word2 are
    close, and false otherwise.
Link: https://leetcode.com/problems/determine-if-two-strings-are-close/
Notes:
    - check letters and frequencies to be equal
    - we can make them equal as long as there frequencies are the same
"""
from collections import Counter


def closeStrings(word1: str, word2: str) -> bool:
    c1, c2 = Counter(word1), Counter(word2)
    n1, n2 = Counter(c1.values()), Counter(c2.values())
    return c1 == c2 or (n1 == n2 and set(word1) == set(word2))
    # N = len(word1)
    # if N != len(word2): return False
    # c1, c2 = [0]*26, [0]*26
    # n1, n2 = {}, {}
    # cutoff = ord('a')
    # for i in range(N):
    #     c1[ord(word1[i])-cutoff] += 1
    #     c2[ord(word2[i])-cutoff] += 1
    # for v1, v2 in zip(c1, c2):
    #     if (v1 == 0 or v2 == 0) and v1+v2 > 0:
    #         return False
    #     n1[v1] = n1.get(v1, 0) + 1
    #     n2[v2] = n2.get(v2, 0) + 1
    # return n1 == n2

if __name__ == '__main__':
    w11, w12 = "abc", "bca"
    w21, w22 = "a", "aa"
    w31, w32 = "cabbba", "abbccc"

    print(closeStrings(w11, w12))
    print(closeStrings(w21, w22))
    print(closeStrings(w31, w32))

