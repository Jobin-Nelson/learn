'''
Created Date: 2023-07-31
Qn: Given two strings s1 and s2, return the lowest ASCII sum of deleted
    characters to make two strings equal.
Link: https://leetcode.com/problems/minimum-ascii-delete-sum-for-two-strings/
Notes:
    - use dp
'''
def minimumDeleteSum(s1: str, s2: str) -> int:
    m, n = len(s1), len(s2)
    dp = [[0] * (n+1) for _ in range(m+1)]

    for i in range(1, m+1):
        dp[i][0] = dp[i-1][0] + ord(s1[i-1])
    for j in range(1, n+1):
        dp[0][j] = dp[0][j-1] + ord(s2[j-1])

    for i in range(1, m+1):
        for j in range(1, n+1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = min(
                    dp[i-1][j] + ord(s1[i-1]),
                    dp[i][j-1] + ord(s2[j-1])
                )
    return dp[m][n]

if __name__ == '__main__':
    s11, s12 = "sea", "eat"
    s21, s22 = "delete", "leet"

    print(minimumDeleteSum(s11, s12))
    print(minimumDeleteSum(s21, s22))
