"""
Created Date: 2024-08-20
Qn: Alice and Bob continue their games with piles of stones.  There are a
    number of piles arranged in a row, and each pile has a positive integer
    number of stones piles[i].  The objective of the game is to end with the
    most stones. 

    Alice and Bob take turns, with Alice starting first.  Initially, M = 1.

    On each player's turn, that player can take all the stones in the first X
    remaining piles, where 1 <= X <= 2M.  Then, we set M = max(M, X).

    The game continues until all the stones have been taken.

    Assuming Alice and Bob play optimally, return the maximum number of stones
    Alice can get.
Link: https://leetcode.com/problems/stone-game-ii/
Notes:
    - use dfs
"""

from functools import cache
from sys import maxsize


def stoneGameII(piles: list[int]) -> int:
    @cache
    def dfs(isAlice: bool, ind: int, m: int) -> int:
        N = len(piles)
        if ind == N:
            return 0
        total = 0
        res = 0 if isAlice else maxsize
        for i in range(1, min(N-ind+1, 2 * m + 1)):
            total += piles[ind + i - 1]
            dfs_res = dfs(not isAlice, ind + i, max(i, m))
            if isAlice:
                res = max(res, total + dfs_res)
            else:
                res = min(res, dfs_res)
        return res

    return dfs(True, 0, 1)


if __name__ == '__main__':
    p1 = [2, 7, 9, 4, 4]
    p2 = [1, 2, 3, 4, 5, 100]

    print(stoneGameII(p1))
    print(stoneGameII(p2))
