"""
Created Date: 2024-05-24
Qn: Given a list of words, list of  single letters (might be repeating) and
    score of every character.

    Return the maximum score of any valid set of words formed by using the
    given letters (words[i] cannot be used two or more times).

    It is not necessary to use all characters in letters and each letter can
    only be used once. Score of letters 'a', 'b', 'c', ... ,'z' is given by
    score[0], score[1], ... , score[25] respectively.
Link: https://leetcode.com/problems/maximum-score-words-formed-by-letters/
Notes:
    - use backtracking
"""
from collections import Counter

def maxScoreWords(words: list[str], letters: list[str], score: list[int]) -> int:
    words_count = [Counter(word) for word in words]
    letters_count = Counter(letters)

    def backtrack(i: int) -> int:
        if i == len(words): return 0
        res = backtrack(i+1)
        if all(words_count[i][c] <= letters_count[c] for c in words[i]):
            for c in words[i]: letters_count[c] -= 1
            res = max(res, sum(score[ord(c) - ord('a')] for c in words[i]) + backtrack(i+1))
            for c in words[i]: letters_count[c] += 1
        return res
    return backtrack(0)

if __name__ == '__main__':
    w1, l1, s1 = ["dog","cat","dad","good"], ["a","a","c","d","d","d","g","o","o"], [1,0,9,5,0,0,3,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0]
    w2, l2, s2 = ["xxxz","ax","bx","cx"], ["z","a","b","c","x","x","x"], [4,4,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,5,0,10]
    w3, l3, s3 = ["leetcode"], ["l","e","t","c","o","d"], [0,0,1,1,1,0,0,0,0,0,0,1,0,0,1,0,0,0,0,1,0,0,0,0,0,0]

    print(maxScoreWords(w1, l1, s1))
    print(maxScoreWords(w2, l2, s2))
    print(maxScoreWords(w3, l3, s3))
