"""
Created Date: 2024-04-29
Qn: You are given a 0-indexed integer array nums and a positive integer k.

    You can apply the following operation on the array any number of times:

        - Choose any element of the array and flip a bit in its binary
          representation. Flipping a bit means changing a 0 to 1 or vice versa.

    Return the minimum number of operations required to make the bitwise XOR of
    all elements of the final array equal to k.

    Note that you can flip leading zero bits in the binary representation of
    elements. For example, for the number (101)2 you can flip the fourth bit
    and obtain (1101)2.
Link: https://leetcode.com/problems/minimum-number-of-operations-to-make-array-xor-equal-to-k/
Notes:
    - calculate the final_xor and get the xor of final_xor and k
    - return bit count of the result
"""
def minOperation(nums: list[int], k: int) -> int:
    final_xor = 0
    for n in nums:
        final_xor ^= n
    res = final_xor ^ k
    return res.bit_count()

if __name__ == '__main__':
    n1, k1 = [2,1,3,4], 1
    n2, k2 = [2,0,2,0], 0

    print(minOperation(n1, k1))
    print(minOperation(n2, k2))
