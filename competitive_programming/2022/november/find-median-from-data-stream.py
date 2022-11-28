'''
Created Date: 2022-11-12
Qn: The median is the middle value in an ordered integer list. If the size of
    the list is even, there is no middle value, and the median is the mean of
    the two middle values.

    - For example, for arr = [2,3,4], the median is 3. 
    - For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5.

    Implement the MedianFinder class:

        - MedianFinder() initializes the MedianFinder object. 
        - void addNum(int num) adds the integer num from the data stream to the
          data structure. 
        - double findMedian() returns the median of all elements so far.
          Answers within 10^-5 of the actual answer will be accepted.
Link: https://leetcode.com/problems/find-median-from-data-stream/
Notes:
    - use 2 heaps to store bottom half and top half of the numbers
    - maintian len(bottom) = 1 + len(top)
'''
from heapq import heappush, heappop

class MedianFinder:
    def __init__(self):
        self.bot = []
        self.top = []

    def addNum(self, num: int) -> None:
        heappush(self.bot, -num)
        heappush(self.top, -heappop(self.bot))

        if len(self.top) > len(self.bot):
            heappush(self.bot, -heappop(self.top))

    def findMedian(self) -> float:
        if len(self.bot) != len(self.top):
            return -self.bot[0]
        else:
            return (self.top[0]-self.bot[0]) / 2

if __name__ == '__main__':
    mf = MedianFinder()
    mf.addNum(1)
    mf.addNum(2)
    print(mf.findMedian())
    mf.addNum(3)
    print(mf.findMedian())
