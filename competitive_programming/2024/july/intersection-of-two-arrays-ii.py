"""
Created Date: 2024-07-02
Qn: Given two integer arrays nums1 and nums2, return an array of their
    intersection. Each element in the result must appear as many times as it
    shows in both arrays and you may return the result in any order.
Link: https://leetcode.com/problems/intersection-of-two-arrays-ii/
Notes:
"""
def intersect(nums1: list[int], nums2: list[int]) -> list[int]:
    c1 = [0] * 1001
    res = []
    for n in nums1:
        c1[n] += 1
    for n in nums2:
        if c1[n] > 0:
            c1[n] -= 1
            res.append(n)
    return res

if __name__ == '__main__':
    n11, n12 = [1,2,2,1], [2,2]
    n21, n22 = [4,9,5], [9,4,9,8,4]

    print(intersect(n11, n12))
    print(intersect(n21, n22))
