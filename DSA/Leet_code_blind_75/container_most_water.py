# Two pointer
class Solution:
    def max_area(self, nums: List[int])-> int:
        l, r = 0, len(nums)-1
        area = 0 
        while l<r:
            cur_area = (r-l)*min(nums[l], nums[r])
            area = max(area, cur_area)
            if nums[l]<=nums[r]:
                l += 1
            else: 
                r -= 1
        return  area