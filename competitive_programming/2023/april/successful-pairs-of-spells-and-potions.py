'''
Created Date: 2023-04-02
Qn: You are given two positive integer arrays spells and potions, of length n
    and m respectively, where spells[i] represents the strength of the ith
    spell and potions[j] represents the strength of the jth potion.

    You are also given an integer success. A spell and potion pair is
    considered successful if the product of their strengths is at least
    success.

    Return an integer array pairs of length n where pairs[i] is the number of
    potions that will form a successful pair with the ith spell.
Link: https://leetcode.com/problems/successful-pairs-of-spells-and-potions/
Notes:
    - use binary search
    - sort potions and binary search to find the first the pair that is
      successful
'''
def successfulPairs(spells: list[int], potions: list[int], success: int) -> list[int]:
    N, M = len(spells), len(potions)
    res = [0] * N
    potions.sort()

    for i in range(N):
        l, r = 0, M - 1
        spell = spells[i]
        while l <= r:
            m = l + ((r-l) >> 1)
            product = spell * potions[m]
            if product >= success:
                r = m - 1
            else:
                l = m + 1
        res[i] = M - l

    return res

if __name__ == '__main__':
    sp1, p1, s1 = [5, 1, 3], [1, 2, 3, 4, 5], 7
    sp2, p2, s2 = [3, 1, 2], [8, 5, 8], 16

    print(successfulPairs(sp1, p1, s1))
    print(successfulPairs(sp2, p2, s2))
