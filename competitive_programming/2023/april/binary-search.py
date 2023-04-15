'''
Created Date: 2023-04-01
Qn: Given an array of integers nums which is sorted in ascending order, and an
    integer target, write a function to search target in nums. If target
    exists, then return its index. Otherwise, return -1.

    You must write an algorithm with O(log n) runtime complexity.
Link: https://leetcode.com/problems/binary-search/
Notes:
    - use binary search
'''
def search(nums: list[int], target: int) -> int:
    l, r = 0, len(nums) - 1

    while l <= r:
        m = l + ((r - l) >> 1)
        if nums[m] > target:
            r = m - 1
        elif nums[m] < target:
            l = m + 1
        else:
            return m
    return -1

if __name__ == '__main__':
    n1, t1 = [-1,0,3,5,9,12], 9
    n2, t2 = [-1,0,3,5,9,12], 2

    print(search(n1, t1))
    print(search(n2, t2))
