'''
Created Date: 2023-03-28
Qn: You have planned some train traveling one year in advance. The days of the
    year in which you will travel are given as an integer array days. Each day
    is an integer from 1 to 365.

    Train tickets are sold in three different ways:

        - 1-day pass is sold for costs[0] dollars
        - 7-day pass is sold for costs[1] dollars
        - 30-day pass is sold for costs[2] dollars

    The passes allow that many days of consecutive travel.

    For example, if we get a 7-day pass on day 2, then we can travel for 7
    days: 2, 3, 4, 5, 6, 7, and 8. Return the minimum number of dollars you
    need to travel every day in the given list of days.
Link: https://leetcode.com/problems/minimum-cost-for-tickets/
Notes:
    - use dp
'''
def mincostTickets(days: list[int], costs: list[int]) -> int:
    dp = {}
    def dfs(i: int) -> int:
        if i == len(days): return 0
        if i in dp: return dp[i]

        dp[i] = float('inf')
        for d, c in zip([1, 7, 30], costs):
            j = i
            while j < len(days) and days[j] < days[i] + d:
                j += 1
            dp[i] = min(dp[i], c + dfs(j))
        return dp[i]
    return dfs(0)

if __name__ == '__main__':
    d1, c1 = [1,4,6,7,8,20], [2,7,15]
    d2, c2 = [1,2,3,4,5,6,7,8,9,10,30,31], [2,7,15]

    print(mincostTickets(d1, c1))
    print(mincostTickets(d2, c2))
