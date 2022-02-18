'''
Qn: Given a string s containing only digits, return the number of ways to decode it.
Link: https://leetcode.com/problems/decode-ways/
Notes:
- breaking the whole problem into subproblems and summing up two different ways when the condition 1|2&(1-6) is met
'''
def num_decodings_tab(self, s: str) -> int:
    dp = {len(s): 1}
    if s[0] == '0':
        return 0
    
    for i in range(len(s)-1, -1, -1):
        if s[i] == '0':
            dp[i] =  0 
        else:
            dp[i] = dp[i+1]

        if (i+1 <= len(s) and (s[i] == '1' or s[i] == '2' and s[i+1]  in '0123456')):
            dp[i] += dp[i+2]
    return dp[0]

def num_decoding(s):
    dp = {len(s): 1}
    def dfs(i):
        if i in dp:
            return dp[i]
        if s[i] == '0':
            return 0
        res = dfs(i + 1)
        if (i+1 < len(s) and (s[i] == '1' or s[i] == '2' and s[i+1] in '0123456')):
            res += dfs(i+2)
        dp[i] = res
        return res
    return dfs(0)


if __name__ == '__main__':
    s1, s2, s3 = '12', '226', '06'
    print(num_decoding(s1))
    print(num_decoding(s2))
    print(num_decoding(s3))
