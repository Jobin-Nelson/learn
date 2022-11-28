'''
Created Date: 2022-10-26
Qn: Given an integer array nums and an integer k, return true if nums has a
    continuous subarray of size at least two whose elements sum up to a
    multiple of k, or false otherwise.

    An integer x is a multiple of k if there exists an integer n such that x =
    n * k. 0 is always a multiple of k.
Link: https://leetcode.com/problems/continuous-subarray-sum/
Notes:
    - return True if we can find two same remainder and new value - prev value
      is > 1
'''
def checkSubarraySum(nums: list[int], k: int) -> bool:
    remainder = {0: -1}
    total = 0

    for i, n in enumerate(nums):
        total += n
        r = total % k
        if r not in remainder:
            remainder[r] = i
        elif i - remainder[r] > 1:
            return True
    return False


if __name__ == '__main__':
    n1, k1 = [23,2,4,6,7], 6
    n2, k2 = [23,2,6,4,7], 6
    n3, k3 = [23, 2, 6, 4, 7], 13

    print(checkSubarraySum(n1, k1))
    print(checkSubarraySum(n2, k2))
    print(checkSubarraySum(n3, k3))
