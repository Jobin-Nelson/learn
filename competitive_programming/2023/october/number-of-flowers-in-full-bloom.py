'''
Created Date: 2023-10-11
Qn: You are given a 0-indexed 2D integer array flowers, where flowers[i] =
    [starti, endi] means the ith flower will be in full bloom from starti to
    endi (inclusive). You are also given a 0-indexed integer array people of
    size n, where people[i] is the time that the ith person will arrive to see
    the flowers.

    Return an integer array answer of size n, where answer[i] is the number of
    flowers that are in full bloom when the ith person arrives.
Link: https://leetcode.com/problems/number-of-flowers-in-full-bloom/
Notes:
    - use min heap
'''
import heapq

def fullBloomFlowers(flowers: list[list[int]], people: list[int]) -> list[int]:
    people_sorted = sorted((p, i) for i, p in enumerate(people))

    flowers.sort()
    end = []
    res = [0] * len(people)
    j = 0
    for p, i in people_sorted:
        while j < len(flowers) and flowers[j][0] <= p:
            heapq.heappush(end, flowers[j][1])
            j += 1
        while end and end[0] < p:
            heapq.heappop(end)
        res[i] = len(end)
    return res

if __name__ == '__main__':
    f1, p1 = [[1,6],[3,7],[9,12],[4,13]], [2,3,7,11]
    f2, p2 = [[1,10],[3,3]], [3,3,2]

    print(fullBloomFlowers(f1, p1))
    print(fullBloomFlowers(f2, p2))

