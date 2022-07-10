'''
Created Date: 10-07-2022
Qn: You are given an integer array cost where cost[i] is the cost of ith step on
    a staircase. Once you pay the cost, you can either climb one or two steps. You
    can either start from the step with index 0, or the step with index 1. Return
    the minimum cost to reach the top of the floor.
Link: https://leetcode.com/problems/min-cost-climbing-stairs/
Notes:
- append a zero to last to signify the reaching the top
- iterate backwards to find the min cost to reach the top
'''
def minCostClimbingStairs(cost: list[int]) -> int:
    cost.append(0)
    for i in range(len(cost)-3, -1, -1):
        cost[i] += min(cost[i+1], cost[i+2])
    return min(cost[0], cost[1])

if __name__ == '__main__':
    c1 = [10, 15, 20]
    c2 = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
    
    print(minCostClimbingStairs(c1))
    print(minCostClimbingStairs(c2))
