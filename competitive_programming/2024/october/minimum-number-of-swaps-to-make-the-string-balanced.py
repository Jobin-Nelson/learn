"""
Created Date: 2024-10-08
Qn: You are given a 0-indexed string s of even length n. The string consists of
    exactly n / 2 opening brackets '[' and n / 2 closing brackets ']'.

    A string is called balanced if and only if:

    - It is the empty string, or
    - It can be written as AB, where both A and B are balanced strings, or
    - It can be written as [C], where C is a balanced string.

    You may swap the brackets at any two indices any number of times.

    Return the minimum number of swaps to make s balanced.
Link: https://leetcode.com/problems/minimum-number-of-swaps-to-make-the-string-balanced/
Notes:
"""


def minSwaps(s: str) -> int:
    close, maxClose = 0, 0
    for c in s:
        if c == '[':
            close -= 1
        else:
            close += 1
        maxClose = max(close, maxClose)
    return (maxClose + 1) >> 1


if __name__ == '__main__':
    s1 = "][]["
    s2 = "]]][[["
    s3 = "[]"

    print(minSwaps(s1))
    print(minSwaps(s2))
    print(minSwaps(s3))
