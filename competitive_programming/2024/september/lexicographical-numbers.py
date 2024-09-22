"""
Created Date: 2024-09-21
Qn: Given an integer n, return all the numbers in the range [1, n] sorted in
    lexicographical order.

    You must write an algorithm that runs in O(n) time and uses O(1) extra
    space. 
Link: https://leetcode.com/problems/lexicographical-numbers/
Notes:
    - use iterative or dfs
"""


def lexicalOrder(n: int) -> list[int]:
    # Iterative solution
    res = []
    cur = 1
    while len(res) < n:
        res.append(cur)
        if cur * 10 <= n:
            cur *= 10
        else:
            while cur == n or cur % 10 == 9:
                cur //= 10
            cur += 1
    return res

    # Recursive solution
    # res = []
    #
    # def dfs(num: int) -> None:
    #     if num > n:
    #         return
    #     res.append(num)
    #     for i in range(10):
    #         cur_num = num * 10 + i
    #         dfs(cur_num)
    #
    # for i in range(1, 10):
    #     dfs(i)
    # return res


if __name__ == '__main__':
    n1 = 13
    n2 = 2

    print(lexicalOrder(n1))
    print(lexicalOrder(n2))
