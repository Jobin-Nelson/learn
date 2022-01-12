# sliding window
class Solution:
    def sum_array(self, nums: List[int])-> int:
        max_sub = nums[0]
        cur_sum = 0
        for n in nums:
            if cur_sum<0:
                cur_sum = 0
            cur_sum += n
            max_sub = max(cur_sum, max_sub)
        return max_sub
