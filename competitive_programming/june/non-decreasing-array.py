'''
Created Date: 25-06-2022
Qn: Given an array nums with n integers, your task is to check if it could 
    become non-decreasing by modifying at most one element.
    We define an array is non-decreasing if nums[i] <= nums[i + 1] holds 
    for every i (0-based) such that (0 <= i <= n - 2).
Link: https://leetcode.com/problems/non-decreasing-array/
Notes:
- if order is broken we have two choices
    - nums[i] = nums[i+1] # When nums[i-1] <= nums[i+1]
    - nums[i+1] = nums[i] # else
'''
def checkPossibility(nums: list[int]) -> bool:
    changed = False

    for i in range(len(nums)-1):
        if nums[i] > nums[i+1]:
            if changed: return False
            if i==0 or nums[i-1] <= nums[i+1]:
                nums[i] = nums[i+1]
            else:
                nums[i+1] = nums[i]
            changed = True 
    return True

if __name__ == '__main__':
    n1 = [4, 2, 3]
    n2 = [4, 2, 1]
    n3 = [3, 4, 2, 3]
    print(checkPossibility(n1))
    print(checkPossibility(n2))
    print(checkPossibility(n3))
