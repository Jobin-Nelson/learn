'''
Created Date: 2023-09-01
Qn: Given an integer n, return an array ans of length n + 1 such that for each
    i (0 <= i <= n), ans[i] is the number of 1's in the binary representation
    of i.
Link: https://leetcode.com/problems/counting-bits/
Notes:
    - use dp
'''
def countBits(n: int) -> list[int]:
    dp = [0] * (n + 1)
    offset = 1

    for i in range(1, n+1):
        if offset * 2 == i: offset = i
        dp[i] = 1 + dp[i-offset]
    return dp

if __name__ == '__main__':
    n1 = 2
    n2 = 5

    print(countBits(n1))
    print(countBits(n2))
