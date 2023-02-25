'''
Created Date: 2023-02-21
Qn: You are given a sorted array consisting of only integers where every
    element appears exactly twice, except for one element which appears exactly
    once.

    Return the single element that appears only once.

    Your solution must run in O(log n) time and O(1) space.
Link: https://leetcode.com/problems/single-element-in-a-sorted-array/
Notes:
    - use binary search
'''
def singleNonDuplicate(nums: list[int]) -> int:
    l, r = 0, len(nums) - 1
    while l <= r:
        m = (r + l) >> 1
        if nums[m] != nums[m-1] and nums[m] != nums[m+1]:
            return nums[m]
        elif (m & 1 == 0 and nums[m] == nums[m+1]) or (m & 1 == 1 and nums[m] == nums[m-1]):
            l = m + 1
        else:
            r = m - 1
    return nums[l]

if __name__ == '__main__':
    n1 = [1,1,2,3,3,4,4,8,8]
    n2 = [3,3,7,7,10,11,11]
    
    print(singleNonDuplicate(n1))
    print(singleNonDuplicate(n2))
