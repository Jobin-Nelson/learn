'''
Created Date: 2022-09-20
Qn: Given two integer arrays nums1 and nums2, return the maximum length of a
    subarray that appears in both arrays.
Link: https://leetcode.com/problems/maximum-length-of-repeated-subarray/
Notes:
    - use dynamic programming with 2d array
    - if both i & j matches incremenet the previous element i-1, j-1
'''
def findLength(nums1: list[int], nums2: list[int]) -> int:
    N, M = len(nums1), len(nums2)
    dp = [[0 for _ in range(M+1)] for _ in range(N+1)]
    output = 0

    for i in range(1, N+1):
        for j in range(1, M+1):
            if nums1[i-1] == nums2[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
            output = max(output, dp[i][j])
    return output

if __name__ == '__main__':
    n11, n12 = [1, 2, 3, 2, 1], [3, 2, 1, 4, 7]
    n21, n22 = [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]

    print(findLength(n11, n12))
    print(findLength(n21, n22))
