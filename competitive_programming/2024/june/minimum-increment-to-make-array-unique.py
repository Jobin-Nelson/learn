"""
Created Date: 2024-06-14
Qn: You are given an integer array nums. In one move, you can pick an index i
    where 0 <= i < nums.length and increment nums[i] by 1.

    Return the minimum number of moves to make every value in nums unique.

    The test cases are generated so that the answer fits in a 32-bit integer.
Link: https://leetcode.com/problems/minimum-increment-to-make-array-unique/
Notes:
"""
def minIncrementForUnique(nums: list[int]) -> int:
    res = 0
    nums.sort()
    for i in range(1, len(nums)):
        if nums[i] <= nums[i-1]:
            increment = nums[i-1] + 1 - nums[i]
            res += increment
            nums[i] = nums[i-1] + 1
    return res


if __name__ == '__main__':
    n1 = [1,2,2]
    n2 = [3,2,1,2,1,7]

    print(minIncrementForUnique(n1))
    print(minIncrementForUnique(n2))
