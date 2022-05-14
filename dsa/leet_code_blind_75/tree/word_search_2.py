'''
Qn: Given an m x n board of characters and a list of strings words, return all words on the board.
Link: https://leetcode.com/problems/word-search-ii/
Notes: 
- implement Trie to search for a word by letter
- then implement word search with basic backtracking recursive method
'''
class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False

    def add_word(self, word):
        for w in word:
            if w not in self.children:
                self.children[w] = TrieNode()
            self = self.children[w]
        self.word = True

def findWords(board: list[list[str]], words: list[str]) -> list[str]:
    rows, cols = len(board), len(board[0])
    res, visited = set(), set()

    root = TrieNode()
    for w in words:
        root.add_word(w)


    def dfs(r, c, node, word):
        row_outbound = r < 0 or r == rows
        col_outbound = c < 0 or c == cols
        if row_outbound or col_outbound or (r, c) in visited or board[r][c] not in node.children:
            return
        visited.add((r, c))
        node = node.children[board[r][c]]
        word += board[r][c]
        if node.word:
            res.add(word)
        dfs(r-1, c, node, word)
        dfs(r+1, c, node, word)
        dfs(r, c-1, node, word)
        dfs(r, c+1, node, word)
        visited.remove((r, c))
    
    for r in range(rows):
        for c in range(cols):
            dfs(r, c, root, '')
    return list(res)

if __name__ == '__main__':
    b1 = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]
    w1 = ["oath","pea","eat","rain"]
    b2 = [["a","b"],["c","d"]]
    w2 = ["abcb"]
    print(findWords(b1, w1))
    print(findWords(b2, w2))