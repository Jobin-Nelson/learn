'''
Created Date: 20-06-2022
Qn: A valid encoding of an array of words is any reference string s and array of 
    indices indices such that:
        - words.length == indices.length
        - The reference string s ends with the '#' character.
        - For each index indices[i], the substring of s starting from indices[i] and 
          up to (but not including) the next '#' character is equal to words[i].
    Given an array of words, return the length of the shortest reference string s 
    possible of any valid encoding of words.
Link: https://leetcode.com/problems/short-encoding-of-words/
Notes:
    - use set to eliminate suffix words and return length of reference string
    - use suffix trie and track the length of each word in trie return the sum of length
'''
class TrieNode:
    def __init__(self):
        self.children = {}

class Trie:
    def __init__(self):
        self.root = TrieNode()
        self.ends = []

    def insert(self, words):
        root = self.root
        for c in words:
            root.children.setdefault(c, TrieNode())
            root = root.children[c]
        self.ends.append((root, len(words)+1))

def minimumLengthEncoding(words: list[str]) -> int:
    # Trie method
    words = list(set(words))
    t = Trie()
    for w in words:
        t.insert(w[::-1])
    return sum([depth for node, depth in t.ends if len(node.children) == 0])

    # Set method
    # N = len(words)
    # W = set(words)
    # for w in words:
    #     M = len(w)
    #     for j in range(1, M):
    #         W.discard(w[-j:])
    # return len('#'.join(w for w in W) + '#')

if __name__ == '__main__':
    w1 = ["time", "me", "bell"]
    w2 = ['t']
    print(minimumLengthEncoding(w1))
    print(minimumLengthEncoding(w2))
