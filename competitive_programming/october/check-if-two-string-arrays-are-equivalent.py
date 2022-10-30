'''
Created Date: 2022-10-25
Qn: Given two string arrays word1 and word2, return true if the two arrays
    represent the same string, and false otherwise.

    A string is represented by an array if the array elements concatenated in
    order forms the string.
Link: https://leetcode.com/problems/check-if-two-string-arrays-are-equivalent/
Notes:
    - naive approach would be to concat to string and compare
    - effective way would be to return False when two char are not the same
'''
def arrayStringsAreEqual(word1: list[str], word2: list[str]) -> bool:
    def gen(wordlist: list[str]):
        for word in wordlist:
            for char in word:
                yield char
        yield None

    for c1, c2 in zip(gen(word1), gen(word2)):
        if c1 != c2: return False
    return True

if __name__ == '__main__':
    w11, w12 = ["ab", "c"], ["a", "bc"]
    w21, w22 = ["a", "cb"], ["ab", "c"]
    w31, w32 = ["abc", "d", "defg"], ["abcddefg"]

    print(arrayStringsAreEqual(w11, w12))
    print(arrayStringsAreEqual(w21, w22))
    print(arrayStringsAreEqual(w31, w32))
