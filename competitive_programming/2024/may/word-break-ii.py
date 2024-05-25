"""
Created Date: 2024-05-25
Qn: Given a string s and a dictionary of strings wordDict, add spaces in s to
    construct a sentence where each word is a valid dictionary word. Return all
    such possible sentences in any order.

    Note that the same word in the dictionary may be reused multiple times in
    the segmentation.
Link: https://leetcode.com/problems/word-break-ii/
Notes:
    - use backtrack
"""
from functools import cache

def wordBreak(s: str, wordDict: list[str]) -> list[str]:
    word_set = set(wordDict)
    @cache
    def backtrack(i: int):
        if i == len(s):
            return [""]
        res = []
        for j in range(i, len(s)):
            w = s[i:j+1]
            if w not in word_set: continue
            strings = backtrack(j+1)
            if not strings: continue
            for sub in strings:
                sentence = w
                if sub: sentence += " " + sub
                res.append(sentence)
        return res
    return backtrack(0)

if __name__ == '__main__':
    s1, w1 = "catsanddog", ["cat","cats","and","sand","dog"]
    s2, w2 = "pineapplepenapple", ["apple","pen","applepen","pine","pineapple"]
    s3, w3 = "catsandog", ["cats","dog","sand","and","cat"]

    print(wordBreak(s1, w1))
    print(wordBreak(s2, w2))
    print(wordBreak(s3, w3))
