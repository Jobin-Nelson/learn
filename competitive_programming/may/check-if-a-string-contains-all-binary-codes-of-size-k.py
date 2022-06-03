'''
Qn: Given a binary string s and an integer k, return true if every 
    binary code of length k is a substring of s. Otherwise, return false.
Link: https://leetcode.com/problems/check-if-a-string-contains-all-binary-codes-of-size-k/
Notes:
- take all the unique substring of s with length k and return if it is equal to 2**k
'''
def hasAllCodes(s: str, k: int) -> bool:
    code_set = set()
    for i in range(len(s)-k+1):
        code_set.add(s[i:i+k])
    return len(code_set) == 2**k

if __name__ == '__main__':
    s1, s2, s3 = "00110110", "0110", "0110"
    k1, k2, k3 = 2, 1, 2
    print(hasAllCodes(s1, k1))
    print(hasAllCodes(s2, k2))
    print(hasAllCodes(s3, k3))
