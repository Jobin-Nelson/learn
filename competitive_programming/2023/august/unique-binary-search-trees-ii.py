'''
Created Date: 2023-08-05
Qn: Given an integer n, return all the structurally unique BST's (binary search
    trees), which has exactly n nodes of unique values from 1 to n. Return the
    answer in any order.
Link: https://leetcode.com/problems/unique-binary-search-trees-ii/
Notes:
    - use dp
'''
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self) -> str:
        res = []
        q = deque([self])
        while q:
            node = q.popleft()
            res.append(node.val)
            if node.left: q.append(node.left)
            if node.right: q.append(node.right)
        return str(res)

    def __repr__(self) -> str:
        return self.__str__()

def generateTrees(n: int) -> list[TreeNode | None]:
    dp = [[] for _ in range(n+1)]
    dp[0].append(None)

    for numberOfNodes in range(1, n+1):
        for i in range(1, numberOfNodes+1):
            j = numberOfNodes - i
            for left in dp[i-1]:
                for right in dp[j]:
                    root = TreeNode(i, left, clone(right, i))
                    dp[numberOfNodes].append(root)
    return dp[n]

def clone(node: TreeNode | None, offset: int) -> TreeNode | None:
    if not node: return None
    cloned_node = TreeNode(node.val + offset)
    cloned_node.left = clone(node.left, offset)
    cloned_node.right = clone(node.right, offset)
    return cloned_node


if __name__ == '__main__':
    n1 = 3
    n2 = 1

    print(generateTrees(n1))
    print(generateTrees(n2))
