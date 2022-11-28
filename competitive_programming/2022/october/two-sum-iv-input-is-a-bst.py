'''
Created Date: 2022-10-09
Qn: Given the root of a Binary Search Tree and a target number k, return true
    if there exist two elements in the BST such that their sum is equal to the
    given target.
Link: https://leetcode.com/problems/two-sum-iv-input-is-a-bst/
Notes:
    - same strategy as two sum
    - traverse the tree, (dfs or bfs)
    - use set to see if the complementary number was visited before
'''
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def findTarget(root: TreeNode | None, k: int) -> bool:
    map = set()

    def dfs(node):
        if not node: return False
        comp_number = k - node.val
        if comp_number in map: 
            return True
        else:
            map.add(node.val)
        return dfs(node.left) or dfs(node.right)
    return dfs(root)

if __name__ == '__main__':
    a1 = TreeNode(2)
    b1 = TreeNode(4)
    c1 = TreeNode(7)
    d1 = TreeNode(3, a1, b1)
    e1 = TreeNode(6, right=c1)
    r1 = TreeNode(5, d1, e1)
    k1 = 9

    a2 = TreeNode(2)
    b2 = TreeNode(4)
    c2 = TreeNode(7)
    d2 = TreeNode(3, a2, b2)
    e2 = TreeNode(6, right=c2)
    r2 = TreeNode(5, d2, e2)
    k2 = 28

    print(findTarget(r1, k1))
    print(findTarget(r2, k2))

