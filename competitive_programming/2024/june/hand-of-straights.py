"""
Created Date: 2024-06-06
Qn: Alice has some number of cards and she wants to rearrange the cards into
    groups so that each group is of size groupSize, and consists of groupSize
    consecutive cards.

    Given an integer array hand where hand[i] is the value written on the ith
    card and an integer groupSize, return true if she can rearrange the cards,
    or false otherwise.
Link: https://leetcode.com/problems/hand-of-straights/
Notes:
    - use hashmap
"""
from collections import Counter

def isNStraightHand(hand: list[int], groupSize: int) -> bool:
    if len(hand) % groupSize != 0:
        return False
    count = Counter(hand)
    for card in hand:
        start_card = card
        while count[start_card - 1] > 0:
            start_card -= 1
        while start_card <= card:
            while count[start_card] > 0:
                for next_card in range(start_card, start_card + groupSize):
                    if count[next_card] == 0: return False
                    count[next_card] -= 1
            start_card += 1
    return True

if __name__ == '__main__':
    h1, g1 = [1,2,3,6,2,3,4,7,8], 3
    h2, g2 = [1,2,3,4,5], 4

    print(isNStraightHand(h1, g1))
    print(isNStraightHand(h2, g2))
