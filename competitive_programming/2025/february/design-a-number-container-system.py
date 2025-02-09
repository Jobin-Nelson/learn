"""
Created Date: 2025-02-08
Qn: Design a number container system that can do the following:

    - Insert or Replace a number at the given index in the system.
    - Return the smallest index for the given number in the system.

    Implement the NumberContainers class:

    - NumberContainers() Initializes the number container system.
    - void change(int index, int number) Fills the container at index with the
      number. If there is already a number at that index, replace it.
    - int find(int number) Returns the smallest index for the given number, or
      -1 if there is no index that is filled by number in the system.
Link: https://leetcode.com/problems/design-a-number-container-system/
Notes:
    - use either sortedset or heap
"""

import unittest
from collections import defaultdict
import heapq


class NumberContainers:
    def __init__(self):
        self.num2index = defaultdict(list)
        self.index2num = {}

    def change(self, index: int, number: int) -> None:
        self.index2num[index] = number
        heapq.heappush(self.num2index[number], index)

    def find(self, number: int) -> int:
        while self.num2index[number]:
            index = self.num2index[number][0]
            if self.index2num.get(index) == number:
                return index
            heapq.heappop(self.num2index[number])
        return -1


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = NumberContainers()

    def test_NumberContainers1(self):
        self.assertEqual(-1, self.sol.find(10))
        self.sol.change(2, 10)
        self.sol.change(1, 10)
        self.sol.change(3, 10)
        self.sol.change(5, 10)
        self.assertEqual(1, self.sol.find(10))
        self.sol.change(1, 20)
        self.assertEqual(2, self.sol.find(10))


if __name__ == '__main__':
    unittest.main()
