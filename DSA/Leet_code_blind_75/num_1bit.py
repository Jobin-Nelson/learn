# Bit shifting and modding with 2
class Solution:
    def hamming_weight(self, n: int)-> int:
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