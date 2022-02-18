'''
Qn: Write a function that takes an unsigned integer and returns the number of '1' bits it has aka hamming weight
Link: https://leetcode.com/problems/number-of-1-bits/
Notes:
- modding with 2 to get the last binary digit and bit shifting towards left by 1 each time
- anding both n and n-1 till n reaches 0 the number of iteration gives the number of 1 bits
'''
# Bit shifting and modding with 2
def hamming_weight(num: int)-> int:
    n = int(num, 2)
# first way - goes through each bit
    # res = 0 
    # while n:
        # res += n%2
        # n = n >> 1
    # return res

# second way - doesn't need to go through the entire number
    res = 0 
    while n:
        n &= (n-1)
        res += 1 
    return res

if __name__ == '__main__':
    num1 = '00000000000000000000000000001011'
    num2 = '00000000000000000000000010000000'
    num3 = '11111111111111111111111111111101'
    print(hamming_weight(num1))
    print(hamming_weight(num2))
    print(hamming_weight(num3))
