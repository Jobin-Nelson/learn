"""
Created Date: 2024-10-10
Qn: A ramp in an integer array nums is a pair (i, j) for which i < j and
    nums[i] <= nums[j]. The width of such a ramp is j - i.

    Given an integer array nums, return the maximum width of a ramp in nums. If
    there is no ramp in nums, return 0.
Link: https://leetcode.com/problems/maximum-width-ramp/
Notes:
    - use two pointer with monotonic increasing stack from right
"""


def maxWidthRamp(nums: list[int]) -> int:
    N = len(nums)
    max_right = [0] * N
    cur_max = 0
    for i in range(N - 1, -1, -1):
        cur_max = max(cur_max, nums[i])
        max_right[i] = cur_max
    res = 0
    l = 0
    for r in range(N):
        while nums[l] > max_right[r]:
            l += 1
        res = max(res, r - l)
    return res


if __name__ == '__main__':
    n1 = [6, 0, 8, 2, 1, 5]
    n2 = [9, 8, 1, 0, 1, 9, 4, 0, 4, 1]

    print(maxWidthRamp(n1))
    print(maxWidthRamp(n2))
