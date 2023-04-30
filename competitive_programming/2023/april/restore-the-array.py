'''
Created Date: 2023-04-23
Qn: A program was supposed to print an array of integers. The program forgot to
    print whitespaces and the array is printed as a string of digits s and all
    we know is that all integers in the array were in the range [1, k] and
    there are no leading zeros in the array.

    Given the string s and the integer k, return the number of the possible
    arrays that can be printed as s using the mentioned program. Since the
    answer may be very large, return it modulo 109 + 7.
Link: https://leetcode.com/problems/restore-the-array/
Notes:
    - use dp (bottom-up)
    - since there are no leading zeros we skip the iteration starting with zero
'''
def numberOfArrays(s: str, k: int) -> int:
    n = len(s)
    mod = 10**9 + 7
    dp = [0] * (n + 1)
    dp[-1] = 1

    for i in range(n-1, -1, -1):
        if s[i] == '0': continue
        num = 0
        j = i
        while j < n and int(s[i:j+1]) <= k:
            num += dp[j+1]
            j += 1
        dp[i] = num % mod

    return dp[0]

if __name__ == '__main__':
    s1, k1 = "1000", 10000
    s2, k2 = "1000", 10
    s3, k3 = "1317", 2000

    print(numberOfArrays(s1, k1))
    print(numberOfArrays(s2, k2))
    print(numberOfArrays(s3, k3))
