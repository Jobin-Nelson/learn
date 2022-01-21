class Solution:
    def word_break(s: str, word_dict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[len(s)] = True





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
