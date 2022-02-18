'''
Qn: Given two integers a and b, return the sum of the two integers without using the operators + and -
Link: https://leetcode.com/problems/sum-of-two-integers/
Notes:
- use xor for adding and & for carrying over values till there is nothing to carry over
'''

def get_sum(a, b):
    while (b != 0):
        tmp = (a & b) << 1 
        a = a ^ b
        b = tmp
    return a

if __name__ == '__main__':
    a1, b1 = 1, 2
    a2, b2 = 2, 3
    print(get_sum(a1, b1))
    print(get_sum(a2, b2))
