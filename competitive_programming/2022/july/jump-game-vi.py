'''
Created Date: 09-07-2022
Qn: You are given a 0-indexed integer array nums and an integer k.

    You are initially standing at index 0. In one move, you can jump at most k
    steps forward without going outside the boundaries of the array. That is, you
    can jump from index i to any index in the range [i + 1, min(n - 1, i + k)]
    inclusive.

    You want to reach the last index of the array (index n - 1). Your score is the
    sum of all nums[j] for each index j you visited in the array.

    Return the maximum score you can get
Link: https://leetcode.com/problems/jump-game-vi/
Notes:
    - use heap to keep track of the score and drop when the index falls outside k range
'''
import heapq

def maxResult(nums: list[int], k: int) -> int:
    N = len(nums)
    h = [(-nums[0], 0)]

    for i in range(1, N):
        while h[0][1] < i-k:
            heapq.heappop(h)
        max_score_so_far = h[0][0]
        heapq.heappush(h, (max_score_so_far-nums[i], i))
        if i == N - 1: return -(max_score_so_far-nums[i])
    return nums[0]

if __name__ == '__main__':
    n1, k1 = [1, -1, -2, 4, -7, 3], 2
    n2, k2 = [10, -5, -2, 4, 0, 3], 3
    n3, k3 = [1, -5, -20, 4, -1, 3, -6, -3], 2

    print(maxResult(n1, k1))
    print(maxResult(n2, k2))
    print(maxResult(n3, k3))
