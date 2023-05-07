'''
Created Date: 2023-05-02
Qn: There is a function signFunc(x) that returns:

        - 1 if x is positive.
        - -1 if x is negative.
        - 0 if x is equal to 0.

    You are given an integer array nums. Let product be the product of all
    values in the array nums.

    Return signFunc(product).
Link: https://leetcode.com/problems/sign-of-the-product-of-an-array/
Notes:
'''
def arraySign(nums: list[int]) -> int:
    is_negative = 0
    for n in nums:
        if n == 0: return 0
        if n < 0: is_negative ^= 1
    return -1 if is_negative else 1

if __name__ == '__main__':
    n1 = [-1,-2,-3,-4,3,2,1]
    n2 = [1,5,0,2,-3]
    n3 = [-1,1,-1,1,-1]

    print(arraySign(n1))
    print(arraySign(n2))
    print(arraySign(n3))
