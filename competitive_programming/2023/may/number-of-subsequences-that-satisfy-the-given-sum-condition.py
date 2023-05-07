'''
Created Date: 2023-05-06
Qn: You are given an array of integers nums and an integer target.

    Return the number of non-empty subsequences of nums such that the sum of
    the minimum and maximum element on it is less or equal to target. Since the
    answer may be too large, return it modulo 10^9 + 7.
Link: https://leetcode.com/problems/number-of-subsequences-that-satisfy-the-given-sum-condition/
Notes:
    - at any position you have 2 choice to include or not include
    - thus for every minimum number + m numbers you've 2^m subsequences
    - sort and do variant of binary search
'''
def numSubseq(nums: list[int], target: int) -> int:
        nums.sort()
        l, r = 0, len(nums) - 1
        res = 0
        mod = 10 ** 9 + 7
        
        while l <= r:
            if nums[l] + nums[r] > target:
                r -= 1
            else:
                res += pow(2, r - l, mod)
                l += 1
        
        return res % mod

if __name__ == '__main__':
    n1, t1 = [3,5,6,7], 9
    n2, t2 = [3,3,6,8], 10
    n3, t3 = [2,3,3,4,6,7], 12

    print(numSubseq(n1, t1))
    print(numSubseq(n2, t2))
    print(numSubseq(n3, t3))
