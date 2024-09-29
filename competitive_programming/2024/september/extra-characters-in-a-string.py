"""
Created Date: 2024-09-23
Qn: You are given a 0-indexed string s and a dictionary of words dictionary.
    You have to break s into one or more non-overlapping substrings such that
    each substring is present in dictionary. There may be some extra characters
    in s which are not present in any of the substrings.

    Return the minimum number of extra characters left over if you break up s
    optimally.
Link: https://leetcode.com/problems/extra-characters-in-a-string/
Notes:
"""


class TrieNode:
    def __init__(self) -> None:
        self.children = {}
        self.is_word = False


class Trie:
    def __init__(self, words: list[str]) -> None:
        self.root = TrieNode()
        for word in words:
            cur = self.root
            for c in word:
                cur = cur.children.setdefault(c, TrieNode())
            cur.is_word = True


def minExtraChar(s: str, dictionary: list[str]) -> int:
    n = len(s)
    dp = [0] * (n + 1)
    root = Trie(dictionary).root

    for start in range(n - 1, -1, -1):
        dp[start] = dp[start + 1] + 1
        node = root
        for end in range(start, n):
            if s[end] not in node.children:
                break
            node = node.children[s[end]]
            if node.is_word:
                dp[start] = min(dp[start], dp[end + 1])
    return dp[0]


if __name__ == '__main__':
    s1, d1 = "leetscode", ["leet", "code", "leetcode"]
    s2, d2 = "sayhelloworld", ["hello", "world"]

    print(minExtraChar(s1, d1))
    print(minExtraChar(s2, d2))
