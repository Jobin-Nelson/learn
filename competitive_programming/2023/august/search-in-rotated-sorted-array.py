'''
Created Date: 2023-08-08
Qn: There is an integer array nums sorted in ascending order (with distinct
    values).

    Prior to being passed to your function, nums is possibly rotated at an
    unknown pivot index k (1 <= k < nums.length) such that the resulting array
    is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]
    (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3
    and become [4,5,6,7,0,1,2].

    Given the array nums after the possible rotation and an integer target,
    return the index of target if it is in nums, or -1 if it is not in nums.

    You must write an algorithm with O(log n) runtime complexity.
Link: https://leetcode.com/problems/search-in-rotated-sorted-array/
Notes:
'''
def search(nums: list[int], target: int) -> int:
    # find pivot
    l, r = 0, len(nums)-1
    while l <= r:
        m = (l + r) >> 1
        if nums[m] > nums[-1]:
            l = m + 1
        else:
            r = m - 1

    # set boundary
    start = l
    # print(f'{start=}, {nums=}')
    if nums[start] <= target <= nums[-1]:
        l, r = start, len(nums)-1
    else:
        l, r = 0, start-1

    # find target
    while l <= r:
        m = (l + r) >> 1
        if nums[m] > target:
            r = m - 1
        elif nums[m] < target:
            l = m + 1
        else:
            return m

    return -1

if __name__ == '__main__':
    n1, t1 = [4,5,6,7,0,1,2], 0
    n2, t2 = [4,5,6,7,0,1,2], 3
    n3, t3 = [1], 0
    n4, t4 = [5,1,3], 1

    print(search(n1, t1))
    print(search(n2, t2))
    print(search(n3, t3))
    print(search(n4, t4))
