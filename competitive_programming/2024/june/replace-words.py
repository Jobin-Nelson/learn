"""
Created Date: 2024-06-07
Qn: In English, we have a concept called root, which can be followed by some
    other word to form another longer word - let's call this word derivative.
    For example, when the root "help" is followed by the word "ful", we can
    form a derivative "helpful".

    Given a dictionary consisting of many roots and a sentence consisting of
    words separated by spaces, replace all the derivatives in the sentence with
    the root forming it. If a derivative can be replaced by more than one root,
    replace it with the root that has the shortest length.

    Return the sentence after the replacement.
Link: https://leetcode.com/problems/replace-words/
Notes:
    - use trie or iterate over prefix
"""
class TrieNode:
    def __init__(self):
        self.is_end = False
        self.children = [None] * 26

class Trie:
    def __init__(self):
        self.root = TrieNode()
    def insert(self, word: str) -> None:
        current = self.root
        for c in word:
            id = ord(c) - ord('a')
            if current.children[id] is None:
                current.children[id] = TrieNode()
            current = current.children[id]
        current.is_end = True
    def shortest_root(self, word: str) -> str:
        current = self.root
        for i, c in enumerate(word):
            id = ord(c) - ord('a')
            if current.children[id] is None:
                return word
            current = current.children[id]
            if current.is_end:
                return word[:i+1]
        return word

def replaceWords(dictionary: list[str], sentence: str) -> str:
    words = sentence.split()
    roots = Trie()

    for root in dictionary:
        roots.insert(root)

    for i, word in enumerate(words):
        words[i] = roots.shortest_root(word)
    return ' '.join(words)

    # words = sentence.split()
    # roots = set(dictionary)
    # for i in range(len(words)):
    #     for j in range(len(words[i])):
    #         if words[i][:j] in roots:
    #             words[i] = words[i][:j]
    #             break
    # return ' '.join(words)

if __name__ == '__main__':
    d1, s1 = ["cat","bat","rat"], "the cattle was rattled by the battery"
    d2, s2 = ["a","b","c"], "aadsfasf absbs bbab cadsfafs"

    print(replaceWords(d1, s1))
    print(replaceWords(d2, s2))
