"""
Created Date: 2024-09-18
Qn: Given a list of non-negative integers nums, arrange them such that they
    form the largest number and return it.

    Since the result may be very large, so you need to return a string instead
    of an integer.
Link: https://leetcode.com/problems/largest-number/
Notes:
    - use custom sorting function
"""


def largestNumber(nums: list[int]) -> str:
    nums = list(map(str, nums))
    nums.sort(key=lambda x: x * 10, reverse=True)
    if nums[0] == '0': return '0'
    return ''.join(map(str, nums))


if __name__ == '__main__':
    n1 = [10, 2]
    n2 = [3, 30, 34, 5, 9]

    print(largestNumber(n1))
    print(largestNumber(n2))
