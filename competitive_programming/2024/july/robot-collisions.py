"""
Created Date: 2024-07-13
Qn: There are n 1-indexed robots, each having a position on a line, health, and
    movement direction.

    You are given 0-indexed integer arrays positions, healths, and a string
    directions (directions[i] is either 'L' for left or 'R' for right). All
    integers in positions are unique.

    All robots start moving on the line simultaneously at the same speed in
    their given directions. If two robots ever share the same position while
    moving, they will collide.

    If two robots collide, the robot with lower health is removed from the
    line, and the health of the other robot decreases by one. The surviving
    robot continues in the same direction it was going. If both robots have the
    same health, they are both removed from the line.

    Your task is to determine the health of the robots that survive the
    collisions, in the same order that the robots were given, i.e. final heath
    of robot 1 (if survived), final health of robot 2 (if survived), and so on.
    If there are no survivors, return an empty array.

    Return an array containing the health of the remaining robots (in the order
    they were given in the input), after no further collisions can occur.

    Note: The positions may be unsorted.
Link: https://leetcode.com/problems/robot-collisions/
Notes:
    - use stack
"""
def survivedRobotsHealths(positions: list[int], healths: list[int], directions: str) -> list[int]:
    rights = []
    indices = sorted(range(len(positions)), key=lambda i: positions[i])
    for i in indices:
        if directions[i] == 'R':
            rights.append(i)
        else:
            while rights and healths[i] > 0:
                oi = rights.pop()
                if healths[oi] > healths[i]:
                    healths[i] = 0
                    healths[oi] -= 1
                    rights.append(oi)
                elif healths[oi] < healths[i]:
                    healths[i] -= 1
                    healths[oi] = 0
                else:
                    healths[i] = 0
                    healths[oi] = 0
    return list(filter(lambda x: x, healths))

if __name__ == '__main__':
    p1, h1, d1 = [5,4,3,2,1], [2,17,9,15,10], "RRRRR"
    p2, h2, d2 = [3,5,2,6], [10,10,15,12], "RLRL"
    p3, h3, d3 = [1,2,5,6], [10,10,11,11], "RLRL"
    p4, h4, d4 = [13,3], [17,2], "LR"

    print(survivedRobotsHealths(p1, h1, d1))
    print(survivedRobotsHealths(p2, h2, d2))
    print(survivedRobotsHealths(p3, h3, d3))
    print(survivedRobotsHealths(p4, h4, d4))
