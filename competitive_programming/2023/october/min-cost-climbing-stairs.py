'''
Created Date: 2023-10-13
Qn: You are given an integer array cost where cost[i] is the cost of ith step
    on a staircase. Once you pay the cost, you can either climb one or two
    steps.

    You can either start from the step with index 0, or the step with index 1.

    Return the minimum cost to reach the top of the floor.
Link: https://leetcode.com/problems/min-cost-climbing-stairs/
Notes:
    - use two pointers
'''
def minCostClimbingStairs(cost: list[int]) -> int:
    N = len(cost)
    if N < 2: return min(cost)
    prev, cur = 0, 0

    for i in range(2, N+1):
        cur, prev = min(cur + cost[i-1], prev + cost[i-2]), cur
    return cur

if __name__ == '__main__':
    c1 = [10,15,20]
    c2 = [1,100,1,1,1,100,1,1,100,1]

    print(minCostClimbingStairs(c1))
    print(minCostClimbingStairs(c2))
