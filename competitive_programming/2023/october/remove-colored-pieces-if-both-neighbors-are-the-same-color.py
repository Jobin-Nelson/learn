'''
Created Date: 2023-10-02
Qn: There are n pieces arranged in a line, and each piece is colored either by
    'A' or by 'B'. You are given a string colors of length n where colors[i] is
    the color of the ith piece.

    Alice and Bob are playing a game where they take alternating turns removing
    pieces from the line. In this game, Alice moves first.

        - Alice is only allowed to remove a piece colored 'A' if both its
          neighbors are also colored 'A'. 
        - She is not allowed to remove pieces that are colored 'B'. 
        - Bob is only allowed to remove a piece colored 'B' if both its
          neighbors are also colored 'B'. 
        - He is not allowed to remove pieces that are colored 'A'. 
        - Alice and Bob cannot remove pieces from the edge of the line. 
        - If a player cannot make a move on their turn, that player loses and
          the other player wins.

    Assuming Alice and Bob play optimally, return true if Alice wins, or return
    false if Bob wins.
Link: https://leetcode.com/problems/remove-colored-pieces-if-both-neighbors-are-the-same-color/
Notes:
'''
def winnerOfGame(colors: str) -> bool:
    alice, bob = 0, 0
    a = b = 0
    prev_a = prev_b = 0
    for c in colors:
        if c == 'A':
            a += 1
            prev_b = b = 0
        elif c == 'B':
            b += 1
            prev_a = a = 0
        if a > 2 and a > prev_a:
            alice += 1
            prev_a = a
        if b > 2 and b > prev_b:
            bob += 1
            prev_b = b
    return alice > bob

if __name__ == '__main__':
    c1 = "AAABABB"
    c2 = "AA"
    c3 = "ABBBBBBBAAA"

    print(winnerOfGame(c1))
    print(winnerOfGame(c2))
    print(winnerOfGame(c3))
