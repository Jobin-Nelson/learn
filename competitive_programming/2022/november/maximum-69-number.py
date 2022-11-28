'''
Created Date: 2022-11-07
Qn: You are given a positive integer num consisting only of digits 6 and 9.

    Return the maximum number you can get by changing at most one digit 
    (6 becomes 9, and 9 becomes 6).
Link: https://leetcode.com/problems/maximum-69-number/
Notes:
    - replace once 6 -> 9
'''
def maximum69Number(num: int) -> int:
    return int(str(num).replace('6', '9', 1))

if __name__ == '__main__':
    n1 = 9669
    n2 = 9996
    n3 = 9999

    print(maximum69Number(n1))
    print(maximum69Number(n2))
    print(maximum69Number(n3))

