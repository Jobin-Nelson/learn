'''
Qn: Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.
Link: https://leetcode.com/problems/missing-number/
Notes:
- difference between the sum and guass equation (original sum) gives the missing number
'''

def missing_number(num):
    n = len(num)
    s = sum(num)
    ogs = n * (n+1) // 2
    return ogs - s

if __name__ == '__main__':
    nums1 = [3, 0, 1]
    nums2 = [0, 1]
    nums3 = [9, 6, 4, 2, 3, 5, 7, 0, 1]
    print(missing_number(nums1))
    print(missing_number(nums2))
    print(missing_number(nums3))