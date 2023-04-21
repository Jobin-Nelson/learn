'''
Created Date: 2023-04-16
Qn: You are given a list of strings of the same length words and a string target.

    Your task is to form target using the given words under the following
    rules:

        - target should be formed from left to right. 
        - To form the ith character (0-indexed) of target, you can choose the
          kth character of the jth string in words if target[i] = words[j][k]. 
        - Once you use the kth character of the jth string of words, you can no
          longer use the xth character of any string in words where x <= k. In
          other words, all characters to the left of or at index k become
          unusuable for every string. 
        - Repeat the process until you form the string target.

    Notice that you can use multiple characters from the same string in words
    provided the conditions above are met.

    Return the number of ways to form target from words. Since the answer may
    be too large, return it modulo 109 + 7.
Link: https://leetcode.com/problems/number-of-ways-to-form-a-target-string-given-a-dictionary/
Notes:
    - use dfs and memoization
'''
from collections import defaultdict

def numWays(words: list[str], target: str) -> int:
    mod = 10**9 + 7

    cnt = defaultdict(int)

    for w in words:
        for i, c in enumerate(w):
            cnt[(i, c)] += 1

    dp = {}

    def dfs(i: int, k: int) -> int:
        if i == len(target): return 1
        if k == len(words[0]): return 0

        if (i, k) in dp: return dp[(i, k)]

        c = target[i]

        dp[(i, k)] = dfs(i, k+1)
        dp[(i, k)] += cnt[(k, c)] * dfs(i+1, k+1)

        return dp[(i, k)] % mod
    
    return dfs(0, 0)

if __name__ == '__main__':
    w1, t1 = ["acca","bbbb","caca"], "aba"
    w2, t2 = ["abba","baab"], "bab"

    print(numWays(w1, t1))
    print(numWays(w2, t2))
