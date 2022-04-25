'''
Qn: Design an iterator that supports the peek operation on an existing iterator 
in addition to the hasNext and the next operations.
Link: https://leetcode.com/problems/peeking-iterator/
Notes:
'''
from __future__ import annotations
from collections import deque

class Iterator:
    def __init__(self, nums: list[int]) -> Iterator:
        '''Initializes an iterator object to the beginnnig of a list'''
        self.it = deque(nums)
    def hasNext(self) -> bool:
        '''Returns true if the iteration has more elements'''
        return len(self.it) != 0
    def next(self) -> int:
        '''Returns the next element in the iteration'''
        return self.it.popleft()

class PeekingIterator:
    def __init__(self, iterator: Iterator) -> PeekingIterator:
        '''Initialize your data structure here'''
        self.iterator = iterator
        self.peeked = None
        self.has_peeked = False

    def peek(self) -> int:
        if not self.has_peeked:
            self.peeked = self.iterator.next()
            self.has_peeked = True
        return self.peeked

    def next(self) -> int:
        if not self.has_peeked:
            return self.iterator.next()
        result = self.peeked
        self.has_peeked = False
        self.peeked = None
        return result

    def hasNext(self) -> bool:
        return self.has_peeked or self.iterator.hasNext()

if __name__ == '__main__':
    nums = [1, 2, 3]
    iter = PeekingIterator(Iterator(nums))
    print(iter.next())
    print(iter.peek())
    print(iter.next())
    print(iter.next())
    print(iter.hasNext())
