'''
Created Date: 2023-07-20
Qn: We are given an array asteroids of integers representing asteroids in a
    row.

    For each asteroid, the absolute value represents its size, and the sign
    represents its direction (positive meaning right, negative meaning left).
    Each asteroid moves at the same speed.

    Find out the state of the asteroids after all collisions. If two asteroids
    meet, the smaller one will explode. If both are the same size, both will
    explode. Two asteroids moving in the same direction will never meet.
Link: https://leetcode.com/problems/asteroid-collision/
Notes:
    - use stack
'''
def asteroidCollision(asteroids: list[int]) -> list[int]:
    stack = []
    for a in asteroids:
        flag = True
        while stack and stack[-1] > 0 and a < 0:
            if abs(stack[-1]) < abs(a):
                stack.pop()
                continue
            elif abs(stack[-1]) == abs(a):
                stack.pop() 
            flag = False
            break
        if flag: stack.append(a)
    return stack

if __name__ == '__main__':
    a1 = [5,10,-5]
    a2 = [8,-8]
    a3 = [10,2,-5]

    print(asteroidCollision(a1))
    print(asteroidCollision(a2))
    print(asteroidCollision(a3))
