'''
Created Date: 2023-09-23
Qn: You are given an array of words where each word consists of lowercase
    English letters.

    wordA is a predecessor of wordB if and only if we can insert exactly one
    letter anywhere in wordA without changing the order of the other characters
    to make it equal to wordB.

        For example, "abc" is a predecessor of "abac", while "cba" is not a
        predecessor of "bcad".

    A word chain is a sequence of words [word1, word2, ..., wordk] with k >= 1,
    where word1 is a predecessor of word2, word2 is a predecessor of word3, and
    so on. A single word is trivially a word chain with k == 1.

    Return the length of the longest possible word chain with words chosen from
    the given list of words.
Link: https://leetcode.com/problems/longest-string-chain/
Notes:
    - use dfs
'''
def longestStrChain(words: list[str]) -> int:
    s = set(words)
    memo = {}

    def dfs(word: str) -> int:
        if word not in s: return 0
        if word in memo: return memo[word]
        res = 0
        for i in range(len(word)):
            res = max(res, 1 + dfs(word[:i] + word[i+1:]))
        memo[word] = res
        return res
    return max(dfs(word) for word in words)

if __name__ == '__main__':
    w1 = ["a","b","ba","bca","bda","bdca"]
    w2 = ["xbc","pcxbcf","xb","cxbc","pcxbc"]
    w3 = ["abcd","dbqca"]

    print(longestStrChain(w1))
    print(longestStrChain(w2))
    print(longestStrChain(w3))
