"""
Created Date: 2024-06-20
Qn: In the universe Earth C-137, Rick discovered a special form of magnetic
    force between two balls if they are put in his new invented basket. Rick
    has n empty baskets, the ith basket is at position[i], Morty has m balls
    and needs to distribute the balls into the baskets such that the minimum
    magnetic force between any two balls is maximum.

    Rick stated that magnetic force between two different balls at positions x
    and y is |x - y|.

    Given the integer array position and the integer m. Return the required
    force.
Link: https://leetcode.com/problems/magnetic-force-between-two-balls/
Notes:
    - use binary search
"""
def maxDistance(position: list[int], m: int) -> int:
    position.sort()
    def can_place_balls(x: int) -> bool:
        prev_ball_pos = position[0]
        balls_placed = 1

        for i in range(1, len(position)):
            cur_pos = position[i]
            if cur_pos - prev_ball_pos >= x:
                prev_ball_pos = cur_pos
                balls_placed += 1
                if balls_placed == m:
                    return True
        return False

    l, r = 0, int(position[-1] / (m-1)) + 1
    res = 0
    while l <= r:
        dist = l + ((r-l)>>1)
        if can_place_balls(dist):
            res = dist
            l = dist + 1
        else:
            r = dist - 1
    return res


if __name__ == '__main__':
    p1, m1 = [1,2,3,4,7], 3
    p2, m2 = [5,4,3,2,1,1000000000], 2

    print(maxDistance(p1, m1))
    print(maxDistance(p2, m2))
