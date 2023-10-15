'''
Created Date: 2023-10-06
Qn: Given an integer n, break it into the sum of k positive integers, where k
    >= 2, and maximize the product of those integers.

    Return the maximum product you can get.
Link: https://leetcode.com/problems/integer-break/
Notes:
    - use dp
'''
def integerBreak(n: int) -> int:
    dp = { 1 : 1 }
    for num in range(2, n+1):
        dp[num] = 0 if num == n else num
        for i in range(1, num):
            val = dp[i] * dp[num-i]
            dp[num] = max(dp[num], val)
    return dp[n]

if __name__ == '__main__':
    n1 = 2
    n2 = 10

    print(integerBreak(n1))
    print(integerBreak(n2))
