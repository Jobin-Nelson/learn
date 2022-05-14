'''
Qn:Given an integer array nums, find the contiguous non-empty subarray within the array which has the largest product, and return the product
Link: https://leetcode.com/problems/maximum-product-subarray/
Notes:
- keeping track of minimum and maximum values throughout iteration 
'''

def maxProduct(nums):
    maxi = nums[0]
    cur_min, cur_max = 1, 1

    for n in nums:
        tmp = cur_max * n
        cur_max = max(cur_min*n, cur_max*n, n)
        cur_min = min(cur_min*n, tmp, n)
        maxi = max(maxi, cur_max)
    return maxi

if __name__ == '__main__':
    nums1 = [2, 3, -2, 4]
    nums2 = [-2, 0, -1]
    nums3 = [2, -5, -2, -4, 3]
    print(maxProduct(nums1))
    print(maxProduct(nums2))
    print(maxProduct(nums3))
