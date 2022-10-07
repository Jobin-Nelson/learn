'''
Created Date: 2022-10-03
Qn: Alice has n balloons arranged on a rope. You are given a 0-indexed string
    colors where colors[i] is the color of the ith balloon.

    Alice wants the rope to be colorful. She does not want two consecutive
    balloons to be of the same color, so she asks Bob for help. Bob can remove
    some balloons from the rope to make it colorful. You are given a 0-indexed
    integer array neededTime where neededTime[i] is the time (in seconds) that
    Bob needs to remove the ith balloon from the rope.

    Return the minimum time Bob needs to make the rope colorful.
Link: https://leetcode.com/problems/minimum-time-to-make-rope-colorful/
Notes:
'''
def minCost(colors: str, neededTime: list[int]) -> int:
    if len(colors) == 1: return 0
    res = 0
    prev_time = neededTime[0]

    for i in range(1, len(colors)):
        if colors[i] == colors[i-1]:
            if prev_time < neededTime[i]:
                res += prev_time
                prev_time = neededTime[i]
            else:
                res += neededTime[i]
        else:
            prev_time = neededTime[i]
    return res


if __name__ == '__main__':
    c1, n1 = "abaac", [1, 2, 3, 4, 5]
    c2, n2 = "abc", [1, 2, 3]
    c3, n3 = "aabaa", [1, 2, 3, 4, 1]

    print(minCost(c1, n1))
    print(minCost(c2, n2))
    print(minCost(c3, n3))
