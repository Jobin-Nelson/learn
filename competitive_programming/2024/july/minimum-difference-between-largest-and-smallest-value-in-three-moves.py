"""
Created Date: 2024-07-03
Qn: You are given an integer array nums.

    In one move, you can choose one element of nums and change it to any value.

    Return the minimum difference between the largest and smallest value of
    nums after performing at most three moves.
Link: https://leetcode.com/problems/minimum-difference-between-largest-and-smallest-value-in-three-moves/
Notes:
    - use heap
"""
import heapq
from sys import maxsize

def minDifference(nums: list[int]) -> int:
    num_size = len(nums)
    if num_size <= 4:
        return 0
    smallest_four = sorted(heapq.nsmallest(4, nums))
    largest_four = sorted(heapq.nlargest(4, nums))

    min_diff = maxsize
    for i in range(4):
        min_diff = min(min_diff, largest_four[i] - smallest_four[i])
    return min_diff

if __name__ == '__main__':
    n1 = [5, 3, 2, 4]
    n2 = [1, 5, 0, 10, 14]
    n3 = [3, 100, 20]

    print(minDifference(n1))
    print(minDifference(n2))
    print(minDifference(n3))
