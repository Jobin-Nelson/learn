'''
Created Date: 2022-11-05
Qn: Given an m x n board of characters and a list of strings words, return all
    words on the board.

    Each word must be constructed from letters of sequentially adjacent cells,
    where adjacent cells are horizontally or vertically neighboring. The same
    letter cell may not be used more than once in a word.
Link: https://leetcode.com/problems/word-search-ii/
Notes:
    - use Trie data structure
    - so that you can just traverse the board recursively only just once
'''
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

    def add_word(self, word):
        cur = self
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.is_word = True

def findWords(board: list[list[str]], words: list[str]) -> list[str]:
    root = TrieNode()
    for word in words:
        root.add_word(word)

    m, n = len(board), len(board[0])
    res, visited = set(), set()
    def dfs(r: int, c: int, node: TrieNode, word: str):
        row_outbound = r < 0 or r == m
        col_outbound = c < 0 or c == n

        if row_outbound or col_outbound or (r, c) in visited or board[r][c] not in node.children:
            return False
        visited.add((r, c))
        node = node.children[board[r][c]]
        word += board[r][c]
        if node.is_word: res.add(word)
        dfs(r+1, c, node, word)
        dfs(r-1, c, node, word)
        dfs(r, c+1, node, word)
        dfs(r, c-1, node, word)
        visited.remove((r, c))

    for r in range(m):
        for c in range(n):
            dfs(r, c, root, "")
    return list(res)

if __name__ == '__main__':
    b1 = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]
    w1 = ["oath","pea","eat","rain"]
    b2 = [["a","b"],["c","d"]]
    w2 = ["abcb"]

    print(findWords(b1, w1))
    print(findWords(b2, w2))
