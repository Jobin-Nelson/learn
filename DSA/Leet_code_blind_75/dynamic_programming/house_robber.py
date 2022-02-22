'''
Qn: You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed,
the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.
Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.
Link: https://leetcode.com/problems/house-robber/
Notes:
- we have to track only two variables r1, r2 and the decision on robbing the next house depends of the max if r1+n, r2
'''
def rob(nums):
    r1, r2 = 0, 0
    for n in nums:
        tmp = max(r1 + n, r2)
        r1 = r2
        r2 = tmp
    return r2

if __name__ == '__main__':
    nums1 = [1, 2, 3, 1]
    nums2 = [2, 7, 9, 3, 1]
    print(rob(nums1))
    print(rob(nums2))