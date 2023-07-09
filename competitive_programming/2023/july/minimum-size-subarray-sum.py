'''
Created Date: 2023-07-06
Qn: Given an array of positive integers nums and a positive integer target,
    return the minimal length of a subarray whose sum is greater than or equal
    to target. If there is no such subarray, return 0 instead.
Link: https://leetcode.com/problems/minimum-size-subarray-sum/
Notes:
    - use sliding window
'''
def minSubArrayLen(target: int, nums: list[int]) -> int:
    N = len(nums)
    l = r = 0
    res, cur_sum = float('inf'), 0
    while r < N:
        cur_sum += nums[r]
        while cur_sum >= target:
            res = min(res, r - l + 1)
            cur_sum -= nums[l]
            l += 1
        r += 1
    return 0 if res == float('inf') else res

if __name__ == '__main__':
    t1, n1 = 7, [2, 3, 1, 2, 4, 3]
    t2, n2 = 4, [1, 4, 4]
    t3, n3 = 11, [1,1,1,1,1,1,1,1]

    print(minSubArrayLen(t1, n1))
    print(minSubArrayLen(t2, n2))
    print(minSubArrayLen(t3, n3))
