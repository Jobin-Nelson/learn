def get_combination(s, word_bank):
    dp = [None for i in range(len(s)+1)]
    dp[0] = [[]]

    for i in range(len(s)):
        if dp[i]:
            for word in word_bank:
                word_len = len(word)
                if s[i:i+word_len] == word:
                    combination = list(map(lambda x: [*x, word], dp[i]))
                    dp[i+word_len].extend(combination) 
    return dp[len(s)+1]