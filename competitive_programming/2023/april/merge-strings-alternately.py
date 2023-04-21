'''
Created Date: 2023-04-18
Qn: You are given two strings word1 and word2. Merge the strings by adding
    letters in alternating order, starting with word1. If a string is longer
    than the other, append the additional letters onto the end of the merged
    string.

    Return the merged string.
Link: https://leetcode.com/problems/merge-strings-alternately/
Notes:
    - use stack
'''
def mergeAlternately(word1: str, word2: str) -> str:
    res = []

    i = j = 0

    while i < len(word1) and j < len(word2):
        res.append(word1[i])
        res.append(word2[j])
        i += 1
        j += 1

    return ''.join(res) + word1[i:] + word2[j:]

if __name__ == '__main__':
    w11, w12 = "abc", "pqr"
    w21, w22 = "ab", "pqrs"

    print(mergeAlternately(w11, w12))
    print(mergeAlternately(w21, w22))
