"""
Created Date: 2024-04-27
Qn: In the video game Fallout 4, the quest "Road to Freedom" requires players
    to reach a metal dial called the "Freedom Trail Ring" and use the dial to
    spell a specific keyword to open the door.

    Given a string ring that represents the code engraved on the outer ring and
    another string key that represents the keyword that needs to be spelled,
    return the minimum number of steps to spell all the characters in the
    keyword.

    Initially, the first character of the ring is aligned at the "12:00"
    direction. You should spell all the characters in key one by one by
    rotating ring clockwise or anticlockwise to make each character of the
    string key aligned at the "12:00" direction and then by pressing the center
    button.

    At the stage of rotating the ring to spell the key character key[i]:

        - You can rotate the ring clockwise or anticlockwise by one place,
          which counts as one step. The final purpose of the rotation is to
          align one of ring's characters at the "12:00" direction, where this
          character must equal key[i]. 
        - If the character key[i] has been aligned at the "12:00" direction,
          press the center button to spell, which also counts as one step.
          After the pressing, you could begin to spell the next character in
          the key (next stage). Otherwise, you have finished all the spelling.

Link: https://leetcode.com/problems/freedom-trail/
Notes:
    - use bottom up dynamic approach
"""
from sys import maxsize

def findRotateSteps(ring: str, key: str) -> int:
    N = len(ring)
    prev_dp = [0] * N

    for k in reversed(key):
        dp = [maxsize] * N
        for r in range(N):
            for i, c in enumerate(ring):
                if c == k:
                    min_dist = min(
                        abs(r - i),
                        N - abs(r - i)
                    )
                    dp[r] = min(
                        dp[r],
                        min_dist + 1 + prev_dp[i]
                    )
        prev_dp = dp
    return prev_dp[0]


if __name__ == '__main__':
    r1, k1 = "godding", "gd"
    r2, k2 = "godding", "godding"
    r3, k3 = "edcba", "abcde"

    print(findRotateSteps(r1, k1))
    print(findRotateSteps(r2, k2))
    print(findRotateSteps(r3, k3))
