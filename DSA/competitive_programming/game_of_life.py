'''
Qn: 
- Any live cell with fewer than two live neighbors dies as if caused by under-population.
- Any live cell with two or three live neighbors lives on to the next generation.
- Any live cell with more than three live neighbors dies, as if by over-population.
- Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
Link: https://leetcode.com/problems/game-of-life/
Notes: 
'''
def game_of_life(board: list[list[int]]) -> None:
    # Original | New | State
    # 0        | 0   | 0
    # 1        | 0   | 1
    # 0        | 1   | 2
    # 1        | 1   | 3

    rows, cols = len(board), len(board[0])

    def count_neighbors(r, c):
        nei = 0
        for i in range(r-1, r+2):
            for j in range(c-1, c+2):
                if ((i==r and j==c) or i<0 or j<0 or i==rows or j==cols):
                    continue
                if board[i][j] in [1, 3]:
                    nei += 1
        return nei

    for r in range(rows):
        for c in range(cols):
            nei = count_neighbors(r, c)
            if board[r][c]:
                if nei in [2, 3]:
                    board[r][c] = 3
            elif nei == 3:
                    board[r][c] = 2
    
    for r in range(rows):
        for c in range(cols):
            board[r][c] = 0 if board[r][c] < 2 else 1


if __name__ == '__main__':
    b1 = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
    b2 = [[1,1],[1,0]]
    game_of_life(b1)
    game_of_life(b2)
    print(b1)
    print(b2)