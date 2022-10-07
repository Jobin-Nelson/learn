'''
Created Date: 2022-10-07
Qn: A k-booking happens when k events have some non-empty intersection (i.e.,
    there is some time that is common to all k events.)

    You are given some events [start, end), after each given event, return an
    integer k representing the maximum k-booking between all the previous
    events.

    Implement the MyCalendarThree class:

    - MyCalendarThree() Initializes the object. 
    - int book(int start, int end) Returns an integer k representing the
      largest integer such that there exists a k-booking in the calendar.
Link: https://leetcode.com/problems/my-calendar-iii/
Notes:
    - dictionary to map the start to +1 and end to -1
    - sort the keys, return the max value
'''
from collections import defaultdict

class MyCalendarThree:
    def __init__(self):
        self.times = defaultdict(int)
    def book(self, start: int, end: int) -> int:
        self.times[start] += 1
        self.times[end] -= 1

        res = cur_inter = 0
        for t in sorted(self.times):
            cur_inter += self.times[t]
            res = max(res, cur_inter)
        return res

if __name__ == '__main__':
    c = MyCalendarThree()
    print(c.book(10, 20))
    print(c.book(50, 60))
    print(c.book(10, 40))
    print(c.book(5, 15))
    print(c.book(5, 10))
    print(c.book(25, 55))
