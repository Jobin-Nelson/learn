"""
Created Date: 2024-01-27
Qn: For an integer array nums, an inverse pair is a pair of integers [i, j]
    where 0 <= i < j < nums.length and nums[i] > nums[j].

    Given two integers n and k, return the number of different arrays consist
    of numbers from 1 to n such that there are exactly k inverse pairs. Since
    the answer can be huge, return it modulo 109 + 7.
Link: https://leetcode.com/problems/k-inverse-pairs-array/
Notes:
    - use eq: dp[n][k] = dp[n][k-1] + dp[n-1][k] - dp[n-1][k-n]
"""
def kInversePairs(n: int, k: int) -> int:
    prev = [0] * (k+1)
    prev[0] = 1
    mod = 10 ** 9 + 7

    for i in range(1, n+1):
        cur = [0] * (k+1)
        cur[0] = 1
        for j in range(1, k+1):
            cur[j] = (cur[j-1] + prev[j] - (prev[j-i] if j-i>=0 else 0)) % mod
        prev = cur
    return prev[k] % mod


if __name__ == '__main__':
    n1, k1 = 3, 0
    n2, k2 = 3, 1
    n3, k3 = 3, 2

    print(kInversePairs(n1, k1))
    print(kInversePairs(n2, k2))
    print(kInversePairs(n3, k3))

