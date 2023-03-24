'''
Created Date: 2023-03-21
Qn: Given an integer array nums, return the number of subarrays filled with 0.
    A subarray is a contiguous non-empty sequence of elements within an array.
Link: https://leetcode.com/problems/number-of-zero-filled-subarrays/
Notes:
    - use two variables to store current and total
    - reset the current whenever you encounter non zero value
'''
def zeroFilledSubArray(nums: list[int]) -> int:
    res = current_zero_subarrays = 0

    for n in nums:
        if n == 0:
            current_zero_subarrays += 1
            res += current_zero_subarrays
        else:
            current_zero_subarrays = 0
    return res

if __name__ == '__main__':
    n1 = [1,3,0,0,2,0,0,4]
    n2 = [0,0,0,2,0,0]
    n3 = [2,10,2019]

    print(zeroFilledSubArray(n1))
    print(zeroFilledSubArray(n2))
    print(zeroFilledSubArray(n3))
