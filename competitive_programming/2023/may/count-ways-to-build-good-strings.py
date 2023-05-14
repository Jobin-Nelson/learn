'''
Created Date: 2023-05-13
Qn: Given the integers zero, one, low, and high, we can construct a string by
    starting with an empty string, and then at each step perform either of the
    following:

        Append the character '0' zero times. Append the character '1' one
        times.

    This can be performed any number of times.

    A good string is a string constructed by the above process having a length
    between low and high (inclusive).

    Return the number of different good strings that can be constructed
    satisfying these properties. Since the answer can be large, return it
    modulo 109 + 7.
Link: https://leetcode.com/problems/count-ways-to-build-good-strings/
Notes:
    - use dp
    - at any position you have two choices add zeroes or ones
'''
def countGoodStrings(low: int, high: int, zero: int, one: int) -> int:
    dp = [0] * (high+1)
    dp[0] = 1
    mod = 10**9 + 7

    for i in range(min(zero, one), high+1):
        dp[i] = (dp[i-zero] + dp[i-one]) % mod
    return sum(dp[low:high+1]) % mod

    # recursive
    # mod = 10**9 + 7
    # def dfs(i: int) -> int:
    #     if i > high: return 0
    #     res = 1  if i >= low else 0
    #     res += dfs(i+zero)
    #     res += dfs(i+one)
    #     return res % mod
    # return dfs(0)

if __name__ == '__main__':
    l1, h1, z1, o1 = 3, 3, 1, 1
    l2, h2, z2, o2 = 2, 3, 1, 2

    print(countGoodStrings(l1, h1, z1, o1))
    print(countGoodStrings(l2, h2, z2, o2))

