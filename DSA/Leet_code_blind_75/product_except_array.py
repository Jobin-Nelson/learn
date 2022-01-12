# pre and post 
class Solution:
    def product_array(self, nums: List[int])->int:
        res = []*len(nums)
        prefix = 1
        for i, num in enumerate(nums):
            res[i] = prefix
            prefix *= num
        postfix = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] = postfix
            postfix *= nums[i]
        return res