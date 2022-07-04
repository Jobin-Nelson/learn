'''
Created Date: 24-06-2022
Qn: You are given an array target of n integers. From a starting array arr 
    consisting of n 1's, you may perform the following procedure :
        - let x be the sum of all elements currently in your array.
        - choose index i, such that 0 <= i < n and set the value of arr at index i to x.
        - You may repeat this procedure as many times as needed.
    Return true if it is possible to construct the target array from arr, otherwise, 
    return false.
Link: https://leetcode.com/problems/construct-target-array-with-multiple-sums/
Notes:
- use heap to pop off max values and reduce from total
'''
import heapq

def isPossible(target: list[int]) -> bool:
    h = [-n for n in target]
    total = sum(target)
    heapq.heapify(h)

    while h[0] != -1:
        cand = -heapq.heappop(h)
        rest_of = total - cand
        if rest_of <= 0 or cand <= rest_of: return False
        prev = cand % rest_of
        heapq.heappush(h, -prev)
        total -= cand 
        total += prev
    return True

if __name__ == '__main__':
    t1 = [9, 3, 5]
    t2 = [1, 1, 1, 2]
    t3 = [8, 5]
    print(isPossible(t1))
    print(isPossible(t2))
    print(isPossible(t3))
