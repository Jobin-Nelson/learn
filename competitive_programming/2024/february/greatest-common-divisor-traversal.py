"""
Created Date: 2024-02-25
Qn: You are given a 0-indexed integer array nums, and you are allowed to
    traverse between its indices. You can traverse between index i and index j,
    i != j, if and only if gcd(nums[i], nums[j]) > 1, where gcd is the greatest
    common divisor.

    Your task is to determine if for every pair of indices i and j in nums,
    where i < j, there exists a sequence of traversals that can take us from i
    to j.

    Return true if it is possible to traverse between all such pairs of
    indices, or false otherwise.
Link: https://leetcode.com/problems/greatest-common-divisor-traversal/
Notes:
    - use union find to find the number of connected component
    - return true if there is only one connected component
"""
class UnionFind:
    def __init__(self, n: int):
        self.parents = list(range(n))
        self.rank = [1] * n
        self.components = n

    def find(self, x: int):
        while self.parents[x] != x:
            self.parents[x] = self.parents[self.parents[x]]
            x = self.parents[x]
        return self.parents[x]
    def union(self, x: int, y: int):
        px, py = self.find(x), self.find(y)
        if px == py: return
        if self.rank[px] < self.rank[py]: px, py = py, px
        self.parents[py] = px
        self.rank[px] += self.rank[py]
        self.components -= 1

def canTravereAllPairs(nums: list[int]) -> bool:
    uf = UnionFind(len(nums))

    factor_index = {}
    for i, n in enumerate(nums):
        f = 2
        while f * f <= n:
            if n % f == 0:
                if f in factor_index:
                    uf.union(i, factor_index[f])
                else:
                    factor_index[f] = i
                while n % f == 0:
                    n = n // f
            f+=1
        if n > 1:
            if n in factor_index:
                uf.union(i, factor_index[n])
            else:
                factor_index[n] = i
    return uf.components == 1

if __name__ == '__main__':
    n1 = [2,3,6]
    n2 = [3,9,5]
    n3 = [4,3,12,8]

    print(canTravereAllPairs(n1))
    print(canTravereAllPairs(n2))
    print(canTravereAllPairs(n3))
