'''
Created Date: 2023-11-24
Qn: There are 3n piles of coins of varying size, you and your friends will take
    piles of coins as follows:

        - In each step, you will choose any 3 piles of coins (not necessarily
          consecutive). 
        - Of your choice, Alice will pick the pile with the maximum number of
          coins. 
        - You will pick the next pile with the maximum number of coins. 
        - Your friend Bob will pick the last pile. Repeat until there are no
          more piles of coins.

    Given an array of integers piles where piles[i] is the number of coins in
    the ith pile.

    Return the maximum number of coins that you can have.
Link: https://leetcode.com/problems/maximum-number-of-coins-you-can-get/
Notes:
    - sorted get 2/3 rd for the piles and get sum of alternate element
'''
def maxCoins(piles: list[int]) -> int:
    return sum(sorted(piles)[len(piles)//3::2])

if __name__ == '__main__':
    p1 = [2,4,1,2,7,8]
    p2 = [2,4,5]
    p3 = [9,8,7,6,5,1,2,3,4]

    print(maxCoins(p1))
    print(maxCoins(p2))
    print(maxCoins(p3))
