'''
Qn: You are climbing a staircase. It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
Link: https://leetcode.com/problems/climbing-stairs/submissions/
Notes:
- fibonnaci with n+1 steps by tracking only two variables
'''

def climb_stairs(n):
    one, two = 1, 1
    i = 0
    while i < n-1:
        temp = one
        one += two
        two = temp
        i += 1
    return one

if __name__ == '__main__':
    n1, n2 = 2, 3
    print(climb_stairs(n1))
    print(climb_stairs(n2))
