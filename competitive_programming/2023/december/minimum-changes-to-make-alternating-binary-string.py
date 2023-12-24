"""
Created Date: 2023-12-24
Qn: You are given a string s consisting only of the characters '0' and '1'. In
    one operation, you can change any '0' to '1' or vice versa.

    The string is called alternating if no two adjacent characters are equal.
    For example, the string "010" is alternating, while the string "0100" is
    not.

    Return the minimum number of operations needed to make s alternating.
Link: https://leetcode.com/problems/minimum-changes-to-make-alternating-binary-string/
Notes:
    - there are only 2 possibilities sequence that starts with 1 or 0
    - we only have to keep track of one, and compute the other by len(s) - start0
"""
def minOperations(s: str) -> int:
    first = 0
    cur_bit = 0

    for d in s:
        if d == str(cur_bit):
            first += 1
        cur_bit ^= 1
    return min(first, len(s)-first)

if __name__ == '__main__':
    s1 = "0100"
    s2 = "10"
    s3 = "1111"

    print(minOperations(s1))
    print(minOperations(s2))
    print(minOperations(s3))
