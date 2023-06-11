'''
Created Date: 2023-06-10
Qn: You are given three positive integers: n, index, and maxSum. You want to
    construct an array nums (0-indexed) that satisfies the following
    conditions:

        - nums.length == n
        - nums[i] is a positive integer where 0 <= i < n.
        - abs(nums[i] - nums[i+1]) <= 1 where 0 <= i < n-1.
        - The sum of all the elements of nums does not exceed maxSum.
        - nums[index] is maximized.

    Return nums[index] of the constructed array.

    Note that abs(x) equals x if x >= 0, and -x otherwise.
Link: https://leetcode.com/problems/maximum-value-at-a-given-index-in-a-bounded-array/
Notes:
    - use binary search
    - use search space 1-maxSum
'''
def maxValue(n: int, index: int, maxSum: int) -> int:
    def getSum(index: int, value: int) -> int:
        count = 0
        if value > index:
            count += (value + value - index) * (index + 1) // 2
        else:
            count += (value + 1) * value // 2 + index - value + 1

        if value >= n - index:
            count += (value + value - n + 1 + index) * (n - index) // 2
        else:
            count += (value + 1) * value // 2 + n - index - value
        return count - value
    
    l, r = 1, maxSum
    while l < r:
        m = (l + r + 1) >> 1
        if getSum(index, m) <= maxSum:
            l = m
        else:
            r = m - 1
    return l

if __name__ == '__main__':
    n1, i1, m1 = 4, 2, 6
    n2, i2, m2 = 6, 1, 10

    print(maxValue(n1, i1, m1))
    print(maxValue(n2, i2, m2))
