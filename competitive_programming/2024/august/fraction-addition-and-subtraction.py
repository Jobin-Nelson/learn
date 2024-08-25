"""
Created Date: 2024-08-23
Qn: Given a string expression representing an expression of fraction addition
    and subtraction, return the calculation result in string format.

    The final result should be an irreducible fraction. If your final result is
    an integer, change it to the format of a fraction that has a denominator 1.
    So in this case, 2 should be converted to 2/1.
Link: https://leetcode.com/problems/fraction-addition-and-subtraction/
Notes:
    - use regular expression
"""

import re


def fractionAddition(expression: str) -> str:
    num = 0
    denom = 1
    nums = re.split('/|(?=[-+])', expression)
    nums = list(filter(None, nums))

    for i in range(0, len(nums), 2):
        cur_num = int(nums[i])
        cur_denom = int(nums[i + 1])

        num = num * cur_denom + cur_num * denom
        denom = denom * cur_denom

    def find_gcd(a: int, b: int) -> int:
        while a:
            a, b = b % a, a
        return b

    gcd = find_gcd(num, denom)
    num //= gcd
    denom //= gcd
    if denom < 0:
        num *= -1
        denom *= -1
    return str(num) + '/' + str(denom)


if __name__ == '__main__':
    e1 = "-1/2+1/2"
    e2 = "-1/2+1/2+1/3"
    e3 = "1/3-1/2"

    print(fractionAddition(e1))
    print(fractionAddition(e2))
    print(fractionAddition(e3))
