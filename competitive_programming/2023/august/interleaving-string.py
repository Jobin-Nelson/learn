'''
Created Date: 2023-08-25
Qn: Given strings s1, s2, and s3, find whether s3 is formed by an interleaving
    of s1 and s2.

    An interleaving of two strings s and t is a configuration where s and t are
    divided into n and m substrings respectively, such that:

        s = s1 + s2 + ... + sn t = t1 + t2 + ... + tm |n - m| <= 1 The
        interleaving is s1 + t1 + s2 + t2 + s3 + t3 + ... or t1 + s1 + t2 + s2
        + t3 + s3 + ...

    Note: a + b is the concatenation of strings a and b.
Link: https://leetcode.com/problems/interleaving-string/
Notes:
    - use dfs or dynamic programming
'''
def isInterleave(s1: str, s2: str, s3: str) -> bool:
    # dp
    N1, N2, N3 = len(s1), len(s2), len(s3)
    if N1 + N2 != N3: return False
    dp = [[False] * (N2+1) for _ in range(N1+1)]
    dp[N1][N2] = True

    for i in range(N1, -1, -1):
        for j in range(N2, -1, -1):
            if i < N1 and s1[i] == s3[i+j] and dp[i+1][j]: dp[i][j] = True
            if j < N2 and s2[j] == s3[i+j] and dp[i][j+1]: dp[i][j] = True
    return dp[0][0]

    # dfs
    # N1, N2, N3 = len(s1), len(s2), len(s3)
    # def dfs(i: int, j: int) -> bool:
    #     if i == N1 and j == N2 and (i+j) == N3: return True
    #     if i < N1 and s1[i] == s3[i+j] and dfs(i+1, j): return True
    #     if j < N2 and s2[j] == s3[i+j] and dfs(i, j+1): return True
    #     return False
    # return dfs(0, 0)

if __name__ == '__main__':
    s11, s12, s13 = "aabcc", "dbbca", "aadbbcbcac"
    s21, s22, s23 = "aabcc", "dbbca", "aadbbbaccc"
    s31, s32, s33 = "", "", ""

    print(isInterleave(s11, s12, s13))
    print(isInterleave(s21, s22, s23))
    print(isInterleave(s31, s32, s33))
