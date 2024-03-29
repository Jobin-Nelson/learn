"""
Created Date: 2023-11-30
Qn: Given an integer n, you must transform it into 0 using the following
    operations any number of times:

        - Change the rightmost (0th) bit in the binary representation of n.
        - Change the ith bit in the binary representation of n if the (i-1)th
          bit is set to 1 and the (i-2)th through 0th bits are set to 0.

    Return the minimum number of operations to transform n into 0.
Link: https://leetcode.com/problems/minimum-one-bit-operations-to-make-integers-zero/
Notes:
"""
def minimumOneBitOperations(n: int) -> int:
    if n == 0:
        return 0
    k = 0
    while 2 ** k <= n:
        k += 1
    k -= 1
    return 2 ** (k+1) - 1 - minimumOneBitOperations(2**k ^ n)

if __name__ == '__main__':
    n1 = 3
    n2 = 6

    print(minimumOneBitOperations(n1))
    print(minimumOneBitOperations(n2))
