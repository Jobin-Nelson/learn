# hashmap
class Solution:
    def two_sum(self, nums: List[int], target: int) -> list[int]:
        hashmap = {} # value : index
        for i, num in enumerate(nums):
            complement = target - num
            if complement in hashmap:
                return [i, hashmap[complement]]
            hashmap[num] = (i)