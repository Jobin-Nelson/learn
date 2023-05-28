'''
Created Date: 2023-05-22
Qn: Given an integer array nums and an integer k, return the k most frequent
elements. You may return the answer in any order.
Link: https://leetcode.com/problems/top-k-frequent-elements/
Notes:
    - use counter to get the counts
    - use heap to pop off the first K most frequent numbers
'''
from collections import Counter
import heapq

def topKFrequent(nums: list[int], k: int) -> list[int]:
    c = Counter(nums)
    h = []

    for num, freq in c.items():
        heapq.heappush(h, (-freq, num))

    res = []
    for _ in range(k):
        res.append(heapq.heappop(h)[1])

    return res

if __name__ == '__main__':
    n1, k1 = [1,1,1,2,2,3], 2
    n2, k2 = [1], 1

    print(topKFrequent(n1 ,k1))
    print(topKFrequent(n2 ,k2))
