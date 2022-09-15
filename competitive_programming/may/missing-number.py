'''
Qn: Given an array nums containing n distinct numbers in the range [0, n], 
    return the only number in the range that is missing from the array.
Link: https://leetcode.com/problems/missing-number/
Notes:
    - difference between the sums of range(n) & nums
'''
def missingNumber(nums: list[int]) -> int:
    res = len(nums)

    for i, n in enumerate(nums):
        res += i - n
    return res

if __name__ == '__main__':
    n1, n2, n3 = [3, 0, 1], [0, 1], [9,6,4,2,3,5,7,0,1]
    print(missingNumber(n1))
    print(missingNumber(n2))
    print(missingNumber(n3))
