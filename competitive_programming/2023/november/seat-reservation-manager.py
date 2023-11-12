'''
Created Date: 2023-11-06
Qn: Design a system that manages the reservation state of n seats that are
    numbered from 1 to n.

    Implement the SeatManager class:

        - SeatManager(int n) Initializes a SeatManager object that will manage
          n seats numbered from 1 to n. All seats are initially available. 
        - int reserve() Fetches the smallest-numbered unreserved seat, reserves
          it, and returns its number. 
        - void unreserve(int seatNumber) Unreserves the seat with the given
          seatNumber.

Link: https://leetcode.com/problems/seat-reservation-manager/
Notes:
    - use min-heap
'''
import heapq
class SeatManager:
    def __init__(self, n: int):
        self.marker = 1
        self.available_seats = []
    def reserve(self) -> int:
        if self.available_seats: return heapq.heappop(self.available_seats)
        seat_number = self.marker
        self.marker += 1
        return seat_number
    def unreserve(self, seatNumber: int) -> None:
        heapq.heappush(self.available_seats, seatNumber)

if __name__ == '__main__':
    s = SeatManager(5)
    print(s.reserve())
    print(s.reserve())
    print(s.unreserve(2))
    print(s.reserve())
    print(s.reserve())
    print(s.reserve())
    print(s.reserve())
    print(s.unreserve(5))
