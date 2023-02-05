'''
Created Date: 2023-01-28
Qn: Given a data stream input of non-negative integers a1, a2, ..., an,
summarize the numbers seen so far as a list of disjoint intervals.

Implement the SummaryRanges class:

    - SummaryRanges() Initializes the object with an empty stream. 
    - void addNum(int value) Adds the integer value to the stream. 
    - int[][] getIntervals() Returns a summary of the integers in the stream
      currently as a list of disjoint intervals [starti, endi]. The answer
      should be sorted by starti.
Link: https://leetcode.com/problems/data-stream-as-disjoint-intervals/
Notes:
    - use set or sortedconainers
    - find left & right disjoint numbers in each iteration
'''
class SummaryRanges:
    def __init__(self):
        self.nums = set()
    def addNum(self, value: int) -> None:
        self.nums.add(value)
    def getIntervals(self) -> list[list[int]]:
        intervals = []
        seen = set()

        for num in self.nums:
            if num in seen: continue

            left = num
            while left-1 in self.nums:
                left -= 1
                seen.add(left)
            right = num
            while right+1 in self.nums:
                right += 1
                seen.add(right)
            intervals.append([left, right])
        return sorted(intervals)

if __name__ == '__main__':
    sr = SummaryRanges()
    sr.addNum(1)
    print(sr.getIntervals())
    sr.addNum(3)
    print(sr.getIntervals())
    sr.addNum(7)
    print(sr.getIntervals())
    sr.addNum(2)
    print(sr.getIntervals())
    sr.addNum(6)
    print(sr.getIntervals())
