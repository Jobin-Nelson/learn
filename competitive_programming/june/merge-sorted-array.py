'''
Created Date: 07-06-2022
Qn: You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, 
    and two integers m and n, representing the number of elements in nums1 and nums2 
    respectively. Merge nums1 and nums2 into a single array sorted in non-decreasing order.
    The final sorted array should not be returned by the function, but instead be 
    stored inside the array nums1. To accommodate this, nums1 has a length of m + n, 
    where the first m elements denote the elements that should be merged, and the 
    last n elements are set to 0 and should be ignored. nums2 has a length of n.
Link: https://leetcode.com/problems/merge-sorted-array/
Notes:
- iterate from last to first and merge the larger value
- merge the leftover nums2 as well 
'''
def merge(nums1: list[int], m: int, nums2: list[int], n: int) -> None:
    last = m + n - 1
    while m > 0 and n > 0:
        if nums1[m-1] > nums2[n-1]:
            nums1[last] = nums1[m-1]
            m -= 1
        else:
            nums1[last] = nums2[n-1]
            n -= 1
        last -= 1

    while n > 0:
        nums1[last] = nums2[n-1]
        n -= 1
        last -= 1

if __name__ == '__main__':
    nums11, nums12 = [1,2,3,0,0,0], [2,5,6]
    m1, n1 = 3, 3
    nums21, nums22 = [1], []
    m2, n2 = 1, 0
    nums31, nums32 = [0], [1]
    m3, n3 = 0, 1
    merge(nums11, m1, nums12, n1)
    print(nums11)
    merge(nums21, m2, nums22, n2)
    print(nums21)
    merge(nums31, m3, nums32, n3)
    print(nums31)
