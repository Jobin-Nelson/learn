'''
Created Date: 2023-09-19
Qn: Given an array of integers nums containing n + 1 integers where each
    integer is in the range [1, n] inclusive.

    There is only one repeated number in nums, return this repeated number.

    You must solve the problem without modifying the array nums and uses only
    constant extra space.
Link: https://leetcode.com/problems/find-the-duplicate-number/
Notes:
    - no too numbers can point to the same index
    - use slow and fast pointers to detect a cycle
'''
def findDuplicates(nums: list[int]) -> int:
    slow = fast = 0

    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast: break

    slow2 = 0
    while True:
        slow = nums[slow]
        slow2 = nums[slow2]
        if slow == slow2: return slow

if __name__ == '__main__':
    n1 = [1,3,4,2,2]
    n2 = [3,1,3,4,2]

    print(findDuplicates(n1))
    print(findDuplicates(n2))
