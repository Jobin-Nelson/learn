'''
Created Date: 2023-05-11
Qn: You are given two integer arrays nums1 and nums2. We write the integers of
    nums1 and nums2 (in the order they are given) on two separate horizontal
    lines.

    We may draw connecting lines: a straight line connecting two numbers
    nums1[i] and nums2[j] such that:

        - nums1[i] == nums2[j],
        - and the line we draw does not intersect any other connecting
          (non-horizontal) line.

    Note that a connecting line cannot intersect even at the endpoints (i.e.,
    each number can only belong to one connecting line).

    Return the maximum number of connecting lines we can draw in this way.
Link: https://leetcode.com/problems/uncrossed-lines/
Notes:
    - use LCS approach
    - use 2 arrays to keep track of the prev and the current dp values
'''
def maxUncrossedLines(nums1: list[int], nums2: list[int]) -> int:
    n, m = len(nums1), len(nums2)

    prev = [0] * (m+1)

    for i in range(1, n+1):
        dp = [0] * (m+1)
        for j in range(1, m+1):
            if nums1[i-1] == nums2[j-1]:
                dp[j] = 1 + prev[j-1]
            else:
                dp[j] = max(prev[j], dp[j-1])
        prev = dp
    return prev[m]

if __name__ == '__main__':
    n11, n12 = [1,4,2], [1,2,4]
    n21, n22 = [2,5,1,2,5], [10,5,2,1,5,2]
    n31, n32 = [1,3,7,1,7,5], [1,9,2,5,1]

    print(maxUncrossedLines(n11, n12))
    print(maxUncrossedLines(n21, n22))
    print(maxUncrossedLines(n31, n32))
