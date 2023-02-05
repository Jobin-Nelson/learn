'''
Created Date: 2023-01-27
Qn: Given an array of strings words (without duplicates), return all the
    concatenated words in the given list of words.

    A concatenated word is defined as a string that is comprised entirely of at
    least two shorter words in the given array.
Link: https://leetcode.com/problems/concatenated-words/
Notes:
    - use dfs
    - check if each substring is present in wordset
    - if present recursively check till rest of the substring is present too
    - append to answer if the dfs returns true
'''
def findAllConcatenatedWordsInDict(words: list[str]) -> list[str]:
    wordset = set(words)
    res = []

    def dfs(word: str, wordset: set) -> bool:
        if word == '': return True
        for i in range(len(word)):
            if word[:i+1] in wordset:
                if dfs(word[i+1:], wordset):
                    return True
        return False

    for word in words:
        wordset.remove(word)
        if dfs(word, wordset): res.append(word)
        wordset.add(word)
    return res

if __name__ == '__main__':
    w1 = ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]
    w2 = ["cat","dog","catdog"]

    print(findAllConcatenatedWordsInDict(w1))
    print(findAllConcatenatedWordsInDict(w2))
