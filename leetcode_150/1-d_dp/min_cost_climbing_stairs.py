def minCostClimbingStairs(cost: list[int]) -> int:
    if len(cost) <= 2: return min(cost)
    first, second = cost[0], cost[1]

    for i in range(2, len(cost)):
        first, second = second, cost[i] + min(first, second)

    return min(first, second)


if __name__ == "__main__":
    c1 = [1, 2, 3]
    c2 = [1, 2, 1, 2, 1, 1, 1]
    print(minCostClimbingStairs(c1))
    print(minCostClimbingStairs(c2))
