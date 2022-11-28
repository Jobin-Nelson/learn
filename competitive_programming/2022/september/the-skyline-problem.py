'''
Created Date: 2022-09-30
Qn: A city's skyline is the outer contour of the silhouette formed by all the
    buildings in that city when viewed from a distance. Given the locations and
    heights of all the buildings, return the skyline formed by these buildings
    collectively.

    The geometric information of each building is given in the array buildings
    where buildings[i] = [lefti, righti, heighti]:

    - lefti is the x coordinate of the left edge of the ith building. 
    - righti is the x coordinate of the right edge of the ith building. 
    - heighti is the height of the ith building. 

    You may assume all buildings are perfect rectangles grounded on an
    absolutely flat surface at height 0.

    The skyline should be represented as a list of "key points" sorted by their
    x-coordinate in the form [[x1,y1],[x2,y2],...]. Each key point is the left
    endpoint of some horizontal segment in the skyline except the last point in
    the list, which always has a y-coordinate 0 and is used to mark the
    skyline's termination where the rightmost building ends. Any ground between
    the leftmost and rightmost buildings should be part of the skyline's
    contour.

    Note: There must be no consecutive horizontal lines of equal height in the
    output skyline. For instance, [...,[2 3],[4 5],[7 5],[11 5],[12 7],...] is
    not acceptable; the three lines of height 5 should be merged into one in
    the final output as such: [...,[2 3],[4 5],[12 7],...]
Link: https://leetcode.com/problems/the-skyline-problem/
Notes:
    - store start and end of buildings in an event list
    - use sortedlist to store the active heights
    - add heights on start and remove them at end
    - append to res whenever there is a change from the last height
'''
from sortedcontainers import SortedList

def getSkyline(buildings: list[list[int]]) -> list[list[int]]:
    events = []

    for l, r, h in buildings:
        events.append((l, h, 0))
        events.append((r, h, 1))

    events.sort()

    res = []
    active_heights = SortedList([0])
    i, n = 0, len(events)

    while i < n:
        cur_x = events[i][0]
        while i < n and events[i][0] == cur_x:
            _, h, t = events[i]
            if t == 0:
                active_heights.add(h)
            else:
                active_heights.remove(h)
            i += 1
        if not res or res[-1][1] != active_heights[-1]:
            res.append((cur_x, active_heights[-1]))
    return res

if __name__ == '__main__':
    b1 = [[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]
    b2 = [[0,2,3],[2,5,3]]

    print(getSkyline(b1))
    print(getSkyline(b2))
