'''
Qn: The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value and the median is the mean of the two middle values.
Link: https://leetcode.com/problems/find-median-from-data-stream/
Notes:
'''
import heapq

class MedianFinder:
    def __init__(self):
        self.small = [] # max heap
        self.large = [] # min heap

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small, -1 * num)

        # small[i] <= large[i]
        if self.small and self.large and (-1*self.small[0]) > self.large[0]:
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)

        # uneven length
        if len(self.small) > (len(self.large) + 1):
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        if len(self.large) > (len(self.small) + 1):
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -1 * val)

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -1*self.small[0]
        if len(self.large) > len(self.small):
            return self.large[0]
        return (-1*self.large[0] + self.small[0]) / 2


if __name__ == '__main__':
    obj = MedianFinder()
    obj.addNum(1)
    obj.addNum(2)
    print(obj.findMedian())
    obj.addNum(3)
    print(obj.findMedian())
