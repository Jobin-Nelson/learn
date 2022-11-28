'''
Created Date: 2022-10-21
Qn: Given an integer array nums and an integer k, return true if there are two
    distinct indices i and j in the array such that nums[i] == nums[j] and
    abs(i - j) <= k.
Link: https://leetcode.com/problems/contains-duplicate-ii/
Notes:
    - can be done using hashmap or hashset
'''
def containsNearbyDuplicate(nums: list[int], k: int) -> bool:
    visited = set()

    for i, n in enumerate(nums):
        if n in visited: return True
        visited.add(n)
        if len(visited) > k: visited.remove(nums[i-k])
    return False

if __name__ == '__main__':
    n1, k1 = [1, 2, 3, 1], 3
    n2, k2 = [1, 0, 1, 1], 1
    n3, k3 = [1, 2, 3, 1, 2, 3], 2
    
    print(containsNearbyDuplicate(n1, k1))
    print(containsNearbyDuplicate(n2, k2))
    print(containsNearbyDuplicate(n3, k3))
