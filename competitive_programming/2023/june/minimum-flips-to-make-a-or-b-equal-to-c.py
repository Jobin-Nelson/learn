'''
Created Date: 2023-06-07
Qn: Given 3 positives numbers a, b and c. Return the minimum flips required in
    some bits of a and b to make ( a OR b == c ). (bitwise OR operation). Flip
    operation consists of change any single bit 1 to 0 or change the bit 0 to 1
    in their binary representation.
Link: https://leetcode.com/problems/minimum-flips-to-make-a-or-b-equal-to-c/
Notes:
    - use XOR to find the bits that need to be flipped
    - use AND to find the extra bit flips
    - return the sum of XOR and AND
'''
def minFlips(a: int, b: int, c: int) -> int:
    return ((a|b) ^ c).bit_count() + (a & b & ((a|b) ^ c)).bit_count()

if __name__ == '__main__':
    a1, b1, c1 = 2, 6, 5
    a2, b2, c2 = 4, 2, 7
    a3, b3, c3 = 1, 2, 3

    print(minFlips(a1, b1, c1))
    print(minFlips(a2, b2, c2))
    print(minFlips(a3, b3, c3))
