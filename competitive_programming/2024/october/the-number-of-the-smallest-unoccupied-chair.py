"""
Created Date: 2024-10-11
Qn: There is a party where n friends numbered from 0 to n - 1 are attending.
    There is an infinite number of chairs in this party that are numbered from
    0 to infinity. When a friend arrives at the party, they sit on the
    unoccupied chair with the smallest number.

    - For example, if chairs 0, 1, and 5 are occupied when a friend comes, they
      will sit on chair number 2. When a friend leaves the party, their chair
      becomes unoccupied at the moment they leave. If another friend arrives at
      that same moment, they can sit in that chair.

    You are given a 0-indexed 2D integer array times where times[i] =
    [arrivali, leavingi], indicating the arrival and leaving times of the ith
    friend respectively, and an integer targetFriend. All arrival times are
    distinct.

    Return the chair number that the friend numbered targetFriend will sit on.
Link: https://leetcode.com/problems/the-number-of-the-smallest-unoccupied-chair/
Notes:
    - use two heaps
"""

import heapq


def smallestChair(times: list[list[int]], targetFriend: int) -> int:
    st = sorted((*t, i) for i, t in enumerate(times))
    used_chairs = []  # [(l, chair)]
    available_chairs = list(range(len(times)))  # [chair]

    for a, l, i in st:
        while used_chairs and used_chairs[0][0] <= a:
            _, chair = heapq.heappop(used_chairs)
            heapq.heappush(available_chairs, chair)
        chair = heapq.heappop(available_chairs)
        heapq.heappush(used_chairs, (l, chair))

        if i == targetFriend:
            return chair
    return 0


if __name__ == '__main__':
    t1, tf1 = [[1, 4], [2, 3], [4, 6]], 1
    t2, tf2 = [[3, 10], [1, 5], [2, 6]], 0

    print(smallestChair(t1, tf1))
    print(smallestChair(t2, tf2))
