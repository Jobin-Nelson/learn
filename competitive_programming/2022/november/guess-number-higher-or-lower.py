'''
Created Date: 2022-11-16
Qn: We are playing the Guess Game. The game is as follows:

    I pick a number from 1 to n. You have to guess which number I picked.

    Every time you guess wrong, I will tell you whether the number I picked is
    higher or lower than your guess.

    You call a pre-defined API int guess(int num), which returns three possible
    results:

        - -1: Your guess is higher than the number I picked (i.e. num > pick).
        - 1: Your guess is lower than the number I picked (i.e. num < pick).
        - 0: your guess is equal to the number I picked (i.e. num == pick).

    Return the number that I picked.
Link: https://leetcode.com/problems/guess-number-higher-or-lower/
Notes:
    - binary search
'''
class Guess:
    def __init__(self, pick: int):
        self.picked = pick

    def guess(self, num: int) -> int:
        if self.picked < num: 
            return -1
        elif self.picked > num:
            return 1
        else:
            return 0

    def guessNumber(self, n: int) -> int:
        l, r = 1, n

        while l+1 < r:
            m = (r + l) // 2
            res = self.guess(m)
            if res >= 0:
                l = m 
            else:
                r = m
        return l

if __name__ == '__main__':
    n1 = 10
    n2 = 1
    n3 = 1

    print(Guess(6).guessNumber(n1))
    print(Guess(1).guessNumber(n2))
    print(Guess(1).guessNumber(n3))
