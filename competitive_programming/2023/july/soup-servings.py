'''
Created Date: 2023-07-29
Qn: There are two types of soup: type A and type B. Initially, we have n ml of
    each type of soup. There are four kinds of operations:

        - Serve 100 ml of soup A and 0 ml of soup B,
        - Serve 75 ml of soup A and 25 ml of soup B,
        - Serve 50 ml of soup A and 50 ml of soup B, and
        - Serve 25 ml of soup A and 75 ml of soup B.

    When we serve some soup, we give it to someone, and we no longer have it.
    Each turn, we will choose from the four operations with an equal
    probability 0.25. If the remaining volume of soup is not enough to complete
    the operation, we will serve as much as possible. We stop once we no longer
    have some quantity of both types of soup.

    Note that we do not have an operation where all 100 ml's of soup B are used
    first.

    Return the probability that soup A will be empty first, plus half the
    probability that A and B become empty at the same time. Answers within 10-5
    of the actual answer will be accepted.
Link: https://leetcode.com/problems/soup-servings/
Notes:
    - use dp and memoization
'''
import math

def soupServings(n: int) -> float:
    m = math.ceil(n / 25)
    dp = {}

    def calculate_dp(i: int, j: int) -> float:
        if i <= 0 and j <= 0: return 0.5
        if i <= 0: return 1.0
        if j <= 0: return 0.0
        if (i, j) in dp: return dp[(i, j)]
        
        dp[(i, j)] = (
            calculate_dp(i-4, j)
            + calculate_dp(i-3, j-1)
            + calculate_dp(i-2, j-2)
            + calculate_dp(i-1, j-3) 
        ) / 4.0
        return dp[(i, j)]

    for k in range(1, m+1):
        if calculate_dp(k, k) > 1 - 1e-5: return 1.0
    return calculate_dp(m, m)

if __name__ == '__main__':
    n1 = 50
    n2 = 100

    print(soupServings(n1))
    print(soupServings(n2))
