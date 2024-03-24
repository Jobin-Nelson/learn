"""
Created Date: 2024-03-24
Qn: Given an array of integers nums containing n + 1 integers where each
    integer is in the range [1, n] inclusive.

    There is only one repeated number in nums, return this repeated number.

    You must solve the problem without modifying the array nums and uses only
    constant extra space.
Link: https://leetcode.com/problems/find-the-duplicate-number/
Notes:
    - use linked list
    - use Floyd's algorithm to find the cycle node
"""
def findDuplicate(nums: list[int]) -> int:
    slow, fast = 0, 0
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast: break

    slow2 = 0
    while True:
        slow = nums[slow]
        slow2 = nums[slow2]
        if slow == slow2: return slow2

if __name__ == '__main__':
    n1 = [1,3,4,2,2]
    n2 = [3,1,3,4,2]
    n3 = [3] * 5

    print(findDuplicate(n1))
    print(findDuplicate(n2))
    print(findDuplicate(n3))

