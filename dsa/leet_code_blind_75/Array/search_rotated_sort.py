'''
Qn: Given an array nums after possible rotation and an integer target, return the index of target if it is in nums or -1 if it is not in nums
Link: https://leetcode.com/problems/search-in-rotated-sorted-array/
Notes:
- a version of binary search 
- finding the pivot and then binary searching a normal sorted array
'''
# Modified binary search
def search_rot(self, nums: list[int], target: int)-> int:
    l, r = 0, len(nums)-1

    while l<=r:
        m = (l+r)//2
        if nums[m]==target:
            return nums[m]

        # left sorted portion
        if nums[l]<=nums[m]:
            if target > nums[m] or target < nums[l]:
                l = m+1
            else:
                r = m-1
        # right sorted portion
        else:
            if target < nums[m] or target > nums[r]:
                r = m-1
            else:
                l = m+1
    return -1

def search(nums, target):
    # finding the pivor index
    l, r = 0, len(nums) - 1
    while l < r:
        m = (r + l) // 2
        if nums[m] > nums[r]:
            l = m + 1
        else:
            r = m 

    # narrowing down to a normal sorted array
    start = l
    l, r = 0, len(nums) - 1
    if target >= nums[start] and target <= nums[r]:
        l = start
    else:
        r = start

    # regular binary search
    while l <= r:
        m = (r + l) // 2
        if nums[m] == target:
            return m
        if nums[m] < target:
            l = m + 1
        else:
            r = m - 1
    return -1

if __name__ == '__main__':
    nums1 = [4, 5, 6, 7, 0, 1 ,2]
    target1 =  0
    nums2 = [4, 5, 6, 7, 0, 1 ,2]
    target2 = 3
    nums3 = [1]
    target3 = 0

    print(search(nums1, target1))
    print(search(nums2, target2))
    print(search(nums3, target3))