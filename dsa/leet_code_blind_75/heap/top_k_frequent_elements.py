'''
Qn: Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.
Link: https://leetcode.com/problems/top-k-frequent-elements/
Notes:
- using Counter and heapq to get the k most frequent items in a list
'''
from collections import Counter
import heapq

def top_k_frequent(nums: list[int], k: int) -> list[int]:
    count = {}
    freq = [[] for i in range(len(nums)+1)]

    for n in nums:
        count[n] = 1 + count.get(n, 0)
    
    for n, c in count.items():
        freq[c].append(n)
    
    res = []
    for i in range(len(freq)-1, 0, -1):
        for n in freq[i]:
            res.append(n)
            if len(res) == k:
                return res


def topKFrequent(nums, k):
    if k == len(nums):
        return nums

    count = Counter(nums)
    return heapq.nlargest(k, count.keys(), key=count.get)

if __name__ == '__main__':
    n1, k1 = [1,1,1,2,2,3], 2
    n2, k2 = [1], 1
    print(top_k_frequent(n1, k1))
    print(top_k_frequent(n2, k2))
    print('Using heap')
    print(topKFrequent(n1, k1))
    print(topKFrequent(n2, k2))