"""
Created Date: 2024-08-22
Qn: The complement of an integer is the integer you get when you flip all the
    0's to 1's and all the 1's to 0's in its binary representation.

    - For example, The integer 5 is "101" in binary and its complement is "010"
      which is the integer 2. 

    Given an integer num, return its complement.
Link: https://leetcode.com/problems/number-complement/
Notes:
    - use bit shifting
"""


def findComplement(num: int) -> int:
    i = 0
    res = 0
    while num > 0:
        res |= ((num & 1) ^ 1) << i
        num >>= 1
        i += 1
    return res


if __name__ == '__main__':
    n1 = 5
    n2 = 1

    print(findComplement(n1))
    print(findComplement(n2))
