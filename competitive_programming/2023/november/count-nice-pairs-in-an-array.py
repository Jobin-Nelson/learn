'''
Created Date: 2023-11-21
Qn: You are given an array nums that consists of non-negative integers. Let us
    define rev(x) as the reverse of the non-negative integer x. For example,
    rev(123) = 321, and rev(120) = 21. A pair of indices (i, j) is nice if it
    satisfies all of the following conditions:

        0 <= i < j < nums.length nums[i] + rev(nums[j]) == nums[j] +
          rev(nums[i])

    Return the number of nice pairs of indices. Since that number can be too
    large, return it modulo 109 + 7.
Link: https://leetcode.com/problems/count-nice-pairs-in-an-array/
Notes:
    - use hashmap and sum of n natural numbers to calculate the number of nice
      values
'''
from collections import Counter

def countNicePairs(nums: list[int]) -> int:
    arr = [n - int(str(n)[::-1]) for n in nums]
    res = 0
    for f in Counter(arr).values():
        res += f * (f-1) // 2
    return res % (10*9 + 7)

    # def rev(num: int) -> int:
    #     res = 0
    #     while num:
    #         res = res * 10 + num % 10
    #         num //= 10
    #     return res
    # MOD = 10**9+7
    # res = 0
    # arr = [n - rev(n) for n in nums] 
    # count = {}
    # for a in arr:
    #     res = (res + count.get(a, 0)) % MOD
    #     count[a] = count.get(a, 0) + 1
    # return res

    # res = 0
    # N = len(nums)
    # rev = lambda x: int(str(x)[::-1])
    # MOD = 10**9 + 7
    #
    # for i in range(N):
    #     for j in range(i+1, N):
    #         res += (nums[i] + rev(nums[j]) == nums[j] + rev(nums[i]))
    # return res % MOD

if __name__ == '__main__':
    n1 = [42, 11, 1, 97]
    n2 = [13, 10, 35, 24, 76]

    print(countNicePairs(n1))
    print(countNicePairs(n2))
