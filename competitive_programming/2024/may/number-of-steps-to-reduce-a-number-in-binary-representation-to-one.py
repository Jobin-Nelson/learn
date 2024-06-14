"""
Created Date: 2024-05-29
Qn: Given the binary representation of an integer as a string s, return the
    number of steps to reduce it to 1 under the following rules:

        - If the current number is even, you have to divide it by 2.
        - If the current number is odd, you have to add 1 to it.

    It is guaranteed that you can always reach one for all test cases.
Link: https://leetcode.com/problems/number-of-steps-to-reduce-a-number-in-binary-representation-to-one/
Notes:
"""
def numSteps(s: str) -> int:
    n = int(s, 2)
    res = 0
    while n != 1:
        if n & 1:
            n += 1
            res += 1
        n >>= 1
        res += 1
    return res

if __name__ == '__main__':
    s1 = "1101"
    s2 = "10"
    s3 = "1"

    print(numSteps(s1))
    print(numSteps(s2))
    print(numSteps(s3))
