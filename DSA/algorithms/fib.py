# recursion
def fib_rec(n):
    if n <= 2:   # base case
        return 1
    return fib_rec(n-1) + fib_rec(n-2)

# memoization
def fib_mem(n):
    dp = [0] * (n+1)
    dp[1] = 1

    for i in range(2, n+1):
        dp[i] = dp[i-1] + dp[i-2]

    return dp[n]

if __name__ == '__main__':
    print(fib_rec(6))
    print(fib_rec(7))
    print(fib_rec(8))

    print(fib_mem(6))
    print(fib_mem(7))
    print(fib_mem(8))
