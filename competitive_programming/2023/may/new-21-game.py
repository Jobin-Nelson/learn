'''
Created Date: 2023-05-25
Qn: Alice plays the following game, loosely based on the card game "21".

    Alice starts with 0 points and draws numbers while she has less than k
    points. During each draw, she gains an integer number of points randomly
    from the range [1, maxPts], where maxPts is an integer. Each draw is
    independent and the outcomes have equal probabilities.

    Alice stops drawing numbers when she gets k or more points.

    Return the probability that Alice has n or fewer points.

    Answers within 10-5 of the actual answer are considered accepted.
Link: https://leetcode.com/problems/new-21-game/
Notes:
    - use vector dp sliding window
'''
def new21Game(n: int, k: int, maxPts: int) -> float:
    if k == 0 or n >= k + maxPts:
        return 1.0
    
    dp = [0.0] * (n+1)
    dp[0] = 1.0
    sum, res = 1.0, 0.0
    for i in range(1, n+1):
        dp[i] = sum / maxPts
        if i < k:
            sum += dp[i]
        else:
            res += dp[i]
        if i >= maxPts:
            sum -= dp[i-maxPts]
    return res

if __name__ == '__main__':
    n1, k1, m1 = 10, 1, 10
    n2, k2, m2 = 6, 1, 10
    n3, k3, m3 = 21, 17, 10
    n4, k4, m4 = 1, 0, 2

    print(new21Game(n1, k1, m1))
    print(new21Game(n2, k2, m2))
    print(new21Game(n3, k3, m3))
    print(new21Game(n4, k4, m4))
