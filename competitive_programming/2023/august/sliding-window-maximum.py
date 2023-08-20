'''
Created Date: 2023-08-16
Qn: You are given an array of integers nums, there is a sliding window of size
    k which is moving from the very left of the array to the very right. You
    can only see the k numbers in the window. Each time the sliding window
    moves right by one position.

    Return the max sliding window.
Link: https://leetcode.com/problems/sliding-window-maximum/
Notes:
    - use monotonic deque
'''
from collections import deque

def maxSlidingWindow(nums: list[int], k: int) -> list[int]:
    res = []
    q = deque()
    l = r = 0

    while r < len(nums):
        while q and nums[q[-1]] < nums[r]:
            q.pop()
        q.append(r)

        if l > q[0]:
            q.popleft()

        if (r+1) >= k:
            res.append(nums[q[0]])
            l += 1
        r += 1
    return res

if __name__ == '__main__':
    n1, k1 = [1,3,-1,-3,5,3,6,7], 3
    n2, k2 = [1], 1

    print(maxSlidingWindow(n1, k1))
    print(maxSlidingWindow(n2, k2))
