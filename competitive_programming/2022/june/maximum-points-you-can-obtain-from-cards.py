'''
Created Date: 26-06-2022
Qn: There are several cards arranged in a row, and each card has an associated 
    number of points. The points are given in the integer array cardPoints.
    In one step, you can take one card from the beginning or from the end of the 
    row. You have to take exactly k cards. Your score is the sum of the points 
    of the cards you have taken.
    Given the integer array cardPoints and the integer k, return the maximum 
    score you can obtain.
Link: https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/
Notes:
    - sliding window to find the max sum of cards outside the window
'''
def maxScore(cardPoints: list[int], k: int) -> int:
    N = len(cardPoints)
    l, r = 0, N - k
    res = total = sum(cardPoints[r:])

    while r < N:
        total += cardPoints[l] - cardPoints[r]
        res = max(res, total)
        r += 1
        l += 1
    return res

if __name__ == '__main__':
    c1, k1 = [1,2,3,4,5,6,1], 3
    c2, k2 = [2,2,2], 2
    c3, k3 = [9,7,7,9,7,7,9], 7
    print(maxScore(c1, k1))
    print(maxScore(c2, k2))
    print(maxScore(c3, k3))
