'''
Created Date: 2023-04-22
Qn: Given a string s. In one step you can insert any character at any index of
    the string.

    Return the minimum number of steps to make s palindrome.

    A Palindrome String is one that reads the same backward as well as forward.
Link: https://leetcode.com/problems/minimum-insertion-steps-to-make-a-string-palindrome/
Notes:
    - use longest common subsequence
    - return length of string - lcs
'''
def minInsertions(s: str) -> int:
    n = len(s)
    dp = [0] * n
    dpPrev = [0] * n

    for start in range(n - 1, -1, -1):
        dp[start] = 1
        for end in range(start + 1, n):
            if s[start] == s[end]:
                dp[end] = dpPrev[end - 1] + 2
            else:
                dp[end] = max(dpPrev[end], dp[end - 1])
        dpPrev = dp[:]

    return n - dp[n-1]

if __name__ == '__main__':
    s1 = "zzazz"
    s2 = "mbadm"
    s3 = "leetcode"

    print(minInsertions(s1))
    print(minInsertions(s2))
    print(minInsertions(s3))
