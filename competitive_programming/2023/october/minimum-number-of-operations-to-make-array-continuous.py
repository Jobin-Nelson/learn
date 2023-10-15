'''
Created Date: 2023-10-10
Qn: You are given an integer array nums. In one operation, you can replace any
    element in nums with any integer.

    nums is considered continuous if both of the following conditions are
    fulfilled:

        All elements in nums are unique. The difference between the maximum
        element and the minimum element in nums equals nums.length - 1.

    For example, nums = [4, 2, 5, 3] is continuous, but nums = [1, 2, 3, 5, 6]
    is not continuous.

    Return the minimum number of operations to make nums continuous.
Link: https://leetcode.com/problems/minimum-number-of-operations-to-make-array-continuous/
Notes:
    - use sliding window
'''
def minOperations(nums: list[int]) -> int:
    N = len(nums)
    nums = sorted(set(nums))
    nums.sort()
    res = N

    r = 0
    for l in range(len(nums)):
        while r < len(nums) and nums[r] < nums[l] + N:
            r += 1
        window = r - l
        res = min(res, N - window)
    return res

if __name__ == '__main__':
    n1 = [4,2,5,3]
    n2 = [1,2,3,5,6]
    n3 = [1,10,100,1000]

    print(minOperations(n1))
    print(minOperations(n2))
    print(minOperations(n3))
