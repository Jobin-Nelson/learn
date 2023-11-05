'''
Created Date: 2023-11-04
Qn: We have a wooden plank of the length n units. Some ants are walking on the
    plank, each ant moves with a speed of 1 unit per second. Some of the ants
    move to the left, the other move to the right.

    When two ants moving in two different directions meet at some point, they
    change their directions and continue moving again. Assume changing
    directions does not take any additional time.

    When an ant reaches one end of the plank at a time t, it falls out of the
    plank immediately.

    Given an integer n and two integer arrays left and right, the positions of
    the ants moving to the left and the right, return the moment when the last
    ant(s) fall out of the plank.
Link: https://leetcode.com/problems/last-moment-before-all-ants-fall-out-of-a-plank/
Notes:
    - the collisions are irrelevant
'''
def getLastMoment(n: int, left: list[int], right: list[int]) -> int:
    return max(max(left or [0]), n-min(right or [n]))

if __name__ == '__main__':
    n1, l1, r1 = 4, [4, 3], [0, 1]
    n2, l2, r2 = 7, [], [0, 1, 2, 3, 4, 5, 6, 7]
    n3, l3, r3 = 7, [0, 1, 2, 3, 4, 5, 6, 7], []

    print(getLastMoment(n1, l1, r1))
    print(getLastMoment(n2, l2, r2))
    print(getLastMoment(n3, l3, r3))
