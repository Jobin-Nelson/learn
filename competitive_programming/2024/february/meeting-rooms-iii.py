"""
Created Date: 2024-02-18
Qn: You are given an integer n. There are n rooms numbered from 0 to n - 1.

    You are given a 2D integer array meetings where meetings[i] = [starti,
    endi] means that a meeting will be held during the half-closed time
    interval [starti, endi). All the values of starti are unique.

    Meetings are allocated to rooms in the following manner:

        - Each meeting will take place in the unused room with the lowest
          number.
        - If there are no available rooms, the meeting will be delayed until a
          room becomes free. The delayed meeting should have the same duration
          as the original meeting. 
        - When a room becomes unused, meetings that have an earlier original
          start time should be given the room.

    Return the number of the room that held the most meetings. If there are
    multiple rooms, return the room with the lowest number.

    A half-closed interval [a, b) is the interval between a and b including a
    and not including b.
Link: https://leetcode.com/problems/meeting-rooms-iii/
Notes:
    - sort meetings and use 2 min heaps or priority queue to keep track of used
      and unused rooms
"""
from sys import maxsize
import heapq
import operator

def mostBooked(n: int, meetings: list[list[int]]) -> int:
    unused_rooms, used_rooms = list(range(n)), []
    heapq.heapify(unused_rooms)
    meeting_counts = [0] * n
    for start, end in sorted(meetings):
        while used_rooms and used_rooms[0][0] <= start:
            _, room = heapq.heappop(used_rooms)
            heapq.heappush(unused_rooms, room)
        if unused_rooms:
            room = heapq.heappop(unused_rooms)
            heapq.heappush(used_rooms, (end, room))
        else:
            room_availability_time, room = heapq.heappop(used_rooms)
            heapq.heappush(used_rooms, (room_availability_time + end - start, room))
        meeting_counts[room] += 1
    return max(enumerate(meeting_counts), key=operator.itemgetter(1))[0]
    # return meeting_count.index(max(meeting_count))

    # rooms = [0] * n
    # meeting_count = [0] * n
    #
    # for s, e in sorted(meetings):
    #     min_room_available_time = maxsize
    #     min_room_available = 0
    #     unused_room_found = False
    #
    #     for i in range(n):
    #         if rooms[i] <= s:
    #             unused_room_found = True
    #             rooms[i] = e
    #             meeting_count[i] += 1
    #             break
    #         if min_room_available_time > rooms[i]:
    #             min_room_available_time = rooms[i]
    #             min_room_available = i
    #     if not unused_room_found:
    #         rooms[min_room_available] += e - s
    #         meeting_count[min_room_available] += 1
    #
    # return meeting_count.index(max(meeting_count))


    
if __name__ == '__main__':
    n1, m1 = 2, [[0,10],[1,5],[2,7],[3,4]]
    n2, m2 = 3, [[1,20],[2,10],[3,5],[4,9],[6,8]]

    print(mostBooked(n1, m1))
    print(mostBooked(n2, m2))
