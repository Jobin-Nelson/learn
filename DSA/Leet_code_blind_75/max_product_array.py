# Keeping track of both min and max
class Solution:
    def max_product(self, nums:List[int])->int:
        res = max(nums)
        cur_min, cur_max = 1, 1

        for n in nums:
            if n==0:
                cur_min, cur_max = 1, 1
            tmp = cur_max*n
            cur_max = max(n*cur_max, n*cur_min, n)
            cur_min = max(tmp, n*cur_min, n)
            res = max(res, cur_max)
        return res