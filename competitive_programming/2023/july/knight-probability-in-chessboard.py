'''
Created Date: 2023-07-22
Qn: On an n x n chessboard, a knight starts at the cell (row, column) and
    attempts to make exactly k moves. The rows and columns are 0-indexed, so
    the top-left cell is (0, 0), and the bottom-right cell is (n - 1, n - 1).

    A chess knight has eight possible moves it can make, as illustrated below.
    Each move is two cells in a cardinal direction, then one cell in an
    orthogonal direction. Each time the knight is to move, it chooses one of
    eight possible moves uniformly at random (even if the piece would go off
    the chessboard) and moves there.

    The knight continues moving until it has made exactly k moves or has moved
    off the chessboard.

    Return the probability that the knight remains on the board after it has
    stopped moving.
Link: https://leetcode.com/problems/knight-probability-in-chessboard/
Notes:
    - use dp
    - use two 2d arrays to store prev_dp and cur_dp
    - cur_dp will calculate the probability that the knight stays on the board
      from the prev_dp
'''
def knightProbability(n: int, k: int, row: int, column: int) -> float:
    dirs = [(1, 2), (1, -2), (-1, 2), (-1, -2),(2, 1), (2, -1), (-2, 1), (-2, -1)]
    prev_dp = [[0] * n for _ in range(n)]
    cur_dp = [[0] * n for _ in range(n)]

    prev_dp[row][column] = 1

    for _ in range(k):
        for i in range(n):
            for j in range(n):
                cur_dp[i][j] = 0
                for dx, dy in dirs:
                    di, dj = i - dx, j - dy
                    if 0 <= di < n and 0 <= dj < n:
                        cur_dp[i][j] += prev_dp[di][dj] / 8
        prev_dp, cur_dp = cur_dp, prev_dp
    return sum(prev_dp[i][j] for i in range(n) for j in range(n))

if __name__ == '__main__':
    n1, k1, r1, c1 = 3, 2, 0, 0
    n2, k2, r2, c2 = 1, 0, 0, 0

    print(knightProbability(n1, k1, r1, c1))
    print(knightProbability(n2, k2, r2, c2))

