'''
Created Date: 14-06-2022
Qn: Given two strings word1 and word2, return the minimum number of steps 
    required to make word1 and word2 the same.
    In one step, you can delete exactly one character in either string.
Link: https://leetcode.com/problems/delete-operation-for-two-strings/
Notes:
    -   w o r d 1
      s e a
w   0 1 2 3
o e 1 2 1 2 
r a 2 3 2 1
d t 3 4 3 2
2         ^
          |
    Ans --^
'''
def minDistance(word1: str, word2: str) -> int:
    N, M = len(word1), len(word2)
    dp = [[0 for _ in range(N+1)] for _ in range(M+1)]
    for r in range(N+1):
        dp[0][r] = r

    for c in range(M+1):
        dp[c][0] = c

    for r in range(1, M+1):
        for c in range(1, N+1):
            if word1[c-1] == word2[r-1]:
                dp[r][c] = dp[r-1][c-1]
            else:
                dp[r][c] = 1 + min(dp[r-1][c], dp[r][c-1])
    return dp[-1][-1]

if __name__ == '__main__':
    w11, w12 = 'sea', 'eat'
    w21, w22 = 'leetcode', 'etco'
    print(minDistance(w11, w12))
    print(minDistance(w21, w22))
