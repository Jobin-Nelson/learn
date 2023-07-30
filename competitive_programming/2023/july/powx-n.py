'''
Created Date: 2023-07-24
Qn: Implement pow(x, n), which calculates x raised to the power n (i.e., xn).
Link: https://leetcode.com/problems/powx-n/
Notes:
    - use binary exponentiation
'''
def myPow(x: float, n: int) -> float:
    # iterative
    def binaryExp(x: float, n: int) -> float:
        if n == 0: return 1
        if n < 0:
            n *= -1
            x = 1 / x
        res = 1
        while n != 0:
            if n & 1:
                res *= x
                n -= 1
            x *= x
            n >>= 1
        return res
    return binaryExp(x, n)

    # dfs
    # def binaryExp(x: float, n: int) -> float:
    #     if n == 0: return 1
    #     if n < 0: return 1 / binaryExp(x, -1 * n)
    #     if n & 1: return x * binaryExp(x * x, (n-1) >> 1)
    #     else: return binaryExp(x * x, n >> 1)
    # return binaryExp(x, n)

if __name__ == '__main__':
    x1, n1 = 2.00000, 10
    x2, n2 = 2.10000, 3
    x3, n3 = 2.00000, -2

    print(myPow(x1, n1))
    print(myPow(x2, n2))
    print(myPow(x3, n3))
