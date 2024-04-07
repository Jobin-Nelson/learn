"""
Created Date: 2024-03-26
Qn: Given an unsorted integer array nums. Return the smallest positive integer
    that is not present in nums.

    You must implement an algorithm that runs in O(n) time and uses O(1)
    auxiliary space.
Link: https://leetcode.com/problems/first-missing-positive/
Notes:
    - use cycle sort
"""
def firstMissingPositive(nums: list[int]) -> int:
    N = len(nums)
    i = 0
    while i < N:
        id = nums[i] - 1
        if 0 < nums[i] <= N and nums[i] != nums[id]:
            nums[i], nums[id] = nums[id], nums[i]
        else:
            i += 1

    for i, n in enumerate(nums):
        if n != i + 1:
            return i + 1
    return N + 1

if __name__ == '__main__':
    n1 = [1,2,0]
    n2 = [3,4,-1,1]
    n3 = [7,8,9,11,12]
    n4 = [2,1]
    n5 = [-1,4,2,1,9,10]

    print(firstMissingPositive(n1))
    print(firstMissingPositive(n2))
    print(firstMissingPositive(n3))
    print(firstMissingPositive(n4))
    print(firstMissingPositive(n5))
