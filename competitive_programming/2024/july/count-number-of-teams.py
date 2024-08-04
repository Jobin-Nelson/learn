"""
Created Date: 2024-07-29
Qn: There are n soldiers standing in a line. Each soldier is assigned a unique
    rating value.

    You have to form a team of 3 soldiers amongst them under the following
    rules:

    - Choose 3 soldiers with index (i, j, k) with rating (rating[i], rating[j],
      rating[k]). 
    - A team is valid if: (rating[i] < rating[j] < rating[k]) or (rating[i] >
      rating[j] > rating[k]) where (0 <= i < j < k < n). 

    Return the number of teams you can form given the conditions. (soldiers can
    be part of multiple teams).
Link: https://leetcode.com/problems/count-number-of-teams/
Notes:
    - start with middle element and go left and right
"""
def numTeams(rating: list[int]) -> int:
    res = 0
    for m in range(1, len(rating)-1):
        left_smaller = right_larger = 0
        for i in range(m):
            if rating[i] < rating[m]:
                left_smaller += 1
        for i in range(m+1, len(rating)):
            if rating[i] > rating[m]:
                right_larger += 1
        res += left_smaller * right_larger
        left_larger = m - left_smaller
        right_smaller = len(rating) - m - 1 - right_larger
        res += left_larger * right_smaller
    return res

if __name__ == '__main__':
    r1 = [2,5,3,4,1]
    r2 = [2,1,3]
    r3 = [1,2,3,4]

    print(numTeams(r1))
    print(numTeams(r2))
    print(numTeams(r3))
