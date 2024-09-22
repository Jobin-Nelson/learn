"""
Created Date: 2024-09-19
Qn: Given a string expression of numbers and operators, return all possible
    results from computing all the different possible ways to group numbers and
    operators. You may return the answer in any order.

    The test cases are generated such that the output values fit in a 32-bit
    integer and the number of different results does not exceed 104.
Link: https://leetcode.com/problems/different-ways-to-add-parentheses/
Notes:
    - use backtracking
"""


def diffWaysToCompute(expression: str) -> list[int]:
    operations = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
    }

    def backtrack(left: int, right: int) -> list[int]:
        res = []
        for i in range(left, right+1):
            op = expression[i]
            if op in operations:
                nums1 = backtrack(left, i-1)
                nums2 = backtrack(i+1, right)
                for n1 in nums1:
                    for n2 in nums2:
                        res.append(operations[op](n1, n2))
        if res == []:
            res.append(int(expression[left:right+1]))
        return res
    return backtrack(0, len(expression)-1)


if __name__ == '__main__':
    e1 = "2-1-1"
    e2 = "2*3-4*5"

    print(diffWaysToCompute(e1))
    print(diffWaysToCompute(e2))
