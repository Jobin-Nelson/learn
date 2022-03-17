'''
Qn: You are climbing a staircase. It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
Link: https://leetcode.com/problems/climbing-stairs/submissions/
Notes:
- fibonnaci with n steps by tracking only two variables
'''

def climb_stairs(n):
    one, two = 0, 1
    i = 0
    while i < n:
        tmp = one + two
        one = two
        two = tmp
        i += 1
    return two

if __name__ == '__main__':
    n1, n2 = 2, 3
    print(climb_stairs(n1))
    print(climb_stairs(n2))
