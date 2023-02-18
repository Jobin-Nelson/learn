'''
Created Date: 2023-02-14
Qn: Given two binary strings a and b, return their sum as a binary string.
Link: https://leetcode.com/problems/add-binary/
Notes:
    - use stack
'''
def addBinary(a: str, b: str) -> str:
    res = []
    carry = 0
    i, j = len(a)-1, len(b)-1

    while i >= 0 or j >=0 or carry:
        if i >= 0:
            carry += int(a[i])
            i -= 1
        if j >= 0:
            carry += int(b[j])
            j -= 1
        res.append(str(carry & 1))
        carry >>= 1

    return ''.join(reversed(res))

if __name__ == '__main__':
    a1, b1 = "11", "1"
    a2, b2 = "1010", "1011"

    print(addBinary(a1, b1))
    print(addBinary(a2, b2))
