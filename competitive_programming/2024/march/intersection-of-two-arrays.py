"""
Created Date: 2024-03-10
Qn: Given two integer arrays nums1 and nums2, return an array of their
    intersection. Each element in the result must be unique and you may return
    the result in any order.
Link: https://leetcode.com/problems/intersection-of-two-arrays/
Notes:
    - use hashset to find intersection
"""
def intersection(nums1: list[int], nums2: list[int]) -> list[int]:
    return list(set(nums1).intersection(set(nums2)))

if __name__ == '__main__':
    n11, n12 = [1,2,2,1], [2,2]
    n21, n22 = [4,9,5], [9,4,9,8,4]

    print(intersection(n11, n12))
    print(intersection(n21, n22))
