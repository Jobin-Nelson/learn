'''
Qn: Given an array of integer nums and integer target, return indices of two numbers such that they add up to target
Link: https://leetcode.com/problems/two-sum/
Notes: Use hashmap to store the indices of each number and check if the remainder is in the hashmap
'''

def two_sum(nums: list[int], target: int) -> list[int]:
    hashmap = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in hashmap:
            return [i, hashmap[complement]]
        hashmap[num] = i

if __name__ == '__main__':
    nums1 = [2, 7, 11, 15]
    target1 = 9
    nums2 = [3, 2, 4]
    target2 = 6
    print(two_sum(nums1, target1))
    print(two_sum(nums2, target2))
