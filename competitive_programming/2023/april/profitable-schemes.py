'''
Created Date: 2023-04-21
Qn: There is a group of n members, and a list of various crimes they could
    commit. The ith crime generates a profit[i] and requires group[i] members
    to participate in it. If a member participates in one crime, that member
    can't participate in another crime.

    Let's call a profitable scheme any subset of these crimes that generates at
    least minProfit profit, and the total number of members participating in
    that subset of crimes is at most n.

    Return the number of schemes that can be chosen. Since the answer may be
    very large, return it modulo 109 + 7.
Link: https://leetcode.com/problems/profitable-schemes/
Notes:
    - use dp
'''
def profitableSchemes(n: int, minProfit: int, group: list[int], profit: list[int]) -> int:
    MOD = 10**9 + 7
    dp = [[0] * (n+1) for _ in range(minProfit + 1)]
    dp[0][0] = 1

    for g, p in zip(group, profit):
        for i in range(minProfit, -1, -1):
            for j in range(n-g, -1, -1):
                dp[min(i+p, minProfit)][j+g] += dp[i][j]
                dp[min(i+p, minProfit)][j+g] %= MOD
    return sum(dp[minProfit]) % MOD

if __name__ == '__main__':
    n1, mp1, g1, p1 = 5, 3, [2,2], [2,3]
    n2, mp2, g2, p2 = 10, 5, [2,3,5], [6,7,8]

    print(profitableSchemes(n1, mp1, g1, p1))
    print(profitableSchemes(n2, mp2, g2, p2))
