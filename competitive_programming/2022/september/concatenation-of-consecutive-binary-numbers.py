'''
Created Date: 2022-09-23
Qn: Given an integer n, return the decimal value of the binary string formed by
    concatenating the binary representations of 1 to n in order, modulo 109 + 7.
Link: https://leetcode.com/problems/concatenation-of-consecutive-binary-numbers/
Notes:
    - concat binary from 1 -> n
    - convert to decimal from concated binary
'''
def concatenatedBinary(n: int) -> int:
    concat_string = ''

    for i in range(1, n+1):
        concat_string += format(i, 'b')
    return int(concat_string, 2) % (10**9 + 7)

if __name__ == '__main__':
    n1, n2, n3 = 1, 3, 12

    print(concatenatedBinary(n1))
    print(concatenatedBinary(n2))
    print(concatenatedBinary(n3))

