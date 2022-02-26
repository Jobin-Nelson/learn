'''
Qn: Given an integer array nums, return all triplets such that nums[i] + nums[j] + nums[k] == 0. Notice that the solution set must not contain any duplicates
Link: https://leetcode.com/problems/3sum/
Notes:
- sort and two pointer on rest of the elements just like in two_sums
'''

# sort and two pointer
def three_sum(nums):
    nums.sort()
    res = []
    for i in range(len(nums)):
        if i > 0 and nums[i] == nums[i-1]: # just skipping the same values
            continue
        l, r = i + 1, len(nums) - 1
        while l < r:
            three_sum = nums[i] + nums[l] + nums[r]
            if three_sum > 0:
                r -= 1
            elif three_sum < 0:
                l += 1
            else:
               res.append([nums[i], nums[l], nums[r]])
               l += 1
               while nums[l] == nums[l-1] and l < r: # just skipping the same values
                   l += 1

    return res

if __name__ == '__main__':
    nums1 = [-1, 0, 1, 2, -1, -4]
    nums2 = []
    nums3 = [0]
    print(three_sum(nums1))
    print(three_sum(nums2))
    print(three_sum(nums3))
