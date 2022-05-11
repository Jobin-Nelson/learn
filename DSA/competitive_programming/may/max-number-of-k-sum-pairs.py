'''
Qn: You are given an integer array nums and an integer k.
    In one operation, you can pick two numbers from the array whose sum 
    equals k and remove them from the array.
    Return the maximum number of operations you can perform on the array.
Link: https://leetcode.com/problems/max-number-of-k-sum-pairs/
Notes:
- modded two sum 
'''
def max_operations(nums: list[int], k: int) -> int:
    hashmap = dict()
    res = 0
    for n in nums:
        complement = k - n
        if complement in hashmap and hashmap[complement] > 0:
            hashmap[complement] -= 1
            res += 1
        else:
            hashmap[n] = 1 + hashmap.get(n, 0)
    return res

if __name__ == '__main__':
    n1, k1 = [1, 2, 3, 4], 5
    n2, k2 = [3, 1, 3, 4, 3], 6
    print(max_operations(n1, k1))
    print(max_operations(n2, k2))
