"""
Created Date: 2023-12-26
Qn: You have n dice, and each die has k faces numbered from 1 to k.

    Given three integers n, k, and target, return the number of possible ways
    (out of the kn total ways) to roll the dice, so the sum of the face-up
    numbers equals target. Since the answer may be too large, return it modulo
    109 + 7.
Link: https://leetcode.com/problems/number-of-dice-rolls-with-target-sum/
Notes:
    - use tabulation or dfs
"""
def numRollsToTarget(n: int, k: int, target: int) -> int:
    # Tabulation
    dp = [0] * (target+1) # dp[i]  = num of ways to roll i
    dp[0] = 1
    MOD = 10 ** 9 + 7

    for _ in range(n):
        next_dp = [0] * (target + 1)
        for val in range(1, k+1):
            for total in range(val, target + 1):
                next_dp[total] = (next_dp[total] + dp[total-val]) % MOD
        dp = next_dp
    return dp[target]

    # Recursive
    # MOD = 10 ** 9 + 7
    # cache = {}
    # def count(n: int, target: int) -> int:
    #     nonlocal MOD
    #     if n == 0: return int(target == 0)
    #     if (n, target) in cache: return cache[(n, target)]
    #     res = 0
    #     for val in range(1, k+1):
    #         res = (res + count(n-1, target-val)) % MOD
    #     cache[(n, target)] = res
    #     return res
    # return count(n, target) % MOD

if __name__ == '__main__':
    n1, k1, t1 = 1, 6, 3
    n2, k2, t2 = 2, 6, 7
    n3, k3, t3 = 30, 30, 500

    print(numRollsToTarget(n1, k1, t1))
    print(numRollsToTarget(n2, k2, t2))
    print(numRollsToTarget(n3, k3, t3))
