'''
Created Date: 2023-10-28
Qn: Given an integer n, your task is to count how many strings of length n can
    be formed under the following rules:

        - Each character is a lower case vowel ('a', 'e', 'i', 'o', 'u')
        - Each vowel 'a' may only be followed by an 'e'.
        - Each vowel 'e' may only be followed by an 'a' or an 'i'.
        - Each vowel 'i' may not be followed by another 'i'.
        - Each vowel 'o' may only be followed by an 'i' or a 'u'.
        - Each vowel 'u' may only be followed by an 'a'.

    Since the answer may be too large, return it modulo 10^9 + 7.
Link: https://leetcode.com/problems/count-vowels-permutation/
Notes:
    - use dp
'''
def countVowelsPermutation(n: int) -> int:
    N = len('aeiou')
    MOD = 10 ** 9 + 7

    dp = [1] * N
    a, e, i, o, u = range(N)

    for _ in range(2, n+1):
        ndp = [0] * N
        ndp[a] = (dp[e] + dp[i] + dp[u]) % MOD
        ndp[e] = (dp[a] + dp[i]) % MOD
        ndp[i] = (dp[e] + dp[o]) % MOD
        ndp[o] = dp[i]
        ndp[u] = (dp[i] + dp[o]) % MOD
        dp = ndp
    return sum(dp) % MOD

if __name__ == '__main__':
    n1 = 1
    n2 = 2
    n3 = 5

    print(countVowelsPermutation(n1))
    print(countVowelsPermutation(n2))
    print(countVowelsPermutation(n3))
