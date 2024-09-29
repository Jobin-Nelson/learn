"""
Created Date: 2024-09-25
Qn: You are given an array words of size n consisting of non-empty strings.

    We define the score of a string word as the number of strings words[i] such
    that word is a prefix of words[i].

    For example, if words = ["a", "ab", "abc", "cab"], then the score of "ab"
    is 2, since "ab" is a prefix of both "ab" and "abc". Return an array answer
    of size n where answer[i] is the sum of scores of every non-empty prefix of
    words[i].

    Note that a string is considered as a prefix of itself.
Link: https://leetcode.com/problems/sum-of-prefix-scores-of-strings/
Notes:
    - use trie
"""


class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.prefix_count = 0


def sumPrefixScores(words: list[str]) -> list[int]:
    root = TrieNode()
    res = [1] * len(words)
    ord_a = ord('a')

    for word in words:
        cur = root
        for c in word:
            c_ind = ord(c) - ord_a
            if cur.children[c_ind] is None:
                cur.children[c_ind] = TrieNode()
            cur.children[c_ind].prefix_count += 1
            cur = cur.children[c_ind]

    for i, word in enumerate(words):
        cur = root
        count = 0
        for c in word:
            c_ind = ord(c) - ord_a
            count += cur.children[c_ind].prefix_count
            cur = cur.children[c_ind]
        res[i] = count
    return res


if __name__ == '__main__':
    w1 = ["abc", "ab", "bc", "b"]
    w2 = ["abcd"]

    print(sumPrefixScores(w1))
    print(sumPrefixScores(w2))
