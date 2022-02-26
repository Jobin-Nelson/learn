'''
Qn: Given an integer nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i]
Link: https://leetcode.com/problems/product-of-array-except-self/
Notes:
- create prefix and postfix products of each elements in the array, then combine them by multiplying
'''
# pre and post 
def product_array(nums: list[int])->int:
    res = [1]*len(nums)
    prefix = 1
    for i in range(len(nums)):
        res[i] = prefix
        prefix *= nums[i]
    postfix = 1
    for i in range(len(nums)-1, -1, -1):
        res[i] *= postfix
        postfix *= nums[i]
    return res

if __name__ == '__main__':
    nums1 = [1, 2, 3, 4]
    nums2 = [-1, 1, 0 , -3, 3]
    print(product_array(nums1))
    print(product_array(nums2))
