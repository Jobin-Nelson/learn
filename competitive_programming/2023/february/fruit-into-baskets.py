'''
Created Date: 2023-02-07
Qn: You are visiting a farm that has a single row of fruit trees arranged from
    left to right. The trees are represented by an integer array fruits where
    fruits[i] is the type of fruit the ith tree produces.

    You want to collect as much fruit as possible. However, the owner has some
    strict rules that you must follow:

        - You only have two baskets, and each basket can only hold a single
          type of fruit. There is no limit on the amount of fruit each basket
          can hold.
        - Starting from any tree of your choice, you must pick exactly one
          fruit from every tree (including the start tree) while moving to the
          right. The picked fruits must fit in one of your baskets. 
        - Once you reach a tree with fruit that cannot fit in your baskets, you
          must stop. 

    Given the integer array fruits, return the maximum number of fruits you can
    pick.
Link: https://leetcode.com/problems/fruit-into-baskets/
Notes:
    - use sliding window
    - hashmap to store the counts of each type of fruits
    - remove fruits from left as len increases more than 2
'''
def totalFruit(fruits: list[int]) -> int:
    basket = {}
    max_picked = 0
    l = 0

    for r in range(len(fruits)):
        basket[fruits[r]] = basket.get(fruits[r], 0) + 1
        while len(basket) > 2:
            basket[fruits[l]] -= 1
            if basket[fruits[l]] == 0: del basket[fruits[l]]
            l += 1
        max_picked = max(max_picked, r - l + 1)
    return max_picked

if __name__ == '__main__':
    f1 = [1, 2, 1]
    f2 = [0, 1, 2, 2]
    f3 = [1, 2, 3, 2, 2]

    print(totalFruit(f1))
    print(totalFruit(f2))
    print(totalFruit(f3))
