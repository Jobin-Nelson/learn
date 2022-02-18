'''
Qn:ou are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed.
All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have a security system connected,
and it will automatically contact the police if two adjacent houses were broken into on the same night.
Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.
Link: https://leetcode.com/problems/house-robber-ii/
Notes: 
- house robber 1 as helper function and call it on nums excluding first and last houses and take the max among them and the first element in case if there is only one element in the array

'''
def rob(nums):
    return max(helper(nums[:-1]), helper(nums[1:]))

def helper(nums):
    r1, r2 = 0, 0
    for n in nums:
        tmp = max(r1 + n, r2)
        r1 = r2
        r2 = tmp
    return r2

if __name__ == '__main__':
    n1, n2, n3 = [2, 3, 2], [1, 2, 3, 1], [1, 2, 3]
    print(rob(n1))
    print(rob(n2))
    print(rob(n3))
