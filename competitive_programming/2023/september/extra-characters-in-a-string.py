'''
Created Date: 2023-09-02
Qn: You are given a 0-indexed string s and a dictionary of words dictionary.
    You have to break s into one or more non-overlapping substrings such that
    each substring is present in dictionary. There may be some extra characters
    in s which are not present in any of the substrings.

    Return the minimum number of extra characters left over if you break up s
    optimally.
Link: https://leetcode.com/problems/extra-characters-in-a-string/
Notes:
    - use trie data structure
'''
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

def buildTrie(dictionary: list[str]) -> TrieNode:
    root = TrieNode()
    for word in dictionary:
        node = root
        for char in word:
            node = node.children.setdefault(char, TrieNode())
        node.is_word = True
    return root

def minExtraChar(s: str, dictionary: list[str]) -> int:
    n, root = len(s), buildTrie(dictionary)
    dp = [0] * (n+1)

    for start in range(n-1, -1, -1):
        dp[start] = dp[start + 1] + 1
        node = root
        for end in range(start, n):
            if s[end] not in node.children: break
            node = node.children[s[end]]
            if node.is_word: dp[start] = min(dp[start], dp[end + 1])
    return dp[0]

if __name__ == '__main__':
    s1, d1 = "leetscode", ["leet","code","leetcode"]
    s2, d2 = "sayhelloworld", ["hello","world"]

    print(minExtraChar(s1, d1))
    print(minExtraChar(s2, d2))
