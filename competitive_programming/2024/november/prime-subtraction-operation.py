"""
Created Date: 2024-11-11
Qn: You are given a 0-indexed integer array nums of length n.

    You can perform the following operation as many times as you want:

    Pick an index i that you haven’t picked before, and pick a prime p
    strictly less than nums[i], then subtract p from nums[i]. Return true
    if you can make nums a strictly increasing array using the above
    operation and false otherwise.

    A strictly increasing array is an array whose each element is strictly
    greater than its preceding element.
Link: https://leetcode.com/problems/prime-subtraction-operation/
Notes:
    - pre compute largest prime
"""

import unittest
import math


class Solution:
    def primeSubOperation(self, nums: list[int]) -> bool:
        def is_prime(n: int) -> bool:
            for i in range(2, int(math.sqrt(n))+1):
                if n % i == 0:
                    return False
            return True

        primes = [0] * max(nums)
        for n in range(2, max(nums)):
            if is_prime(n):
                primes[n] = n
            else:
                primes[n] = primes[n-1]

        prev = 0
        for n in nums:
            upper_bound = n - prev - 1
            largest_p = primes[upper_bound]
            cur = n - largest_p
            if cur <= prev:
                return False
            prev = cur
        return True





class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_primeSubOperation1(self):
        n = [4,9,6,10]
        self.assertEqual(self.sol.primeSubOperation(n), True)
    def test_primeSubOperation2(self):
        n = [6,8,11,12]
        self.assertEqual(self.sol.primeSubOperation(n), True)
    def test_primeSubOperation3(self):
        n = [5,8,3]
        self.assertEqual(self.sol.primeSubOperation(n), False)


if __name__ == '__main__':
    unittest.main()
