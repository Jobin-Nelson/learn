'''
Created Date: 2023-10-26
Qn: Given an array of unique integers, arr, where each integer arr[i] is
    strictly greater than 1.

    We make a binary tree using these integers, and each number may be used for
    any number of times. Each non-leaf node's value should be equal to the
    product of the values of its children.

    Return the number of binary trees we can make. The answer may be too large
    so return the answer modulo 109 + 7.
Link: https://leetcode.com/problems/binary-trees-with-factors/
Notes:
    - sort and iterate n^2
'''
def numFactoredBinaryTrees(arr: list[int]) -> int:
    MOD = 10 ** 9 + 7
    arr.sort()
    set_arr = set(arr)

    dp = {i: 1 for i in arr}

    for i in arr:
        for j in arr:
            if j > i ** 0.5: break
            if i % j == 0 and i // j in set_arr:
                if i // j == j:
                    dp[i] += dp[j] * dp[j]
                else:
                    dp[i] += dp[j] * dp[i//j] * 2 # 2 trees can be formed j and i//j also i//j and j as children
                dp[i] %= MOD
    return sum(dp.values()) % MOD

if __name__ == '__main__':
    a1 = [2, 4]
    a2 = [2, 4, 5, 10]

    print(numFactoredBinaryTrees(a1))
    print(numFactoredBinaryTrees(a2))

