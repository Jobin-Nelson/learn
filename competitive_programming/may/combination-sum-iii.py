'''
Qn: Find all valid combinations of k numbers that sum up to n 
    such that the following conditions are true:
    Only numbers 1 through 9 are used.
    Each number is used at most once.
Link: https://leetcode.com/problems/combination-sum-iii/
Notes:
- recursively find the values
'''
def combinationSum(k: int, n: int) -> list[list[int]]:
    res = []

    def dfs(build, num, sum_so_far):
        if len(build) == k:
            if sum_so_far == n:
                res.append(build)
            return 
        for i in range(num, 10):
            if sum_so_far > n:
                break
            dfs(build+[i], i+1, sum_so_far+i)
    dfs([], 1, 0)
    return res

if __name__ == '__main__':
    k1, n1 = 3, 7
    k2, n2 = 3, 9
    k3, n3 = 4, 1
    print(combinationSum(k1, n1))
    print(combinationSum(k2, n2))
    print(combinationSum(k3, n3))
