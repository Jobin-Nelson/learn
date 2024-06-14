"""
Created Date: 2024-05-27
Qn: You are given an array nums of non-negative integers. nums is considered
    special if there exists a number x such that there are exactly x numbers in
    nums that are greater than or equal to x.

    Notice that x does not have to be an element in nums.

    Return x if the array is special, otherwise, return -1. It can be proven
    that if nums is special, the value for x is unique.
Link: https://leetcode.com/problems/special-array-with-x-elements-greater-than-or-equal-x/
Notes:
    - use suffix sum
"""
def specialArray(nums: list[int]) -> int:
    N = len(nums)
    freq = [0] * (N+1)

    for n in nums:
        freq[min(N, n)] += 1

    nums_greater_than_or_equal = 0
    for i in range(N, -1, -1):
        nums_greater_than_or_equal += freq[i]
        if i == nums_greater_than_or_equal:
            return i
    return -1

if __name__ == '__main__':
    n1 = [3,5]
    n2 = [0,0]
    n3 = [0,4,3,0,4]

    print(specialArray(n1))
    print(specialArray(n2))
    print(specialArray(n3))
