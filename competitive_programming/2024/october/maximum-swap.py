"""
Created Date: 2024-10-17
Qn: You are given an integer num. You can swap two digits at most once to get
    the maximum valued number.

    Return the maximum valued number you can get.
Link: https://leetcode.com/problems/maximum-swap/
Notes:
    - track index of max_digit_index
"""


def maximumSwap(num: int) -> int:
    num_str = list(str(num))
    n = len(num_str)
    max_digit_index = -1
    swapi1 = -1
    swapi2 = -1

    for i in range(n - 1, -1, -1):
        if max_digit_index == -1 or num_str[i] > num_str[max_digit_index]:
            max_digit_index = i
        elif num_str[i] < num_str[max_digit_index]:
            swapi1 = i
            swapi2 = max_digit_index

    if swapi1 != -1 and swapi2 != -1:
        num_str[swapi1], num_str[swapi2] = num_str[swapi2], num_str[swapi1]
    return int(''.join(num_str))


if __name__ == '__main__':
    n1 = 2736
    n2 = 9973

    print(maximumSwap(n1))
    print(maximumSwap(n2))
