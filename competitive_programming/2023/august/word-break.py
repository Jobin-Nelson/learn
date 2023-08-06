'''
Created Date: 2023-08-04
Qn: Given a string s and a dictionary of strings wordDict, return true if s can
    be segmented into a space-separated sequence of one or more dictionary
    words.

    Note that the same word in the dictionary may be reused multiple times in
    the segmentation.
Link: https://leetcode.com/problems/word-break/
Notes:
    - use dp
'''
def wordBreak(s: str, wordDict: list[str]) -> bool:
    n = len(s)
    dp = [False] * (n+1)
    dp[0] = True
    words = set(wordDict)

    for i in range(1, n+1):
        for j in range(i):
            if dp[j] and s[j:i] in words:
                dp[i] = True
                break
    return dp[-1]

if __name__ == '__main__':
    s1, w1 = "leetcode", ["leet", "code"]
    s2, w2 = "applepenapple", ["apple","pen"]
    s3, w3 = "catsandog", ["cats","dog","sand","and","cat"]

    print(wordBreak(s1, w1))
    print(wordBreak(s2, w2))
    print(wordBreak(s3, w3))
