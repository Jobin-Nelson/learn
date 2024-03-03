"""
Created Date: 2024-03-01
Qn: You are given a binary string s that contains at least one '1'.

    You have to rearrange the bits in such a way that the resulting binary
    number is the maximum odd binary number that can be created from this
    combination.

    Return a string representing the maximum odd binary number that can be
    created from the given combination.

    Note that the resulting string can have leading zeros.
Link: https://leetcode.com/problems/maximum-odd-binary-number/
Notes:
    - use string maniuplation
"""
def maximumOddBinaryNumber(s: str) -> str:
    ones = s.count('1')
    return ('1' * (ones-1)) + ('0' * (len(s) - ones)) + '1'
    # bit_count = 0
    # n = int(s, 2)
    # while n:
    #     n &= (n-1)
    #     bit_count += 1
    # if bit_count == 0: return '0'
    # res = [0] * len(s)
    # for i in range(bit_count-1):
    #     res[i] = 1
    # res[-1] = 1
    # return ''.join(map(str, res))

if __name__ == '__main__':
    s1 = "010"
    s2 = "0101"

    print(maximumOddBinaryNumber(s1))
    print(maximumOddBinaryNumber(s2))
