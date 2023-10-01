'''
Created Date: 2023-09-27
Qn: You are given an encoded string s. To decode the string to a tape, the
    encoded string is read one character at a time and the following steps are
    taken:

        If the character read is a letter, that letter is written onto the
        tape. If the character read is a digit d, the entire current tape is
        repeatedly written d - 1 more times in total.

    Given an integer k, return the kth letter (1-indexed) in the decoded
    string.
Link: https://leetcode.com/problems/decoded-string-at-index/
Notes:
    - don't store the strings
    - we can calculate the size of the string
'''
def decodeAtIndex(s: str, k: int) -> str:
    size = 0

    for c in s:
        if c.isdigit():
            size *= int(c)
        else:
            size += 1

    for i in range(len(s)-1, -1, -1):
        c = s[i]
        k %= size
        if (k == 0 or k == size) and c.isalpha():
            return c
        if c.isdigit():
            size //= int(c)
        else:
            size -= 1

if __name__ == '__main__':
    s1, k1 = "leet2code3", 10
    s2, k2 = "ha22", 5
    s3, k3 = "a2345678999999999999999", 1
    s4, k4 = "a23", 6

    print(decodeAtIndex(s1, k1))
    print(decodeAtIndex(s2, k2))
    print(decodeAtIndex(s3, k3))
    print(decodeAtIndex(s4, k4))
