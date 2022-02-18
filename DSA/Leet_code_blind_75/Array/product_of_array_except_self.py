'''
Qn: Given an integer nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i]
Link: https://leetcode.com/problems/product-of-array-except-self/
Notes:
- create prefix and postfix products of each elements in the array, then combine them by multiplying
'''

def product_except_self(nums):
    length = len(nums)
    pre, post = [1] * length, [1] * length

    for i in range(length):
        if i > 0:
            pre[i] = pre[i-1] * nums[i-1]
            post[length-1-i] = post[length-i] * nums[length-i]
    i = 0
    while i < length:
        pre[i] *= post[i]
        i += 1
    return pre

# pre and post 
def product_array(nums: list[int])->int:
    res = []*len(nums)
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
    print(product_except_self(nums1))
    print(product_except_self(nums2))
