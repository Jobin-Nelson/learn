"""
Created Date: 2023-12-04
Qn: You are given a string num representing a large integer. An integer is good
    if it meets the following conditions:

        - It is a substring of num with length 3. 
        - It consists of only one unique digit.

    Return the maximum good integer as a string or an empty string "" if no such
    integer exists.

    Note:

        - A substring is a contiguous sequence of characters within a string. 
        - There may be leading zeroes in num or a good integer.

Link: https://leetcode.com/problems/largest-3-same-digit-number-in-string/
Notes:
    - use simple iteration and keep track of prev digits
"""
def largestGoodInteger(num: str) -> str:
    if len(num) <= 1: return ''
    prev = num[0]

    count, res = 1, ''
    for d in num[1:]:
        if d == prev:
            count += 1
        else:
            prev = d
            count = 1
        if count == 3 and (res == '' or res < d):
            res = d
    return res * 3

if __name__ == '__main__':
    n1 = "6777133339"
    n2 = "2300019"
    n3 = "42352338"
    n4 = "222"

    print(largestGoodInteger(n1))
    print(largestGoodInteger(n2))
    print(largestGoodInteger(n3))
    print(largestGoodInteger(n4))


