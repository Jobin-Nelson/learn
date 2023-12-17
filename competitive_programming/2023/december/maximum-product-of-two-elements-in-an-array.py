"""
Created Date: 2023-12-12
Qn: Given the array of integers nums, you will choose two different indices i
    and j of that array. Return the maximum value of (nums[i]-1)*(nums[j]-1). 
Link: https://leetcode.com/problems/maximum-product-of-two-elements-in-an-array/
Notes:
    - use two variables to track largest and second largest
"""
def maxProduct(nums: list[int]) -> int:
    mf = ms = 0
    for n in nums:
        if n >= mf:
            mf, ms = n, mf
        elif n > ms:
            ms = n
    return (mf-1) * (ms-1)

if __name__ == '__main__':
    n1 = [3, 4, 5, 2]
    n2 = [1, 5, 4, 5]
    n3 = [10,2,5,2]

    print(maxProduct(n1))
    print(maxProduct(n2))
    print(maxProduct(n3))
