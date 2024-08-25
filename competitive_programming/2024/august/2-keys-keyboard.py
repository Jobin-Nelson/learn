"""
Created Date: 2024-08-19
Qn: There is only one character 'A' on the screen of a notepad. You can perform
    one of two operations on this notepad for each step:

    - Copy All: You can copy all the characters present on the screen (a
      partial copy is not allowed). 
    - Paste: You can paste the characters which are copied last time. 

    Given an integer n, return the minimum number of operations to
    get the character 'A' exactly n times on the screen.
Link: https://leetcode.com/problems/2-keys-keyboard/
Notes:
    - use dp
"""


def minSteps(n: int) -> int:
    dp = [1000] * (n + 1)
    dp[1] = 0

    for i in range(2, n + 1):
        for j in range(1, 1 + (i >> 1)):
            if i % j == 0:
                dp[i] = min(dp[i], dp[j] + i // j)
    return dp[n]


if __name__ == '__main__':
    n1 = 3
    n2 = 1

    print(minSteps(n1))
    print(minSteps(n2))
