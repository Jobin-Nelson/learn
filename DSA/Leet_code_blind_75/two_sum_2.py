# Two pointer
class Solution:
    def two_sum_2(self, nums: List[int], target: int)-> List[int]:
        l, r = 0, len(nums)-1

        while l<r:
            cur_sum = nums[l]+nums[r]

            if cur_sum > target:
                r -= 1
            elif cur_sum < target:
                l += 1
            else:
                return [l+1, r+1]
        return []