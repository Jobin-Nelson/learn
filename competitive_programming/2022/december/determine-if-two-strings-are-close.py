'''
Created Date: 2022-12-02
Qn: Two strings are considered close if you can attain one from the other using
    the following operations:

        - Operation 1: Swap any two existing characters. 
            - For example, abcde -> aecdb
        - Operation 2: Transform every occurrence of one existing character
          into another existing character, and do the same with the other
          character. 
            - For example, aacabb -> bbcbaa 
              (all a's turn into b's, and all b's turn into a's) You can use
              the operations on either string as many times as necessary.

    Given two strings, word1 and word2, return true if word1 and word2 are
    close, and false otherwise.
Link: https://leetcode.com/problems/determine-if-two-strings-are-close/
Notes:
    - use hashmap to count the characters
'''
from collections import Counter

def closeStrings(word1: str, word2: str) -> bool:
    count1 = Counter(word1)
    count2 = Counter(word2)

    return sorted(count1.values()) == sorted(count2.values()) and set(count1.keys()) == set(count2.keys())


if __name__ == '__main__':
    w11, w12 = "abc", "bca"
    w21, w22 = "a", "aa"
    w31, w32 = "cabbba", "abbccc"

    print(closeStrings(w11, w12))
    print(closeStrings(w21, w22))
    print(closeStrings(w31, w32))
