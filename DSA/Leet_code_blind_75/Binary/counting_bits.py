'''
Qn: Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.
Link: https://leetcode.com/problems/counting-bits/
Notes:
- there is a pattern which is repeating after each offset 1, 2, 4, 8, 16...
'''
# offset to find the number of 1's in the number
class Solution:
    def count_bits(self, n: int)->List[int]:
        dp = [0]*(n+1)
        offset = 1

        for i in range(1, n+1):
            if offset*2==i:
                offset = i
            dp[i] = 1 + dp[i-offset]
        
        return dp


def count_bits(n):
    dp = [0] * (n+1)
    offset = 1
    for i in range(1, n+1):
        if 2*offset == i:
            offset = i
        dp[i] = 1 + dp[i-offset]

    return dp

if __name__ == '__main__':
    num1 = 2
    num2 = 5
    print(count_bits(num1))
    print(count_bits(num2))