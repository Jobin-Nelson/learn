"""
Created Date: 2023-11-27
Qn: The chess knight has a unique movement, it may move two squares vertically
    and one square horizontally, or two squares horizontally and one square
    vertically (with both forming the shape of an L). The possible movements of
    chess knight are shown in this diagaram:

    A chess knight can move as indicated in the chess diagram below:

    We have a chess knight and a phone pad as shown below, the knight can only
    stand on a numeric cell (i.e. blue cell).

    Given an integer n, return how many distinct phone numbers of length n we
    can dial.

    You are allowed to place the knight on any numeric cell initially and then
    you should perform n - 1 jumps to dial a number of length n. All jumps
    should be valid knight jumps.

    As the answer may be very large, return the answer modulo 109 + 7.
Link: https://leetcode.com/problems/knight-dialer/
Notes:
    - use iterative approach
"""
def knightDialer(n: int) -> int:
    MOD = 10 ** 9 + 7
    prev_dp = [1] * 10
    jumps = [
        [4, 6],
        [6, 8],
        [7, 9],
        [4, 8],
        [3, 9, 0],
        [],
        [1, 7, 0],
        [2, 6],
        [1, 3],
        [2, 4]
    ]

    for _ in range(n-1):
        dp = [0] * 10
        for square in range(10):
            dp[square] = sum(prev_dp[next_square] % MOD for next_square in jumps[square])
        prev_dp = dp
    return sum(prev_dp) % MOD


    # states
    # if n == 1:
    #     return 10
    # A = 4
    # B = 2
    # C = 2
    # D = 1
    # MOD = 10 ** 9 + 7
    #
    # for _ in range(n-1):
    #     A, B, C, D = (2 * (B + C)) % MOD, A, (A + 2 * D) % MOD, C
    # return (A + B + C + D) % MOD

    # mod = 10**9 + 7
    # phone_dial = [list(range(s, s+3)) for s in range(1, 10, 3)]
    # phone_dial.append([-1, 0, -1])
    # m, n = len(phone_dial), len(phone_dial[0])
    # dirs = [(-1, 2), (1, 2), (2, 1), (2, -1), (-1, -2), (1, -2), (-2, -1), (-2, 1)]
    #
    # def dfs(x: int, y: int, no: str) -> int:
    #     if len(no) == n: return 1
    #     res = 0
    #     for dx, dy in dirs:
    #         nx, ny = x + dx, y + dy
    #         if 0 <= nx < m and 0 <= ny < n and phone_dial[nx][ny] >= 0:
    #             res += dfs(nx, ny, no+str(phone_dial[nx][ny])) % mod
    #     return res % mod
    #
    # return  sum(
    #     dfs(i, j, str(phone_dial[i][j]))
    #     for i in range(m)
    #     for j in range(n)
    #     if phone_dial[i][j] >= 0
    # ) % mod

if __name__ == '__main__':
    n1 = 1
    n2 = 2
    n3 = 3131

    print(knightDialer(n1))
    print(knightDialer(n2))
    print(knightDialer(n3))
