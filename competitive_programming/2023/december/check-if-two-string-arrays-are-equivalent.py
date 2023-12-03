"""
Created Date: 2023-12-01
Qn: Given two string arrays word1 and word2, return true if the two arrays
    represent the same string, and false otherwise.

    A string is represented by an array if the array elements concatenated in
    order forms the string.
Link: https://leetcode.com/problems/check-if-two-string-arrays-are-equivalent/
Notes:
    - use 2 pointers one for word and another for string
"""
def arrayStringsAreEqual(word1: list[str], word2: list[str]):
    w1p, w2p = 0, 0
    s1p, s2p = 0, 0
    N1, N2 = len(word1), len(word2)
    while w1p < N1 and w2p < N2:
        if word1[w1p][s1p] != word2[w2p][s2p]:
            return False
        s1p += 1
        s2p += 1
        if s1p == len(word1[w1p]):
            w1p += 1
            s1p = 0
        if s2p == len(word2[w2p]):
            w2p += 1
            s2p = 0
    return w1p == N1 and w2p == N2
            
    # def next_char(word: list[str]):
    #     for w in word:
    #         for c in w:
    #             yield c
    # return all(c1 == c2 for c1, c2 in zip(next_char(word1), next_char(word2)))

if __name__ == '__main__':
    w11, w12 = ["ab", "c"], ["a", "bc"]
    w21, w22 = ["a", "cb"], ["ab", "c"]
    w31, w32 = ["abc", "d", "defg"], ["abcddefg"]

    print(arrayStringsAreEqual(w11, w12))
    print(arrayStringsAreEqual(w21, w22))
    print(arrayStringsAreEqual(w31, w32))
