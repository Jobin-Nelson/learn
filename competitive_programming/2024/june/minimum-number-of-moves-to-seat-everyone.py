"""
Created Date: 2024-06-13
Qn: There are n seats and n students in a room. You are given an array seats of
    length n, where seats[i] is the position of the ith seat. You are also
    given the array students of length n, where students[j] is the position of
    the jth student.

    You may perform the following move any number of times:

        Increase or decrease the position of the ith student by 1 (i.e., moving
        the ith student from position x to x + 1 or x - 1)

    Return the minimum number of moves required to move each student to a seat
    such that no two students are in the same seat.

    Note that there may be multiple seats or students in the same position at
    the beginning.
Link: https://leetcode.com/problems/minimum-number-of-moves-to-seat-everyone/
Notes:
    - sort and sum the difference
"""
from collections import Counter

def minMovesToSeat(seats: list[int], students: list[int]) -> int:
    seats.sort()
    students.sort()
    return sum(abs(seat - student) for seat,student in zip(seats, students))

if __name__ == '__main__':
    se1, st1 = [3,1,5], [2,7,4]
    se2, st2 = [4,1,5,9], [1,3,2,6]
    se3, st3 = [2,2,6,6], [1,3,2,6]

    print(minMovesToSeat(se1, st1))
    print(minMovesToSeat(se2, st2))
    print(minMovesToSeat(se3, st3))
