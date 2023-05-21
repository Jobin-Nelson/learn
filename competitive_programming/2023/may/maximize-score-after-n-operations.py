'''
Created Date: 2023-05-14
Qn: You are given nums, an array of positive integers of size 2 * n. You must
    perform n operations on this array.

    In the ith operation (1-indexed), you will:

        - Choose two elements, x and y.
        - Receive a score of i * gcd(x, y).
        - Remove x and y from nums.

    Return the maximum score you can receive after performing n operations.

    The function gcd(x, y) is the greatest common divisor of x and y.
Link: https://leetcode.com/problems/maximize-score-after-n-operations/
Notes:
    - use recursive
'''
from collections import defaultdict
import math

def maxScore(nums:list[int]) -> int:
    cache = defaultdict(int)
    
    def dfs(mask: int, op: int) -> int:
        if mask in cache: return cache[mask]

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if (1<<i) & mask or (1<<j) & mask: continue
                
                new_mask = mask | (1<<i) | (1<<j)
                score = op * math.gcd(nums[i], nums[j])
                cache[mask] = max(cache[mask], score + dfs(new_mask, op+1))
        return cache[mask]
    return dfs(0, 1)
    # def gcd(x: int, y: int) -> int:
    #     while y:
    #         x, y = y, x % y
    #     return x

if __name__ == '__main__':
    n1 = [1, 2]
    n2 = [3, 4, 6, 8]
    n3 = [1, 2, 3, 4, 5, 6]

    print(maxScore(n1))
    print(maxScore(n2))
    print(maxScore(n3))
