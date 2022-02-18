'''
Qn: Reverse bits of a given 32 bits unsigned integer.
Link: https://leetcode.com/problems/reverse-bits/
Notes:
- shifting bits by one to the left for the input and right for the output by adding the last digit to the output, 32 times
'''
def reverse_bits(n):
    n = int(n, 2)
    res = 0
    for i in range(32):
        res <<= 1
        res += n & 1
        n >>= 1
    return res



if __name__ == '__main__':
    n1 = '00000010100101000001111010011100'
    n2 = '11111111111111111111111111111101'
    print(reverse_bits(n1))
    print(reverse_bits(n2))
