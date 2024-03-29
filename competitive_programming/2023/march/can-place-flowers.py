'''
Created Date: 2023-03-20
Qn: You have a long flowerbed in which some of the plots are planted, and some
    are not. However, flowers cannot be planted in adjacent plots.

    Given an integer array flowerbed containing 0's and 1's, where 0 means
    empty and 1 means not empty, and an integer n, return if n new flowers can
    be planted in the flowerbed without violating the no-adjacent-flowers rule.
Link: https://leetcode.com/problems/can-place-flowers/
Notes:
    - modify the list in place once n == 0 return True
'''
def canPlaceFlowers(flowerbed: list[int], n: int) -> bool:
    N = len(flowerbed)
    if N == 0 or n == 0: return True
    for i in range(N):
        if flowerbed[i] == 0 and (i==0 or flowerbed[i-1]==0) and (i==N-1 or flowerbed[i+1]==0):
            flowerbed[i] = 1
            n -= 1
        if n == 0: return True
    return False

if __name__ == '__main__':
    f1, n1 = [1,0,0,0,1], 1
    f2, n2 = [1,0,0,0,1], 2
    f3, n3 = [0,0,1,0,0], 1
    f4, n4 = [0,0,0,0,0,1,0,0], 0

    print(canPlaceFlowers(f1, n1))
    print(canPlaceFlowers(f2, n2))
    print(canPlaceFlowers(f3, n3))
    print(canPlaceFlowers(f4, n4))
