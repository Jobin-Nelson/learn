'''
Created Date: 2023-09-13
Qn: here are n children standing in a line. Each child is assigned a rating
    value given in the integer array ratings.

    You are giving candies to these children subjected to the following
    requirements:

        Each child must have at least one candy. Children with a higher rating
        get more candies than their neighbors.

    Return the minimum number of candies you need to have to distribute the
    candies to the children.
Link: https://leetcode.com/problems/candy/
Notes:
    - iterate left to right, and right to left create a mountain where the
      peeks are at high ratings when compared to neighbors
'''
def candy(ratings: list[int]) -> int:
    N = len(ratings)
    l, r = [1] * N, [1] * N

    for i in range(1, N):
        if ratings[i] > ratings[i-1]:
            l[i] = l[i-1] + 1

    for i in range(N-2, -1, -1):
        if ratings[i] > ratings[i+1]:
            r[i] = r[i+1] + 1

    return sum(max(l[i], r[i]) for i in range(N))

if __name__ == '__main__':
    r1 = [1,0,2]
    r2 = [1,2,2]

    print(candy(r1))
    print(candy(r2))
