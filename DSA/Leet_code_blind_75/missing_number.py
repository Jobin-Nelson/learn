# summing the difference at each index to find the missing value
class Solution:
    def missing_number(self, nums: List[int])-> int:
        res = len(nums)
        for i in range(len(nums)):
            res += (i-nums[i])
        return res