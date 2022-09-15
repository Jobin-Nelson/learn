'''
Qn: Given an integer num, return the number of steps to reduce it to zero.
    In one step, if the current number is even, you have to divide it by 2, 
    otherwise, you have to subtract 1 from it.
Link: https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/
Notes:
    - iterate and divide by 2 when even subtract 1 when odd
'''
def numberOfSteps(num: int) -> int:
    #res = 0
    #while num:
        #if num % 2:
            #num -= 1
        #else:
            #num //= 2
        #res += 1
    #return res
    return len(bin(num)[2:]) + bin(num).count('1') - 1


if __name__ == '__main__':
    n1, n2, n3 = 14, 8, 123
    print(numberOfSteps(n1))
    print(numberOfSteps(n2))
    print(numberOfSteps(n3))
