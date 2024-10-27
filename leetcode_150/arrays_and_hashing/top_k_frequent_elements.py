def topKFrequent(nums: list[int], k: int) -> list[int]:
    count = {}
    for n in nums:
        count[n] = count.get(n, 0) + 1
    return sorted(count.keys(), key=lambda x: count[x], reverse=True)[:k]

