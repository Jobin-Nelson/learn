"""
Created Date: 2024-04-10
Qn: You are given an integer array deck. There is a deck of cards where every
    card has a unique integer. The integer on the ith card is deck[i].

    You can order the deck in any order you want. Initially, all the cards
    start face down (unrevealed) in one deck.

    You will do the following steps repeatedly until all cards are revealed:

        - Take the top card of the deck, reveal it, and take it out of the
          deck.
        - If there are still cards in the deck then put the next top card of
          the deck at the bottom of the deck. 
        - If there are still unrevealed cards, go back to step 1. Otherwise,
          stop.

    Return an ordering of the deck that would reveal the cards in increasing
    order.

    Note that the first entry in the answer is considered to be the top of the
    deck.
Link: https://leetcode.com/problems/reveal-cards-in-increasing-order/
Notes:
    - queue the index and simulate the condition on indices
"""
from collections import deque
def deckRevealedIncreasing(deck: list[int]) -> list[int]:
    deck.sort()
    res = [0] * len(deck)
    q = deque(range(len(deck)))
    for n in deck:
        i = q.popleft()
        res[i] = n
        if q: q.append(q.popleft())
    return res

if __name__ == '__main__':
    d1 = [17,13,11,2,3,5,7]
    d2 = [1,1000]

    print(deckRevealedIncreasing(d1))
    print(deckRevealedIncreasing(d2))
