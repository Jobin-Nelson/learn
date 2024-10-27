def maxProfit(prices: list[int]) -> int:
    res = 0
    lowest = prices[0]
    for p in prices:
        if p < lowest:
            lowest = p
        res = max(res, p - lowest)
    return res

if __name__ == "__main__":
    p1 = [10,1,5,6,7,1]
    p2 = [0,8,7,5,2]

    print(maxProfit(p1))
    print(maxProfit(p2))
