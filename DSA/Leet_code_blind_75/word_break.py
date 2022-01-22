class Solution:
    def word_break(self, s: str, word_dict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[len(s)] = True

        for i in range(len(s)-1, -1, -1):
            for word in word_dict:
                if (i+len(word) <= len(s)) and (str[i:i+len(word)]==word):
                    dp[i] = dp[i+len(word)]
                if dp[i]:
                    break

        return dp[0]

    def word_break_memo(self, s, word_dict, memo=None):
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
