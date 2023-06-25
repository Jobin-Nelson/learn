'''
Created Date: 2023-06-25
Qn: You are given an array of distinct positive integers locations where
    locations[i] represents the position of city i. You are also given integers
    start, finish and fuel representing the starting city, ending city, and the
    initial amount of fuel you have, respectively.

    At each step, if you are at city i, you can pick any city j such that j !=
    i and 0 <= j < locations.length and move to city j. Moving from city i to
    city j reduces the amount of fuel you have by |locations[i] -
    locations[j]|. Please notice that |x| denotes the absolute value of x.

    Notice that fuel cannot become negative at any point in time, and that you
    are allowed to visit any city more than once (including start and finish).

    Return the count of all possible routes from start to finish. Since the
    answer may be too large, return it modulo 109 + 7.
Link: https://leetcode.com/problems/count-all-possible-routes/
Notes:
    - use dp
'''
def countPairs(locations: list[int], start: int, finish: int, fuel: int) -> int:
    N = len(locations)
    mod = 10 ** 9 + 7
    dp = [[0]* (fuel + 1) for _ in range(N)]

    for i in range(fuel + 1):
        dp[finish][i] = 1

    for j in range(fuel + 1):
        for i in range(N):
            for k in range(N):
                if k == i: continue
                if abs(locations[i] - locations[k]) <= j:
                    dp[i][j] = (dp[i][j] + dp[k][j - abs(locations[i] - locations[k])]) % mod
    return dp[start][fuel]

    # Recursive approach
    # N = len(locations)
    # mod = 10 ** 9 + 7
    # memo = [[None]*(fuel + 1) for _ in range(N)]
    #
    # def solve(curCity: int, remFuel: int) -> int:
    #     if remFuel < 0: return 0
    #     if memo[curCity][remFuel] is not None: return memo[curCity][remFuel]
    #     res = 0
    #     if curCity == finish: res += 1
    #     for nextCity in range(N):
    #         if nextCity != curCity:
    #             res += (solve(nextCity, remFuel - abs(locations[curCity] - locations[nextCity])) % mod)
    #     memo[curCity][remFuel] = res
    #     return res
    # return solve(start, fuel)
    

if __name__ == '__main__':
    l1, s1, fi1, fu1 = [2,3,6,8,4], 1, 3, 5
    l2, s2, fi2, fu2 = [4,3,1], 1, 0, 6
    l3, s3, fi3, fu3 = [5,2,1], 0, 2, 3
    l4, s4, fi4, fu4 = [1,2,3], 0, 2, 40

    print(countPairs(l1, s1, fi1, fu1))
    print(countPairs(l2, s2, fi2, fu2))
    print(countPairs(l3, s3, fi3, fu3))
    print(countPairs(l4, s4, fi4, fu4))

