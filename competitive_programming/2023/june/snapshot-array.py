'''
Created Date: 2023-06-11
Qn: Implement a SnapshotArray that supports the following interface:

    - SnapshotArray(int length) initializes an array-like data structure with
      the given length. Initially, each element equals 0. 
    - void set(index, val) sets the element at the given index to be equal to
      val. 
    - int snap() takes a snapshot of the array and returns the snap_id: the
      total number of times we called snap() minus 1. 
    - int get(index, snap_id) returns the value at the given index, at the time
      we took the snapshot with the given snap_id

Link: https://leetcode.com/problems/snapshot-array/
Notes:
'''
import bisect

class SnapshotArray:
    def __init__(self, length: int):
        self.id = 0
        self.array = [[[0,0]] for _ in range(length)]
    def set(self, index: int, val: int) -> None:
        self.array[index].append([self.id, val])
    def snap(self) -> int:
        self.id += 1
        return self.id - 1
    def get(self, index: int, snap_id: int) -> int:
        snap_index = bisect.bisect_right(self.array[index], [snap_id, 10**9])
        return self.array[index][snap_index-1][1]

if __name__ == '__main__':
    s = SnapshotArray(3)
    s.set(0, 5)
    print(s.snap())
    s.set(0, 6)
    print(s.get(0,0))
