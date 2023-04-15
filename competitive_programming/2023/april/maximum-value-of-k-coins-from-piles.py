'''
Created Date: 2023-04-15
Qn: There are n piles of coins on a table. Each pile consists of a positive
    number of coins of assorted denominations.

    In one move, you can choose any coin on top of any pile, remove it, and add
    it to your wallet.

    Given a list piles, where piles[i] is a list of integers denoting the
    composition of the ith pile from top to bottom, and a positive integer k,
    return the maximum total value of coins you can have in your wallet if you
    choose exactly k coins optimally.
Link: https://leetcode.com/problems/maximum-value-of-k-coins-from-piles/
Notes:
    - use dfs
'''
import functools

def maxValuesOfCoins(piles: list[list[int]], k: int) -> int:

    @functools.lru_cache(None)
    def dfs(i: int, k: int) -> int:
        if k == 0 or i == len(piles): return 0
        res, cur = dfs(i+1, k), 0

        for j in range(min(len(piles[i]), k)):
            cur += piles[i][j]
            res = max(res, cur + dfs(i+1, k-j-1))
        return res

    return dfs(0, k)

if __name__ == '__main__':
    p1, k1 = [[1,100,3],[7,8,9]], 2
    p2, k2 = [[100],[100],[100],[100],[100],[100],[1,1,1,1,1,1,700]], 7

    print(maxValuesOfCoins(p1, k1))
    print(maxValuesOfCoins(p2, k2))
