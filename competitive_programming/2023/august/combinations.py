'''
Created Date: 2023-08-01
Qn: Given two integers n and k, return all possible combinations of k numbers
    chosen from the range [1, n].

    You may return the answer in any order.
Link: https://leetcode.com/problems/combinations/
Notes:
    - use backtrack
'''
def combine(n: int, k: int) -> list[list[int]]:
    res = []
    def backtrack(start: int, comb: list[int]) -> None:
        if len(comb) == k:
            res.append(comb.copy())
            return
        for i in range(start, n+1):
            comb.append(i)
            backtrack(i+1, comb)
            comb.pop()
    backtrack(1, [])
    return res

    # return list(map(list, iterools.combinations(range(1, n+1), k)))


if __name__ == '__main__':
    n1, k1 = 4, 2
    n2, k2 = 1, 1

    print(combine(n1, k1))
    print(combine(n2, k2))
