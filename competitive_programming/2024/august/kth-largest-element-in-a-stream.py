"""
Created Date: 2024-08-12
Qn: Design a class to find the kth largest element in a stream. Note that it is
    the kth largest element in the sorted order, not the kth distinct element.

    Implement KthLargest class:

    - KthLargest(int k, int[] nums) Initializes the object with the integer k
      and the stream of integers nums. 
    - int add(int val) Appends the integer val to the stream and returns the
      element representing the kth largest element in the stream.
Link: https://leetcode.com/problems/kth-largest-element-in-a-stream/
Notes:
"""

import heapq


class KthLargest:
    def __init__(self, k: int, nums: list[int]):
        self.heap = []
        self.k = k
        for n in nums:
            self.add(n)

    def add(self, val: int) -> int:
        if len(self.heap) < self.k or self.heap[0] < val:
            heapq.heappush(self.heap, val)
            if len(self.heap) > self.k:
                heapq.heappop(self.heap)
        return self.heap[0]


if __name__ == '__main__':
    o = KthLargest(3, [4, 5, 8, 2])
    print(o.add(3))
    print(o.add(5))
    print(o.add(10))
    print(o.add(9))
    print(o.add(4))
