'''
Created Date: 2022-09-03
Qn: Return all non-negative integers of length n such that the absolute
    difference between every two consecutive digits is k.

    Note that every number in the answer must not have leading zeros. For example,
    01 has one leading zero and is invalid.

    You may return the answer in any order.
Link: https://leetcode.com/problems/numbers-with-same-consecutive-differences/
Notes: 
- iterate through the 0 -> 9
- attach a digit that is +k, -k if it is a single digit(0 - 9) and 
- if the original digit is not zero
- store them in a set to remove duplicates
'''
def numsSameConsecDiff(n: int, k: int) -> list[int]:
    temp = range(10)

    for _ in range(n-1):
        temp = {x*10+y for x in temp for y in [x%10+k, x%10-k] if x and 0<=y<10}
    return list(temp)

if __name__ == '__main__':
    n1, k1 = 3, 7
    n2, k2 = 2, 1

    print(numsSameConsecDiff(n1, k1))
    print(numsSameConsecDiff(n2, k2))
