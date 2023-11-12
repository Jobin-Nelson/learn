'''
Created Date: 2023-11-07
Qn: Can you solve this real interview question? Eliminate Maximum Number of
    Monsters - You are playing a video game where you are defending your city
    from a group of n monsters. You are given a 0-indexed integer array dist of
    size n, where dist[i] is the initial distance in kilometers of the ith
    monster from the city.

    The monsters walk toward the city at a constant speed. The speed of each
    monster is given to you in an integer array speed of size n, where speed[i]
    is the speed of the ith monster in kilometers per minute.

    You have a weapon that, once fully charged, can eliminate a single monster.
    However, the weapon takes one minute to charge. The weapon is fully charged
    at the very start.

    You lose when any monster reaches your city. If a monster reaches the city
    at the exact moment the weapon is fully charged, it counts as a loss, and
    the game ends before you can use your weapon.

    Return the maximum number of monsters that you can eliminate before you
    lose, or n if you can eliminate all the monsters before they reach the
    city.
Link: https://leetcode.com/problems/eliminate-maximum-number-of-monsters/
Notes:
    - calculate and sort by time = dist / speed
'''
def eliminateMaximum(dist: list[int], speed: list[int]) -> int:
    time = sorted(dist[i]/speed[i] for i in range(len(dist)))
    for t, tm in enumerate(time):
        if tm <= t: return t
    return len(dist)

if __name__ == '__main__':
    d1, s1 = [1,3,4], [1,1,1]
    d2, s2 = [1,1,2,3], [1,1,1,1]
    d3, s3 = [3,2,4], [5,3,2]
    d4, s4 = list(reversed([3,2,4])), list(reversed([5,3,2]))

    print(eliminateMaximum(d1, s1))
    print(eliminateMaximum(d2, s2))
    print(eliminateMaximum(d3, s3))
    print(eliminateMaximum(d4, s4))
