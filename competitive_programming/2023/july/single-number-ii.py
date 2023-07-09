'''
Created Date: 2023-07-04
Qn: Given an integer array nums where every element appears three times except
    for one, which appears exactly once. Find the single element and return it.

    You must implement a solution with a linear runtime complexity and use only
    constant extra space.
Link: https://leetcode.com/problems/single-number-ii/
Notes:
    - Take 2's complement bit manipulation
    - Keep track of ones and twos
'''
def singleNumber(nums: list[int]) -> int:
    ones = 0
    twos = 0

    for n in nums:
        ones ^= (n & ~twos) # ones = (ones ^ i) & ~twos
        twos ^= (n & ~ones)
    return ones

if __name__ == '__main__':
    n1 = [2,2,3,2]
    n2 = [0,1,0,1,0,1,99]

    print(singleNumber(n1))
    print(singleNumber(n2))


