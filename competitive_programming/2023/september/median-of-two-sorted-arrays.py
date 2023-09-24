'''
Created Date: 2023-09-21
Qn: Given two sorted arrays nums1 and nums2 of size m and n respectively,
    return the median of the two sorted arrays.

    The overall run time complexity should be O(log (m+n)).
Link: https://leetcode.com/problems/median-of-two-sorted-arrays/
Notes:
    - use binary search
'''
def findMedianSortedArray(nums1: list[int], nums2: list[int]) -> float:
    A, B = nums1, nums2
    total = len(A) + len(B)
    half = total >> 1
    if len(B) < len(A): A, B = B, A
    N1, N2 = len(A), len(B)

    l, r = 0, N1 -1
    while True:
        i = (l + r) >> 1
        j = half - i - 2

        Aleft = A[i] if i >= 0 else float('-inf')
        Aright = A[i+1] if i+1 < N1 else float('inf')
        Bleft = B[j] if j >= 0 else float('-inf')
        Bright = B[j+1] if j+1 < N2 else float('inf')

        if Aleft <= Bright and Bleft <= Aright:
            if total & 1: return min(Aright, Bright)
            return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
        elif Aleft > Bright:
            r = i - 1
        else:
            l = i + 1

if __name__ == '__main__':
    n11, n12 = [1, 3], [2]
    n21, n22 = [1, 2], [3, 4]

    print(findMedianSortedArray(n11, n12))
    print(findMedianSortedArray(n21, n22))
