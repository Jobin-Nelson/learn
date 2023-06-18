'''
Created Date: 2023-06-13
Qn: Given a 0-indexed n x n integer matrix grid, return the number of pairs
    (ri, cj) such that row ri and column cj are equal.

    A row and column pair is considered equal if they contain the same elements
    in the same order (i.e., an equal array).
Link: https://leetcode.com/problems/equal-row-and-column-pairs/
Notes:
    - use trie
'''
class TrieNode:
    def __init__(self):
        self.count = 0
        self.children = {}

class Trie:
    def __init__(self):
        self.trie = TrieNode()

    def insert(self, array: list[int]):
        trie = self.trie

        for a in array:
            if a not in trie.children:
                trie.children[a] = TrieNode()
            trie = trie.children[a]
        trie.count += 1

    def search(self, array) -> int:
        trie = self.trie

        for a in array:
            if a in trie.children:
                trie = trie.children[a]
            else:
                return 0
        return trie.count

def equalPairs(grid: list[list[int]]) -> int:
    trie = Trie()
    res = 0
    N = len(grid)

    for row in grid:
        trie.insert(row)

    for c in range(N):
        cols = [grid[i][c] for i in range(N)]
        res += trie.search(cols)
    return res

if __name__ == '__main__':
    g1 = [[3,2,1],[1,7,6],[2,7,7]]
    g2 = [[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]

    print(equalPairs(g1))
    print(equalPairs(g2))
