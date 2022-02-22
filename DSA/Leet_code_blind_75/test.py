def word_break(s, word_dict):
    dp = [False] * (len(s) + 1)
    dp[len(s)] = True

    i = len(s)
    while i >= 0:
        for w in word_dict:
            if i+len(w) <= len(s) and s[i: i+len(w)] == w:
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
