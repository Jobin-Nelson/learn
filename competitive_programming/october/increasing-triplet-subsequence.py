'''
Created Date: 2022-10-11
Qn: Given an integer array nums, return true if there exists a triple of
    indices (i, j, k) such that i < j < k and nums[i] < nums[j] < nums[k]. If
    no such indices exists, return false.
Link: https://leetcode.com/problems/increasing-triplet-subsequence/
Notes:
    - maintain two variables initialized to infinity
    - return True if second < third
    - if third is less or equal first assign first = third
    - else assign second = third
'''
def increasingTriplet(nums: list[int]) -> bool:
    first, second = float('inf'), float('inf')

    for third in nums:
        if second < third: return True
        if third <= first:
            first = third
        else:
            second = third
    return False

if __name__ == '__main__':
    n1 = [1, 2, 3, 4, 5]
    n2 = [5, 4, 3, 2, 1]
    n3 = [2, 1, 5, 0, 4, 6]

    print(increasingTriplet(n1))
    print(increasingTriplet(n2))
    print(increasingTriplet(n3))
