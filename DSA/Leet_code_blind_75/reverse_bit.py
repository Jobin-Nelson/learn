# bit operation to get only bit and inserting it in the reverse order
class Solution:
    def reverse_bits(self, n: int)-> int:
        res = 0

        for i in range(32):
            bit = (n >> i) & 1
            res = res | (bit << (31 -i))
        return res
