'''
Created Date: 2023-10-09
Qn: Given an array of integers nums sorted in non-decreasing order, find the
    starting and ending position of a given target value.

    If target is not found in the array, return [-1, -1].

    You must write an algorithm with O(log n) runtime complexity.
Link: https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
Notes:
    - use binary search
'''
def searchRange(nums: list[int], target: int) -> list[int]:
    if not nums or nums[0] > target or nums[len(nums)-1] < target: return [-1, -1]

    def binary_search(left_biased: bool) -> int:
        l, r = 0, len(nums)-1
        i = -1
        while l <= r:
            m = l + ((r-l) >> 1)
            if nums[m] < target:
                l = m + 1
            elif nums[m] > target:
                r = m - 1
            else:
                i = m
                if left_biased:
                    r = m - 1
                else:
                    l = m + 1
        return i
    return [binary_search(True), binary_search(False)]

if __name__ == '__main__':
    n1, t1 = [5,7,7,8,8,10], 8
    n2, t2 = [5,7,7,8,8,10], 6
    n3, t3 = [], 0

    print(searchRange(n1, t1))
    print(searchRange(n2, t2))
    print(searchRange(n3, t3))
