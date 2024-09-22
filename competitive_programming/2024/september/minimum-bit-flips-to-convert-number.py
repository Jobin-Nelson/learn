"""
Created Date: 2024-09-11
Qn: A bit flip of a number x is choosing a bit in the binary representation of
  x and flipping it from either 0 to 1 or 1 to 0.

  - For example, for x = 7, the binary representation is 111 and we may choose
    any bit (including any leading zeros not shown) and flip it. We can flip
    the first bit from the right to get 110, flip the second bit from the right
    to get 101, flip the fifth bit from the right (a leading zero) to get
    10111, etc. 

  Given two integers start and goal, return the minimum number of bit flips to
  convert start to goal.
Link: https://leetcode.com/problems/minimum-bit-flips-to-convert-number/
Notes:
    - get xor and use brian kernigan bit count algo
"""
def minBitFlips(start: int, goal: int) -> int:
    res =0
    xor = start ^ goal
    while xor:
        xor &= xor -1
        res += 1
    return res


if __name__ == '__main__':
    s1, g1 = 10, 7
    s2, g2 = 3, 4

    print(minBitFlips(s1, g1))
    print(minBitFlips(s2, g2))