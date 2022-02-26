'''
Qn: Given sorted rotated array nums of unique, return the minimum element of this array
Link: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
Notes:
- variation of binary search
'''

def find_min(nums):
    l, r  = 0, len(nums) - 1

    while l < r:
        m = (r + l) // 2
        if m > 0 and (nums[m] < nums[m-1]):
            return nums[m]
        if nums[l] <= nums[m] and nums[m] > nums[r]:
            l = m + 1
        else: 
            r = m - 1

    return nums[l]

if __name__ == '__main__':
    nums1 = [3, 4, 5, 1, 2]
    nums2 = [4, 5, 6, 7, 0, 1, 2]
    nums3 = [11, 13, 15, 17]
    nums4 = [2, 1]
    print(find_min(nums1))
    print(find_min(nums2))
    print(find_min(nums3))
    print(find_min(nums4))
