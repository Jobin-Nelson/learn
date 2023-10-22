'''
Created Date: 2023-10-20
Qn: You are given a nested list of integers nestedList. Each element is either
    an integer or a list whose elements may also be integers or other lists.
    Implement an iterator to flatten it.

    Implement the NestedIterator class:

        - NestedIterator(List<NestedInteger> nestedList) Initializes the
          iterator with the nested list nestedList. 
        - int next() Returns the next integer in the nested list. 
        - boolean hasNext() Returns true if there are still some integers in
          the nested list and false otherwise.

    Your code will be tested with the following pseudocode:

    initialize iterator with nestedList
    res = []
    while iterator.hasNext()
        append iterator.next() to the end of res
    return res

    If res matches the expected flattened list, then your code will be judged
    as correct.
Link: https://leetcode.com/problems/flatten-nested-list-iterator/
Notes:
    - use recrusion to flatten
'''
from collections import deque


class NestedInteger:
    def __init__(self, arr):
        self.val = arr
    def isInteger(self) -> bool:
        return isinstance(self.val, int)
    def getInteger(self) -> int:
        return self.val
    def getList(self):
        return self.val
    
class NestedIterators:
    def __init__(self, nestedList: list[NestedInteger]):
        self.l = nestedList
        self.res = deque([])
        def dfs(arr):
            for i in arr:
                if i.isInteger():
                    self.res.append(i.getInteger())
                else:
                    dfs(i.getList())
        dfs(self.l)
    def next(self) -> int:
        return self.res.popleft()
    def hasNext(self) -> bool:
        return bool(self.res)

if __name__ == '__main__':

