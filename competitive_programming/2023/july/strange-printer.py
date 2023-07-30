'''
Created Date: 2023-07-30
Qn: There is a strange printer with the following two special properties:

        - The printer can only print a sequence of the same character each
          time.
        - At each turn, the printer can print new characters starting from and
          ending at any place and will cover the original existing characters.

    Given a string s, return the minimum number of turns the printer needed to
    print it.
Link: https://leetcode.com/problems/strange-printer/
Notes:
    - use dp
'''
def strangePrinter(s: str) -> int:
    n = len(s)
    dp = [[n]*n for _ in range(n)]

    for length in range(1, n+1):
        for left in range(n-length+1):
            right = left + length - 1
            j = -1
            for i in range(left, right):
                if s[i] != s[right] and j == -1:
                    j = i
                if j != -1:
                    dp[left][right] = min(dp[left][right], 1 + dp[j][i] + dp[i+1][right])
            if j == -1:
                dp[left][right] = 0
    return dp[0][n-1] + 1

if __name__ == '__main__':
    i1 = "aaabbb"
    i2 = "aba"

    print(strangePrinter(i1))
    print(strangePrinter(i2))
