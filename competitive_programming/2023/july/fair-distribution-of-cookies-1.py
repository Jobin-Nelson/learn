'''
Created Date: 2023-07-01
Qn: You are given an integer array cookies, where cookies[i] denotes the number
    of cookies in the ith bag. You are also given an integer k that denotes the
    number of children to distribute all the bags of cookies to. All the
    cookies in the same bag must go to the same child and cannot be split up.

    The unfairness of a distribution is defined as the maximum total cookies
    obtained by a single child in the distribution.

    Return the minimum unfairness of all distributions.
Link: https://leetcode.com/problems/fair-distribution-of-cookies/
Notes:
    - use backtracking
'''
def distributeCookies(cookies: list[int], k: int) -> int:
    cur = [0] * k
    N = len(cookies)

    def dfs(i: int, zero_count: int) -> int:
        if N - i < zero_count: return float('inf')
        if i == N: return max(cur)
        res = float('inf')
        for j in range(k):
            zero_count -= int(cur[j] == 0)
            cur[j] += cookies[i]
            res = min(res, dfs(i+1, zero_count))
            cur[j] -= cookies[i]
            zero_count -= int(cur[j] == 0)
        return res
    return dfs(0, k)

if __name__ == '__main__':
    c1, k1 = [8,15,10,20,8], 2
    c2, k2 = [6,1,3,2,2,4,1,2], 3

    print(distributeCookies(c1, k1))
    print(distributeCookies(c2, k2))
