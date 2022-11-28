'''
Created Date: 02-07-2022
Qn: You are given a rectangular cake of size h x w and two arrays of integers 
    horizontalCuts and verticalCuts where:
        - horizontalCuts[i] is the distance from the top of the rectangular cake 
        to the ith horizontal cut and similarly, and
        - verticalCuts[j] is the distance from the left of the rectangular cake 
        to the jth vertical cut.
    Return the maximum area of a piece of cake after you cut at each horizontal and 
    vertical position provided in the arrays horizontalCuts and verticalCuts. Since 
    the answer can be a large number, return this modulo 10^9 + 7.
Link: https://leetcode.com/problems/maximum-area-of-a-piece-of-cake-after-horizontal-and-vertical-cuts/
Notes:
    - sort find the max difference between the cuts including the boundaries
'''
def maxArea(h: int, w: int, horizontalCuts: list[int], verticalCuts: list[int]) -> int:
    horizontalCuts.sort()
    verticalCuts.sort()
    horizontalCuts = [0] + horizontalCuts + [h]
    verticalCuts = [0] + verticalCuts + [w]

    mh = mw = 0
    for i in range(1, len(horizontalCuts)):
        mh = max(mh, abs(horizontalCuts[i-1] - horizontalCuts[i]))
    for i in range(1, len(verticalCuts)):
        mw = max(mw, abs(verticalCuts[i-1] - verticalCuts[i]))
    return (mh * mw) % (10**9+7)

if __name__ == '__main__':
    h1, w1, hc1, vc1 = 5, 4, [1, 2, 4], [1, 3]
    h2, w2, hc2, vc2 = 5, 4, [3, 1], [1]
    h3, w3, hc3, vc3 = 5, 4, [3], [3]
    print(maxArea(h1, w1, hc1, vc1))
    print(maxArea(h2, w2, hc2, vc2))
    print(maxArea(h3, w3, hc3, vc3))
