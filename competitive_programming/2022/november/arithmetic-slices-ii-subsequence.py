'''
Created Date: 2022-11-27
Qn: Given an integer array nums, return the number of all the arithmetic
    subsequences of nums.

    A sequence of numbers is called arithmetic if it consists of at least three
    elements and if the difference between any two consecutive elements is the
    same.

        - For example, [1, 3, 5, 7, 9], [7, 7, 7, 7], and [3, -1, -5, -9] are
          arithmetic sequences. 
        - For example, [1, 1, 2, 5, 7] is not an arithmetic sequence. 

    A subsequence of an array is a sequence that can be formed by removing some
    elements (possibly none) of the array.

        - For example, [2,5,10] is a subsequence of [1,2,1,2,4,1,5,10]. The
          test cases are generated so that the answer fits in 32-bit integer.
Link: https://leetcode.com/problems/arithmetic-slices-ii-subsequence/
Notes:
    - use dp
    - store (diff: count) add previous count to result
'''
from collections import defaultdict

def numberOfArithmeticSlices(nums: list[int]) -> int:
    N = len(nums)
    dp = [defaultdict(int) for _ in range(N)]
    res = 0

    for i in range(N):
        for j in range(i):
            diff = nums[i] - nums[j]
            count = dp[j][diff]
            dp[i][diff] += count + 1
            res += count
    return res

if __name__ == '__main__':
    n1 = [2, 4, 6, 8, 10]
    n2 = [7, 7, 7, 7, 7]

    print(numberOfArithmeticSlices(n1))
    print(numberOfArithmeticSlices(n2))
