'''
Created Date: 12-06-2022
Qn: You are given an array of positive integers nums and want to erase 
    a subarray containing unique elements. The score you get by erasing 
    the subarray is equal to the sum of its elements.
    Return the maximum score you can get by erasing exactly one subarray.
Link: https://leetcode.com/problems/maximum-erasure-value/
Notes:
- two pointer, sliding window solution & two variables to track max sum
'''
def maximumUniqueSubarray(nums: list[int]) -> int:
    res = cur_sum = l = r = 0
    visited = set()
    while r < len(nums):
        while nums[r] in visited:
            visited.remove(nums[l])
            cur_sum -= nums[l]
            l += 1
        visited.add(nums[r])
        cur_sum += nums[r]
        res = max(res, cur_sum)
        r += 1

    return res

if __name__ == '__main__':
    n1 = [4, 2, 4, 5, 6]
    n2 = [5,2,1,2,5,2,1,2,5]
    print(maximumUniqueSubarray(n1))
    print(maximumUniqueSubarray(n2))
