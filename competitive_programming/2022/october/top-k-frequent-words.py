'''
Created Date: 2022-10-19
Qn: Given an array of strings words and an integer k, return the k most
    frequent strings.

    Return the answer sorted by the frequency from highest to lowest. Sort the
    words with the same frequency by their lexicographical order
Link: https://leetcode.com/problems/top-k-frequent-words/
Notes:
    - count the occurence of each word using a hashmap
    - use heap to get the top k frequent words 
'''
from collections import defaultdict
import heapq

def topKFrequent(words: list[str], k: int) -> list[str]:
    d = defaultdict(lambda: [0, ""])
    for w in words:
        d[w] = [d[w][0]-1, w]
    values = list(d.values())
    heapq.heapify(values)
    values = heapq.nsmallest(k, values)
    res = [i[1] for i in values]
    return res

if __name__ == '__main__':
    w1, k1 = ["i","love","leetcode","i","love","coding"], 2
    w2, k2 = ["the","day","is","sunny","the","the","the","sunny","is","is"], 4

    print(topKFrequent(w1, k1))
    print(topKFrequent(w2, k2))
