"""
Created Date: 2024-10-16
Qn: A string s is called happy if it satisfies the following conditions:

    - s only contains the letters 'a', 'b', and 'c'.
    - s does not contain any of "aaa", "bbb", or "ccc" as a substring.
    - s contains at most a occurrences of the letter 'a'.
    - s contains at most b occurrences of the letter 'b'.
    - s contains at most c occurrences of the letter 'c'.

    Given three integers a, b, and c, return the longest possible happy string.
    If there are multiple longest happy strings, return any of them. If there
    is no such string, return the empty string "".

    A substring is a contiguous sequence of characters within a string.
Link: https://leetcode.com/problems/longest-happy-string/
Notes:
    - greedy approach
"""


def longestDiverseString(a: int, b: int, c: int) -> str:
    res = []
    a_count = 0
    b_count = 0
    c_count = 0
    for _ in range(a + b + c):
        if (a >= b and a >= c and a_count != 2) or (
            a > 0 and (b_count == 2 or c_count == 2)
        ):
            res.append('a')
            a_count += 1
            b_count = 0
            c_count = 0
            a -= 1
        elif (b >= a and b >= c and b_count != 2) or (
            b > 0 and (a_count == 2 or c_count == 2)
        ):
            res.append('b')
            a_count = 0
            b_count += 1
            c_count = 0
            b -= 1
        elif (c >= a and c >= b and c_count != 2) or (
            c > 0 and (b_count == 2 or a_count == 2)
        ):
            res.append('c')
            a_count = 0
            b_count = 0
            c_count += 1
            c -= 1
    return ''.join(res)


if __name__ == '__main__':
    a1, b1, c1 = 1, 1, 7
    a2, b2, c2 = 7, 1, 0

    print(longestDiverseString(a1, b1, c1))
    print(longestDiverseString(a2, b2, c2))
