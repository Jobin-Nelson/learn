'''
Created Date: 2023-03-30
Qn: We can scramble a string s to get a string t using the following algorithm:

    If the length of the string is 1, stop.
    If the length of the string is > 1, do the following:

        - Split the string into two non-empty substrings at a random index,
          i.e., if the string is s, divide it to x and y where s = x + y.
        - Randomly decide to swap the two substrings or to keep them in the
          same order. i.e., after this step, s may become s = x + y or s = y +
          x.
        - Apply step 1 recursively on each of the two substrings x and y.

    Given two strings s1 and s2 of the same length, return true if s2 is a
    scrambled string of s1, otherwise, return false.
Link: https://leetcode.com/problems/scramble-string/
Notes:
    - use dp 3d array
'''
def isScramble(s1: str, s2: str) -> bool:
    if s1 == s2: return True
    if sorted(s1) != sorted(s2): return False

    n = len(s1)
    dp = [[[False] * (n+1) for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            dp[i][j][1] = (s1[i] == s2[j])

    for length in range(2, n+1):
        for i in range(n-length+1):
            for j in range(n-length+1):
                for k in range(1, length):
                    if (dp[i][j][k] and dp[i+k][j+k][length-k]) or (dp[i][j+length-k][k] and dp[i+k][j][length-k]):
                        dp[i][j][length] = True
                        break
    return dp[0][0][n]

if __name__ == '__main__':
    s11, s12  = "great", "rgeat"
    s21, s22  = "abcde", "caebd"
    s31, s32  = "a", "a"

    print(isScramble(s11, s12))
    print(isScramble(s21, s22))
    print(isScramble(s31, s32))
