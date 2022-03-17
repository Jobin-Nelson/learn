'''
Qn: Given an m x n grid of characters board and a string word, return true if word exists in the grid.
The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.
Link: https://leetcode.com/problems/word-search/
Notes:
- dfs
- similar to number of islands
'''

def exist(board, word):
    rows, cols = len(board), len(board[0])
    path = set()

    def dfs(r, c, i):
        if i == len(word):
            return True
        
        row_inbound = r < 0 or r >= rows
        col_inbound = c < 0 or c >= cols
        if row_inbound or col_inbound or (r, c) in path or board[r][c] != word[i]:
            return False

        path.add((r, c))

        res = (
            dfs(r+1, c, i+1) or
            dfs(r-1, c, i+1) or
            dfs(r, c+1, i+1) or
            dfs(r, c-1, i+1)
        )
        path.remove((r, c))
        return res
    
    for r in range(rows):
        for c in range(cols):
            if dfs(r, c, 0):
                return True
    return False
    

if __name__ == '__main__':
    b1 = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
    w1 = 'ABCCED'
    b2 = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
    w2 = 'SEE'
    b3 = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
    w3 = 'ABCB'
    print(exist(b1, w1))
    print(exist(b2, w2))
    print(exist(b3, w3))