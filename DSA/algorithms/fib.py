# recursion
def fib_rec(n):
    if n <= 2:   # base case
        return 1
    return fib_rec(n-1) + fib_rec(n-2)

# tabulation
def fib_tab(n):
    dp = [0] * (n+1)
    dp[1] = 1

    for i in range(2, n+1):
        dp[i] = dp[i-1] + dp[i-2]

    return dp[n]

# memoization
def fib_memoization(n, memo=None):
    if memo == None:
        memo = dict()
    if n in memo:
        return memo[n]
    if n <= 2:
        return 1

    memo[n] = fib_memoization(n-1, memo) + fib_memoization(n-2, memo)
    return memo[n]

if __name__ == '__main__':
    print(fib_rec(6))
    print(fib_rec(7))
    print(fib_rec(8))

    print(fib_tab(6))
    print(fib_tab(7))
    print(fib_tab(8))

    print(fib_memoization(6))
    print(fib_memoization(7))
    print(fib_memoization(8))
