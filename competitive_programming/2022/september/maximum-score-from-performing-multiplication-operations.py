'''
Created Date: 2022-09-16
Qn: You are given two integer arrays nums and multipliers of size n and m
    respectively, where n >= m. The arrays are 1-indexed.

    You begin with a score of 0. You want to perform exactly m operations. On the
    ith operation (1-indexed), you will:

        - Choose one integer x from either the start or the end of the array nums.
        - Add multipliers[i] * x to your score. 
        - Remove x from the array nums. 
    Return the maximum score after performing m operations.
Link: https://leetcode.com/problems/maximum-score-from-performing-multiplication-operations/
Notes:
    - dynamic programming
'''
def maximumScore(nums: list[int], multipliers: list[int]) -> int:
    N, M = len(nums), len(multipliers)

    dp = [ max(multipliers[M-1] * nums[lo], multipliers[M-1] * nums[N-M+lo]) for lo in range(M) ]

    for i in range(M-2, -1, -1):
        for lo in range(i+1):
            hi = N - (i - lo) - 1
            c1 = multipliers[i] * nums[lo] + dp[lo+1]
            c2 = multipliers[i] * nums[hi] + dp[lo]
            dp[lo] = max(c1, c2)
    return dp[0]

if __name__ == '__main__':
    n1, m1 = [1, 2, 3], [3, 2, 1]
    n2, m2 = [-5, -3, -3, -2, 7, 1], [-10, -5, 3, 4, 6]

    print(maximumScore(n1, m1))
    print(maximumScore(n2, m2))
