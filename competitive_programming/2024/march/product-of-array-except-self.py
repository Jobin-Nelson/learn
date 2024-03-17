"""
Created Date: 2024-03-15
Qn: Given an integer array nums, return an array answer such that answer[i] is
    equal to the product of all the elements of nums except nums[i].

    The product of any prefix or suffix of nums is guaranteed to fit in a
    32-bit integer.

    You must write an algorithm that runs in O(n) time and without using the
    division operation
Link: https://leetcode.com/problems/product-of-array-except-self/
Notes:
    - use prefix and postfix products
"""
def productExceptSelf(nums: list[int]) -> list[int]:
    N = len(nums)
    postfix_product = prefix_product = 1
    res = [0] * N

    for i in range(N):
        res[i] = prefix_product
        if res[N-1-i] != 0:
            res[N-1-i] *= postfix_product
        else:
            res[N-1-i] = postfix_product
        prefix_product *= nums[i]
        postfix_product *= nums[N-1-i]
    return res
    # N = len(nums)
    # prefix_product = [1] * N
    # post_product = [1] * N
    #
    # for i in range(N-1):
    #     prefix_product[i+1] = prefix_product[i] * nums[i]
    #     post_product[N-i-2] = post_product[N-i-1] * nums[N-i-1]
    #
    # return [pre_pro * pos_pro for pre_pro, pos_pro in zip(prefix_product, post_product)]



if __name__ == '__main__':
    n1 = [1,2,3,4]
    n2 = [-1,1,0,-3,3]

    print(productExceptSelf(n1))
    print(productExceptSelf(n2))
