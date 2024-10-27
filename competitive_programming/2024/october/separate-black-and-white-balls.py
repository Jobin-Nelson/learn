"""
Created Date: 2024-10-15
Qn: There are n balls on a table, each ball has a color black or white.

    You are given a 0-indexed binary string s of length n, where 1 and 0
    represent black and white balls, respectively.

    In each step, you can choose two adjacent balls and swap them.

    Return the minimum number of steps to group all the black balls to the
    right and all the white balls to the left.
Link: https://leetcode.com/problems/separate-black-and-white-balls/
Notes:
    - use black ball counter
"""


def minimumSteps(s: str) -> int:
    black_count = 0
    swap = 0
    for c in s:
        if c == '0':
            swap += black_count
        else:
            black_count += 1
    return swap



if __name__ == '__main__':
    s1 = "101"
    s2 = "100"
    s3 = "0111"

    print(minimumSteps(s1))
    print(minimumSteps(s2))
    print(minimumSteps(s3))
