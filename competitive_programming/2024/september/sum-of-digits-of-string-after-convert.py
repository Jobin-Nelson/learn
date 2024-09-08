"""
Created Date: 2024-09-03
Qn: You are given a string s consisting of lowercase English letters, and an
    integer k.

    First, convert s into an integer by replacing each letter with its position
    in the alphabet (i.e., replace 'a' with 1, 'b' with 2, ..., 'z' with 26).
    Then, transform the integer by replacing it with the sum of its digits.
    Repeat the transform operation k times in total.

    For example, if s = "zbax" and k = 2, then the resulting integer would be 8
    by the following operations:

        - Convert: "zbax" ➝ "(26)(2)(1)(24)" ➝ "262124" ➝ 262124 
        - Transform #1: 262124 ➝ 2 + 6 + 2 + 1 + 2 + 4 ➝ 17 
        - Transform #2: 17 ➝ 1 + 7 ➝ 8 

    Return the resulting integer after performing the operations described
    above.
Link: https://leetcode.com/problems/sum-of-digits-of-string-after-convert/
Notes:
    - use remainder and integer division to add digits
"""


def getLucky(s: str, k: int) -> int:
    cur_num = 0
    for c in s:
        d = ord(c) - ord('a') + 1
        while d > 0:
            cur_num += d % 10
            d //= 10

    for _ in range(k-1):
        cur_sum = 0
        while cur_num > 0:
            cur_num, d = divmod(cur_num, 10)
            cur_sum += d
        cur_num = cur_sum
    return cur_num


if __name__ == '__main__':
    s1, k1 = "iiii", 1
    s2, k2 = "leetcode", 2
    s3, k3 = "zbax", 2

    print(getLucky(s1, k1))
    print(getLucky(s2, k2))
    print(getLucky(s3, k3))
