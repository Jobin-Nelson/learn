"""
Created Date: 2023-03-19
Qn: Design a data structure that supports adding new words and finding if a
    string matches any previously added string.

    Implement the WordDictionary class:

        - WordDictionary() Initializes the object. 
        - void addWord(word) Adds word to the data structure, it can be matched
          later. 
        - bool search(word) Returns true if there is any string in the data
          structure that matches word or false otherwise. word may contain dots
          '.' where dots can be matched with any letter.
Link: https://leetcode.com/problems/design-add-and-search-words-data-structure/
Notes:
    - use trie data structure
"""


class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False


class WordDictionary:
    def __init__(self):
        self.dict = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.dict
        for w in word:
            cur = cur.children.setdefault(w, TrieNode())
        cur.end = True

    def search(self, word: str) -> bool:
        def dfs(node: TrieNode, index: int):
            if index == len(word):
                return node.end

            if word[index] == ".":
                for child in node.children.values():
                    if dfs(child, index + 1):
                        return True

            if word[index] in node.children:
                return dfs(node.children[word[index]], index + 1)
            return False

        return dfs(self.dict, 0)


if __name__ == "__main__":
    w = WordDictionary()
    w.addWord("bad")
    w.addWord("dad")
    w.addWord("mad")
    print(w.search("pad"))
    print(w.search("bad"))
    print(w.search(".ad"))
    print(w.search("b.."))
