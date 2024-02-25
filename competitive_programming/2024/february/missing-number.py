"""
Created Date: 2024-02-20
Qn: Given an array nums containing n distinct numbers in the range [0, n],
    return the only number in the range that is missing from the array.
Link: https://leetcode.com/problems/missing-number/
Notes:
    - difference between target sum and actual sum
"""
def missingNumber(nums: list[int]) -> int:
    n = len(nums)
    target_sum = (n * (n+1)) // 2
    actual_sum = sum(nums)
    return target_sum - actual_sum

if __name__ == '__main__':
    n1 = [3,0,1]
    n2 = [0,1]
    n3 = [9,6,4,2,3,5,7,0,1]

    print(missingNumber(n1))
    print(missingNumber(n2))
    print(missingNumber(n3))
