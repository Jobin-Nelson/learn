"""
Created Date: 2023-12-27
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
    - use stack or two pointer approach
"""
def minCost(colors: str, neededTime: list[int]) -> int:
    # two pointer approach
    l = res = 0
    for r in range(1, len(colors)):
        if colors[l] == colors[r]:
           if neededTime[l] < neededTime[r]:
                res += neededTime[l]
                l = r
           else:
                res += neededTime[r]
        else:
            l = r
    return res

    # stack approach
    # stack = []
    # res = 0
    # for c, t in zip(colors, neededTime):
    #     if stack and c == stack[-1][0]:
    #         if t < stack[-1][1]:
    #             res += t
    #         else:
    #             res += stack.pop()[1]
    #     else:
    #         stack.append((c, t))
    # return res

if __name__ == '__main__':
    c1, n1 = "abaac", [1,2,3,4,5]
    c2, n2 = "abc", [1,2,3]
    c3, n3 = "aabaa", [1,2,3,4,1]

    print(minCost(c1, n1))
    print(minCost(c2, n2))
    print(minCost(c3, n3))
