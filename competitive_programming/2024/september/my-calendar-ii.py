"""
Created Date: 2024-09-27
Qn: You are implementing a program to use as your calendar. We can add a new
    event if adding the event will not cause a triple booking.

    A triple booking happens when three events have some non-empty intersection
    (i.e., some moment is common to all the three events.).

    The event can be represented as a pair of integers start and end that
    represents a booking on the half-open interval [start, end), the range of
    real numbers x such that start <= x < end.

    Implement the MyCalendarTwo class:

    MyCalendarTwo() Initializes the calendar object. boolean book(int start,
    int end) Returns true if the event can be added to the calendar
    successfully without causing a triple booking. Otherwise, return false and
    do not add the event to the calendar.
Link: https://leetcode.com/problems/my-calendar-ii/
Notes:
    - use two lists one for overlapping and other for non-overlapping
"""


class MyCalendarTwo:
    def __init__(self):
        self.overlapping = []
        self.non_overlapping = []

    def book(self, start: int, end: int) -> bool:
        for s, e in self.overlapping:
            if end > s and e > start:
                return False
        for s, e in self.non_overlapping:
            if end > s and e > start:
                self.overlapping.append((max(s, start), min(e, end)))
        self.non_overlapping.append((start, end))
        return True


if __name__ == '__main__':
    c1 = MyCalendarTwo()
    print(c1.book(10, 20))
    print(c1.book(50, 60))
    print(c1.book(10, 40))
    print(c1.book(5, 15))
    print(c1.book(5, 10))
    print(c1.book(25, 55))
