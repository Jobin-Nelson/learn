'''
Created Date: 2023-05-03
Qn: Given two 0-indexed integer arrays nums1 and nums2, return a list answer of
    size 2 where:

        - answer[0] is a list of all distinct integers in nums1 which are not
          present in nums2. 
        - answer[1] is a list of all distinct integers in nums2 which are not
          present in nums1.

    Note that the integers in the lists may be returned in any order.
Link: https://leetcode.com/problems/find-the-difference-of-two-arrays/
Notes:
    - use set
'''
def findDifference(nums1: list[int], nums2: list[int]) -> list[list[int]]:
    s1, s2 = set(nums1), set(nums2)

    return [list(s1 - s2), list(s2 - s1)]

if __name__ == '__main__':
    n11, n12 = [1,2,3], [2,4,6]
    n21, n22 = [1,2,3,3], [1,1,2,2]

    print(findDifference(n11, n12))
    print(findDifference(n21, n22))
