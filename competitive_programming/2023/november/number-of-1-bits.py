"""
Created Date: 2023-11-29
Qn: Write a function that takes the binary representation of an unsigned
    integer and returns the number of '1' bits it has (also known as the
    Hamming weight).

    Note:

        - Note that in some languages, such as Java, there is no unsigned
          integer type. In this case, the input will be given as a signed
          integer type. It should not affect your implementation, as the
          integer's internal binary representation is the same, whether it is
          signed or unsigned. 
        - In Java, the compiler represents the signed integers using 2's
          complement notation. Therefore, in Example 3, the input represents
          the signed integer. -3.

Link: https://leetcode.com/problems/number-of-1-bits/
Notes:
    - use brian kernighans algorithm
    - n = n & (n-1) to only iterate over one bits
"""
def hammingWeight(n: int) -> int:
    res = 0
    while n:
        n &= (n-1)
        res += 1
    return res

if __name__ == '__main__':
    n1 = 0b00000000000000000000000000001011
    n2 = 0b00000000000000000000000010000000
    n3 = 0b11111111111111111111111111111101

    print(hammingWeight(n1))
    print(hammingWeight(n2))
    print(hammingWeight(n3))
