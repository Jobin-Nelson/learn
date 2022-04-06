'''
Qn: Design a data structure that supports adding new words and finding if a string matches any previously added string.
Link: https://leetcode.com/problems/design-add-and-search-words-data-structure/
Notes:
'''
class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def add_word(self, word: str) -> None:
        cur = self.root
        for w in word:
            if w not in cur.children:
                cur.children[w] = TrieNode()
            cur = cur.children[w]
        cur.endOfWord = True

    def search(self, word: str) -> bool:
        def dfs(j, root):
            cur = root
            for i in range(j, len(word)):
                c = word[i]
                if c == '.':
                    for child in cur.children.values():
                        if dfs(i+1, child):
                            return True
                    return False
                else:
                    if c not in cur.children:
                        return False
                    cur = cur.children[c]
            return cur.endOfWord
        return dfs(0, self.root)



if __name__ == '__main__':
    word_dictionary = WordDictionary()
    word_dictionary.add_word('bad')
    word_dictionary.add_word('dad')
    word_dictionary.add_word('mad')
    print(word_dictionary.search('pad'))
    print(word_dictionary.search('bad'))
    print(word_dictionary.search('.ad'))
    print(word_dictionary.search('.ad'))