'''
Created Date: 2022-11-24
Qn: Given an m x n grid of characters board and a string word, return true if
    word exists in the grid.

    The word can be constructed from letters of sequentially adjacent cells,
    where adjacent cells are horizontally or vertically neighboring. The same
    letter cell may not be used more than once.
Link: https://leetcode.com/problems/word-search/
Notes:
    - use dfs backtracking
'''
def exist(board: list[list[str]], word: str) -> bool:
    R, C = len(board), len(board[0])
    N = len(word)
    visited = set()

    def dfs(r: int, c: int, i: int) -> bool:
        if i == N: return True
        row_outbound = r < 0 or r >= R
        col_outbound = c < 0 or c >= C
        if row_outbound or col_outbound or (r, c) in visited or board[r][c] != word[i]:
            return False
        visited.add((r, c))
        res = (dfs(r+1, c, i+1) or 
                dfs(r-1, c, i+1) or 
                dfs(r, c-1, i+1) or 
                dfs(r, c+1, i+1))
        visited.remove((r, c))
        return res

    for r in range(R):
        for c in range(C):
            if dfs(r, c, 0):
                return True
    return False

if __name__ == '__main__':
    b1, w1 = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCED"
    b2, w2 = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "SEE"
    b3, w3 = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCB"

    print(exist(b1, w1))
    print(exist(b2, w2))
    print(exist(b3, w3))
