'''
Qn: Given two strings text1 and text2, return the length of their longest common subsequence. If there is no common subsequence, return 0.
Link: https://leetcode.com/problems/longest-common-subsequence/
Notes:
- breaking the whole problem into subproblems and incrementing 1 when the condition is satisfied from the bottom (last element) to top (first element)
'''
# 2D matrix dynamic programming
def long_com_subseq(text1: str, text2: str) -> int:
    dp = [[0 for _ in range(len(text2)+1)] for _ in range(len(text1)+1)]

    for i in range(len(text1) -1, -1, -1):
        for j in range(len(text2) -1, -1, -1):
            if text1[i] == text2[j]:
                dp[i][j] = 1 + dp[i+1][j+1]
            else:
                dp[i][j] = max(dp[i+1][j], dp[i][j+1])

    return dp[0][0]

if __name__ == '__main__':
    t11, t12 = 'abcde', 'ace'
    t21, t22 = 'abc', 'abc'
    t31, t32 = 'abc', 'def'
    t41, t42 = 'ezupkr', 'ubmrapg'
    print(long_com_subseq(t11, t12))
    print(long_com_subseq(t21, t22))
    print(long_com_subseq(t31, t32))
    print(long_com_subseq(t41, t42))
