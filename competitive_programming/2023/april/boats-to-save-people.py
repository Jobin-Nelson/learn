'''
Created Date: 2023-04-03
Qn: You are given an array people where people[i] is the weight of the ith
    person, and an infinite number of boats where each boat can carry a maximum
    weight of limit. Each boat carries at most two people at the same time,
    provided the sum of the weight of those people is at most limit.

    Return the minimum number of boats to carry every given person.
Link: https://leetcode.com/problems/boats-to-save-people/
Notes:
    - use binary search
'''
def numRescueBoats(people: list[int], limit: int) -> int:
    people.sort()
    l, r = 0, len(people)-1
    boat = 0

    while l <= r:
        if people[l] + people[r] <= limit:
            l += 1
        r -= 1
        boat += 1
    return boat

if __name__ == '__main__':
    p1, l1 = [1,2], 3
    p2, l2 = [3,2,2,1], 3
    p3, l3 = [3,5,3,4], 5

    print(numRescueBoats(p1, l1))
    print(numRescueBoats(p2, l2))
    print(numRescueBoats(p3, l3))
