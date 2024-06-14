"""
Created Date: 2024-06-12
Qn: Given an array nums with n objects colored red, white, or blue, sort them
    in-place so that objects of the same color are adjacent, with the colors in
    the order red, white, and blue.

    We will use the integers 0, 1, and 2 to represent the color red, white, and
    blue, respectively.

    You must solve this problem without using the library's sort function.
Link: https://leetcode.com/problems/sort-colors/
Notes:
    - use quick sort partitioning from both left and right
"""
def sortColors(nums: list[int]) -> None:
    l, r = 0, len(nums)-1
    i = 0
    while i <= r:
        if nums[i] == 0:
            nums[l], nums[i] = nums[i], nums[l]
            l += 1
        elif nums[i] == 2:
            nums[r], nums[i] = nums[i], nums[r]
            r -= 1
            i -= 1
        i += 1

    # Two pass counter
    # counter = [0] * 3
    # for n in nums:
    #     counter[n] += 1
    # j = 0
    # for i in range(3):
    #     for _ in range(counter[i]):
    #         nums[j] = i
    #         j += 1

    # Merge sort
    # def merge_sort(nums: list[int]):
    #     if len(nums) == 1: return
    #     m = len(nums) >> 1
    #     l, r = nums[:m], nums[m:]
    #
    #     merge_sort(l)
    #     merge_sort(r)
    #
    #     k = i = j = 0
    #     while i < len(l) and j < len(r):
    #         if l[i] <= r[j]:
    #             nums[k] = l[i]
    #             i += 1
    #         else:
    #             nums[k] = r[j]
    #             j += 1
    #         k += 1
    #     while i < len(l):
    #         nums[k] = l[i]
    #         k += 1
    #         i += 1
    #     while j < len(r):
    #         nums[k] = r[j]
    #         k += 1
    #         j += 1
    # merge_sort(nums)

if __name__ == '__main__':
    n1 = [2,0,2,1,1,0]
    n2 = [2,0,1]

    sortColors(n1)
    sortColors(n2)

    print(n1)
    print(n2)
