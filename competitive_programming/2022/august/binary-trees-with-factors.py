'''
Created Date: 09-08-2022
Qn: Given an array of unique integers, arr, where each integer arr[i] is
    strictly greater than 1.

    We make a binary tree using these integers, and each number may be used for
    any number of times. Each non-leaf node's value should be equal to the
    product of the values of its children.

    Return the number of binary trees we can make. The answer may be too large
    so return the answer modulo 109 + 7.
Link: https://leetcode.com/problems/binary-trees-with-factors/
Notes:
'''
from collections import defaultdict

def numFactoredBinaryTrees(arr: list[int]) -> int:
    arr.sort()
    lookup = defaultdict(int)
    N = len(arr)

    for i in range(N):
        temp = 1
        for j in range(i):
            temp += lookup[arr[j]]*lookup[arr[i]/arr[j]]
        lookup[arr[i]] = temp

    return sum(lookup.values()) % (10**9+7)

if __name__ == '__main__':
    a1, a2 = [2, 4], [2, 4, 5, 10]
    print(numFactoredBinaryTrees(a1))
    print(numFactoredBinaryTrees(a2))
