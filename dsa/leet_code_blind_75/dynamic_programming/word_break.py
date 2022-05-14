'''
Qn: Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words
Link: https://leetcode.com/problems/word-break/
Notes:
- can be solved both by recursively and tabulation
- bottom up approach keep track of bool value from the last element up to the first element
'''
# memoization
def word_break_memo(s, word_dict, memo=None):
    if memo == None:
        memo = dict()

    if s in memo:
        return memo[s]

    if s == '':
        return True
    
    for word in word_dict:
        if s.startswith(word):
            if word_break_memo(s[len(word):], word_dict, memo):
                memo[s] = True
                return True

    memo[s] = False
    return False

# tabulation
def word_break(s, word_dict):
    dp = [False] * (len(s)+1)
    dp[-1] = True
    i = len(s)-1
    while i >= 0:
        for w in word_dict:
            if (i+len(w) <= len(s)) and (s[i:i+len(w)] == w):
                dp[i] = dp[i+len(w)]
            if dp[i]:
                break
        i -= 1
    return dp[0]


if __name__ == '__main__':
    s1, w1  = 'leetcode', ['leet', 'code']
    s2, w2 = 'applepenapple', ['apple', 'pen']
    s3, w3 = 'catsandog', ['cats', 'dog', 'sand', 'and', 'cat']
    print(word_break(s1, w1))
    print(word_break(s2, w2))
    print(word_break(s3, w3))
