'''
Created Date: 2022-10-02
Qn: You have n dice and each die has k faces numbered from 1 to k.

    Given three integers n, k, and target, return the number of possible ways
    (out of the k^n total ways) to roll the dice so the sum of the face-up
    numbers equals target. Since the answer may be too large, return it modulo
    10^9 + 7.
Link: https://leetcode.com/problems/number-of-dice-rolls-with-target-sum/
Notes:
    - memoization and dfs
'''
def numRollsToTarget(n: int, k: int, target: int) -> int:
    memo = {}

    def dp(dice, target):
        if dice == 0: return 1 if not target else 0
        elif target < 0: return 0
        elif (dice, target) in memo: 
            return memo[(dice, target)]

        res = 0

        for num in range(1, k + 1):
            res += dp(dice - 1, target - num)
        memo[(dice, target)] = res
        return res 
    return dp(n, target) % (10^9 + 7)

if __name__ == '__main__':
    n1, k1, t1 = 1, 6, 3
    n2, k2, t2 = 2, 6, 7
    n3, k3, t3 = 30, 30, 500

    print(numRollsToTarget(n1, k1, t1))
    print(numRollsToTarget(n2, k2, t2))
    print(numRollsToTarget(n3, k3, t3))
