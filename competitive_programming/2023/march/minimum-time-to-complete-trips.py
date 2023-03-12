'''
Created Date: 2023-03-07
Qn: You are given an array time where time[i] denotes the time taken by the ith
    bus to complete one trip.

    Each bus can make multiple trips successively; that is, the next trip can
    start immediately after completing the current trip. Also, each bus
    operates independently; that is, the trips of one bus do not influence the
    trips of any other bus.

    You are also given an integer totalTrips, which denotes the number of trips
    all buses should make in total. Return the minimum time required for all
    buses to complete at least totalTrips trips.
Link: https://leetcode.com/problems/minimum-time-to-complete-trips/
Notes:
    - use binary search
    - l, r = 0, min(time) * totalTrips
    - we know for sure that min(time) * totalTrips would be enough time to
      complete totalTrips
'''
def minimumTime(time: list[int], totalTrips: int) -> int:
    def check_status(target: int) -> bool:
        return sum(target // n for n in time) >= totalTrips

    l, r = 0, min(time) * totalTrips

    while l < r:
        m = l + ((r -l) >> 1)
        if check_status(m):
            r = m
        else:
            l = m + 1
    return l

if __name__ == '__main__':
    ti1, to1 = [1, 2, 3], 5
    ti2, to2 = [2], 1

    print(minimumTime(ti1, to1))
    print(minimumTime(ti2, to2))
