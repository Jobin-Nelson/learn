"""
Created Date: 2024-05-31
Qn: Given an integer array nums, in which exactly two elements appear only once
    and all the other elements appear exactly twice. Find the two elements that
    appear only once. You can return the answer in any order.

    You must write an algorithm that runs in linear runtime complexity and uses
    only constant extra space.
Link: https://leetcode.com/problems/single-number-iii/
Notes:
    - use xor
"""
def singleNumber(nums: list[int]) -> list[int]:
    total_xor = 0
    for n in nums:
        total_xor ^= n

    diff_bit = 1
    while not (total_xor & diff_bit):
        diff_bit <<= 1

    a = 0
    b = 0
    for n in nums:
        if diff_bit & n:
            a ^= n
        else:
            b ^= n
    return [a, b]

if __name__ == '__main__':
    n1 = [1,2,1,3,2,5]
    n2 = [-1,0]
    n3 = [0,1]

    print(singleNumber(n1))
    print(singleNumber(n2))
    print(singleNumber(n3))
