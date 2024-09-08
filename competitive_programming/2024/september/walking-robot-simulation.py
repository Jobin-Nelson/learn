"""
Created Date: 2024-09-04
Qn: A robot on an infinite XY-plane starts at point (0, 0) facing north. The
  robot can receive a sequence of these three possible types of commands:

  - -2: Turn left 90 degrees.
  - -1: Turn right 90 degrees.
  - 1 <= k <= 9: Move forward k units, one unit at a time.

  Some of the grid squares are obstacles. The ith obstacle is at grid point
  obstacles[i] = (xi, yi). If the robot runs into an obstacle, then it will
  instead stay in its current location and move on to the next command.

  Return the maximum Euclidean distance that the robot ever gets from the
  origin squared (i.e. if the distance is 5, return 25).

  Note:

    - North means +Y direction.
    - East means +X direction.
    - South means -Y direction.
    - West means -X direction.
    - There can be obstacle in [0,0].
Link: https://leetcode.com/problems/walking-robot-simulation/
Notes:
    - use simulation, hashing function
"""


def robotSim(commands: list[int], obstacles: list[list[int]]) -> int:
    def hash_coordinates(x: int, y: int) -> int:
        return x + 60001 * y

    obstacles_set = set(hash_coordinates(x, y) for (x, y) in obstacles)
    x, y = 0, 0
    cur_direction = 0
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    res = 0
    for command in commands:
        if command == -2:
            cur_direction = (cur_direction + 3) % 4
            continue
        elif command == -1:
            cur_direction = (cur_direction + 1) % 4
            continue
        dx, dy = directions[cur_direction]
        for _ in range(command):
            if hash_coordinates(x + dx, y + dy) not in obstacles_set:
                x += dx
                y += dy
        res = max(res, x * x + y * y)
    return res


if __name__ == '__main__':
    c1, o1 = [4, -1, 3], []
    c2, o2 = [4, -1, 4, -2, 4], [[2, 4]]
    c3, o3 = [6, -1, -1, 6], []
    c4, o4 = [6,-1,-1,6], []

    print(robotSim(c1, o1))
    print(robotSim(c2, o2))
    print(robotSim(c3, o3))
    print(robotSim(c4, o4))
