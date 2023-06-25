'''
Created Date: 2023-06-19
Qn: There is a biker going on a road trip. The road trip consists of n + 1
    points at different altitudes. The biker starts his trip on point 0 with
    altitude equal 0.

    You are given an integer array gain of length n where gain[i] is the net
    gain in altitude between points i and i + 1 for all (0 <= i < n). Return
    the highest altitude of a point.
Link: https://leetcode.com/problems/find-the-highest-altitude/
Notes:
'''
def largestAltitude(gain: list[int]) -> int:
    max_altitude = cur_altitude = 0
    
    for g in gain:
        cur_altitude += g
        max_altitude = max(max_altitude, cur_altitude)

    return max_altitude

if __name__ == '__main__':
    g1 = [-5,1,5,0,-7]
    g2 = [-4,-3,-2,-1,4,3,2]

    print(largestAltitude(g1))
    print(largestAltitude(g2))
