'''
Created Date: 2023-05-23
Qn: Design a class to find the kth largest element in a stream. Note that it is
    the kth largest element in the sorted order, not the kth distinct element.

    Implement KthLargest class:

        - KthLargest(int k, int[] nums) Initializes the object with the integer
          k and the stream of integers nums. 
        - int add(int val) Appends the integer val to the stream and returns
          the element representing the kth largest element in the stream.

Link: https://leetcode.com/problems/kth-largest-element-in-a-stream/
Notes:
    - use heap
'''
import heapq

class KthLargest:
    def __init__(self, k: int, nums: list[int]):
        self.h, self.k = nums, k
        heapq.heapify(self.h)
        while len(self.h) > k:
            heapq.heappop(self.h)

    def add(self, val: int) -> int:
        heapq.heappush(self.h, val)
        if len(self.h) > self.k: heapq.heappop(self.h)
        return self.h[0]

if __name__ == '__main__':
    k = KthLargest(3, [4, 5, 8, 2])
    print(k.add(3))
    print(k.add(5))
    print(k.add(10))
    print(k.add(9))
    print(k.add(4))
