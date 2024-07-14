"""
Created Date: 2024-07-08
Qn: There are n friends that are playing a game. The friends are sitting in a
    circle and are numbered from 1 to n in clockwise order. More formally,
    moving clockwise from the ith friend brings you to the (i+1)th friend for 1
    <= i < n, and moving clockwise from the nth friend brings you to the 1st
    friend.

    The rules of the game are as follows:

        - Start at the 1st friend. 
        - Count the next k friends in the clockwise direction including the
          friend you started at. 
        - The counting wraps around the circle and may count some friends more
          than once. 
        - The last friend you counted leaves the circle and loses the game. 
        - If there is still more than one friend in the circle, go back to step
          2 starting from the friend immediately clockwise of the friend who
          just lost and repeat. 
        - Else, the last friend in the circle wins the game. 

    Given the number of friends, n, and an integer k, return the winner of the
    game.

Link: https://leetcode.com/problems/find-the-winner-of-the-circular-game/
Notes:
    - use simulation or recursion or iterative
"""
from collections import deque

def findTheWinner(n: int, k: int) -> int:
    circle = deque(range(1,n+1))
    while len(circle) > 1:
        for _ in range(k-1):
            circle.append(circle.popleft())
        circle.popleft()
    return circle[0]

    # Iterative approach
    # res = 0
    # for i in range(2, n+1):
    #     res = (res + k) % i
    # return res + 1

if __name__ == '__main__':
    n1, k1 = 5, 2
    n2, k2 = 6, 5

    print(findTheWinner(n1, k1))
    print(findTheWinner(n2, k2))
