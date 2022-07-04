'''
Created Date: 27-06-2022
Qn: A decimal number is called deci-binary if each of its digits is either 
    0 or 1 without any leading zeros. For example, 101 and 1100 are deci-binary, 
    while 112 and 3001 are not.
    Given a string n that represents a positive decimal integer, return the 
    minimum number of positive deci-binary numbers needed so that they sum up to n.
Link: https://leetcode.com/problems/partitioning-into-minimum-number-of-deci-binary-numbers/
Notes:
- Answer is always the maximum digit in the number
'''
def minPartitions(n: str) -> int:
    return max(int(c) for c in n)

if __name__ == '__main__':
    n1, n2, n3 = '32', '82734', '27346209830709182346'
    print(minPartitions(n1))
    print(minPartitions(n2))
    print(minPartitions(n3))
