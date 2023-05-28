'''
Created Date: 2023-05-26
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
    - calculate only alice stones
    - maximize alice stones and minimize alice stones when it is bob's turn
'''
def stoneGameII(piles: list[int]) -> int:
    N = len(piles)
    dp = {}

    def dfs(alice: bool, i: int, M: int) -> int:
        if i == N: return 0
        if (alice, i, M) in dp: return dp[(alice, i, M)]

        res = 0 if alice else float('inf')
        total = 0

        for X in range(1, 2*M+1):
            if i + X > N: break
            total += piles[i+X-1]

            cur_res = dfs(not alice, i+X, max(M, X))
            if alice:
                res = max(res, total + cur_res)
            else:
                res = min(res, cur_res)
        dp[(alice, i, M)] = res
        return res
    return dfs(True, 0, 1)

if __name__ == '__main__':
    p1 = [2,7,9,4,4]
    p2 = [1,2,3,4,5,100]

    print(stoneGameII(p1))
    print(stoneGameII(p2))
