'''
Created Date: 2023-04-17
Qn: There are n kids with candies. You are given an integer array candies,
    where each candies[i] represents the number of candies the ith kid has, and
    an integer extraCandies, denoting the number of extra candies that you
    have.

    Return a boolean array result of length n, where result[i] is true if,
    after giving the ith kid all the extraCandies, they will have the greatest
    number of candies among all the kids, or false otherwise.

    Note that multiple kids can have the greatest number of candies.
Link: https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/
Notes:
'''
def kidsWithCandies(candies: list[int], extraCandies: int) -> list[bool]:
    required_min_candy = max(candies) - extraCandies

    return [ candy >= required_min_candy for candy in candies ]

if __name__ == '__main__':
    c1, e1 = [2,3,5,1,3], 3
    c2, e2 = [4,2,1,1,2], 1
    c3, e3 = [12,1,12], 10

    print(kidsWithCandies(c1, e1))
    print(kidsWithCandies(c2, e2))
    print(kidsWithCandies(c3, e3))
