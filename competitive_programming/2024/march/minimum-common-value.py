"""
Created Date: 2024-03-04
Qn: Given two integer arrays nums1 and nums2, sorted in non-decreasing order,
    return the minimum integer common to both arrays. If there is no common
    integer amongst nums1 and nums2, return -1.

    Note that an integer is said to be common to nums1 and nums2 if both arrays
    have at least one occurrence of that integer.
Link: https://leetcode.com/problems/bag-of-tokens/
Notes:
    - two pointers for each lists
"""
def getCommon(nums1: list[int], nums2: list[int]) -> int:
    i = j = 0
    while i < len(nums1) and j < len(nums2):
        if nums1[i] < nums2[j]:
            i += 1
        elif nums1[i] > nums2[j]:
            j += 1
        else:
            return nums1[i]
    return -1

if __name__ == '__main__':
    n11, n12 = [1,2,3], [2,4]
    n21, n22 = [1,2,3,6], [2,3,4,5]

    print(getCommon(n11, n12))
    print(getCommon(n12, n22))
