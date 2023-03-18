'''
Created Date: 2023-03-17
Qn: A trie (pronounced as "try") or prefix tree is a tree data structure used
    to efficiently store and retrieve keys in a dataset of strings. There are
    various applications of this data structure, such as autocomplete and
    spellchecker.

    Implement the Trie class:

        - Trie() Initializes the trie object. 
        - void insert(String word) Inserts the string word into the trie. 
        - boolean search(String word) Returns true if the string word is in the
          trie (i.e., was inserted before), and false otherwise. 
        - boolean startsWith(String prefix) Returns true if there is a
          previously inserted string word that has the prefix prefix, and false
          otherwise.
Link: https://leetcode.com/problems/implement-trie-prefix-tree/
Notes:
    - use hashmap
    - marker to indicate end of word
'''
class Trie:
    def __init__(self):
        self.children = {}
        self.end = False

    def insert(self, word: str) -> None:
        node = self
        for w in word:
            if w not in node.children:
                node.children[w] = Trie()
            node = node.children[w]
        node.end = True

    def search(self, word: str) -> bool:
        node = self
        for w in word:
            if w not in node.children:
                return False
            node = node.children[w]
        return node.end

    def startsWith(self, prefix: str) -> bool:
        node = self
        for w in prefix:
            if w not in node.children:
                return False
            node = node.children[w]
        return True

if __name__ == '__main__':
    t = Trie()
    t.insert('apple')
    print(t.search('apple'))
    print(t.search('app'))
    print(t.startsWith('app'))
    t.insert('app')
    print(t.search('app'))
    
