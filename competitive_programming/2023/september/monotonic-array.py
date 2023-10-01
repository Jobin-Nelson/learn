'''
Created Date: 2023-09-29
Qn: An array is monotonic if it is either monotone increasing or monotone
    decreasing.

    An array nums is monotone increasing if for all i <= j, nums[i] <= nums[j].
    An array nums is monotone decreasing if for all i <= j, nums[i] >= nums[j].

    Given an integer array nums, return true if the given array is monotonic,
    or false otherwise.
Link: https://leetcode.com/problems/monotonic-array/
Notes:
'''
def isMonotonic(nums: list[int]) -> bool:
    dec = inc = True
    for i in range(len(nums)-1):
        if nums[i] > nums[i+1]:
            inc = False
        if nums[i] < nums[i+1]:
            dec = False
    return inc or dec

if __name__ == '__main__':
    n1 = [1,2,2,3]
    n2 = [6,5,4,3]
    n3 = [1,3,2]

    print(isMonotonic(n1))
    print(isMonotonic(n2))
    print(isMonotonic(n3))
