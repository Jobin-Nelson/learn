"""
Created Date: 2024-09-26
Qn: You are implementing a program to use as your calendar. We can add a new
    event if adding the event will not cause a double booking.

    A double booking happens when two events have some non-empty intersection
    (i.e., some moment is common to both events.).

    The event can be represented as a pair of integers start and end that
    represents a booking on the half-open interval [start, end), the range of
    real numbers x such that start <= x < end.

    Implement the MyCalendar class:

    MyCalendar() Initializes the calendar object. boolean book(int start, int
    end) Returns true if the event can be added to the calendar successfully
    without causing a double booking. Otherwise, return false and do not add
    the event to the calendar.
Link: https://leetcode.com/problems/my-calendar-i/
Notes:
    - use binary search tree
"""


class BST:
    def __init__(self, start: int, end: int):
        self.left = None
        self.right = None
        self.start = start
        self.end = end

    def insert(self, start: int, end: int) -> bool:
        cur = self
        while True:
            if start >= cur.end:
                if not cur.right:
                    cur.right = BST(start, end)
                    return True
                cur = cur.right
            elif end <= cur.start:
                if not cur.left:
                    cur.left = BST(start, end)
                    return True
                cur = cur.left
            else:
                return False


class MyCalendar:
    def __init__(self):
        self.root = None

    def book(self, start: int, end: int) -> bool:
        if not self.root:
            self.root = BST(start, end)
            return True
        return self.root.insert(start, end)


if __name__ == '__main__':
    c1 = MyCalendar()
    print(c1.book(10, 20))
    print(c1.book(15, 25))
    print(c1.book(20, 30))
