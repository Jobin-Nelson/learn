"""
Created Date: 2024-01-07
Qn: Given an integer array nums, return the number of all the arithmetic
    subsequences of nums.

    A sequence of numbers is called arithmetic if it consists of at least three
    elements and if the difference between any two consecutive elements is the
    same.

        For example, [1, 3, 5, 7, 9], [7, 7, 7, 7], and [3, -1, -5, -9] are
        arithmetic sequences. For example, [1, 1, 2, 5, 7] is not an arithmetic
        sequence.

    A subsequence of an array is a sequence that can be formed by removing some
    elements (possibly none) of the array.

        For example, [2,5,10] is a subsequence of [1,2,1,2,4,1,5,10].

    The test cases are generated so that the answer fits in 32-bit integer.
Link: https://leetcode.com/problems/arithmetic-slices-ii-subsequence/
Notes:
    - use dp
"""
from collections import defaultdict

def numberOfArithmeticSlices(nums: list[int]) -> int:
    res, N = 0, len(nums)
    dp = [defaultdict(int) for _ in range(N)]

    for i in range(N):
        for j in range(i):
            diff = nums[i] - nums[j]
            dp[i][diff] += 1 + dp[j][diff]
            res += 1 + dp[j][diff]
    return res - (N*(N-1) // 2)

if __name__ == '__main__':
    n1 = [2,4,6,8,10]
    n2 = [7,7,7,7,7]

    print(numberOfArithmeticSlices(n1))
    print(numberOfArithmeticSlices(n2))
