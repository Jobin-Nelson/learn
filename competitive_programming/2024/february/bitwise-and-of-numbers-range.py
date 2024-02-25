"""
Created Date: 2024-02-21
Qn: Given two integers left and right that represent the range [left, right],
    return the bitwise AND of all numbers in this range, inclusive.
Link: https://leetcode.com/problems/bitwise-and-of-numbers-range/
Notes:
    - chop off rightmost bit and compare left and right
    - do this till most significant bits are equal
"""
def rangeBitwiseAnd(left: int, right: int) -> int:
    i = 0
    while left != right:
        left >>= 1
        right >>= 1
        i += 1
    return left << i

if __name__ == '__main__':
    l1, r1 = 5, 7
    l2, r2 = 0, 0
    l3, r3 = 1, 2147483647

    print(rangeBitwiseAnd(l1, r1))
    print(rangeBitwiseAnd(l2, r2))
    print(rangeBitwiseAnd(l3, r3))
