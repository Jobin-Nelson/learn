'''
Qn: You are given the root of a binary search tree (BST), 
where the values of exactly two nodes of the tree were swapped by mistake. 
Recover the tree without changing its structure.
Link: https://leetcode.com/problems/recover-binary-search-tree/
Notes:
- check if the current node value is less than previous node value while traversing inorder
- capture the ones that are not, and swap their values
'''
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def recover_tree(root: TreeNode) -> None:
    '''Do not return anything modify root in-place instead'''
    stack, replace = [], []
    prev = TreeNode(float('-inf'))
    cur = root

    while cur or stack:
        while cur:
            stack.append(cur)
            cur = cur.left
        temp = stack.pop()

        if temp.val < prev.val:
            replace.append((prev, temp))
        prev = temp
        cur = temp.right

    replace[0][0].val, replace[-1][1].val = replace[-1][1].val, replace[0][0].val

def list_tree(root: TreeNode) -> list:
    if not root: return []
    queue = [root]
    res = []

    while queue:
        current = queue.pop(0)
        res.append(current.val)
        if current.left: queue.append(current.left)
        if current.right: queue.append(current.right)
    return res

if __name__ == '__main__':
    a1 = TreeNode(2)
    b1 = TreeNode(3, right=a1)
    r1 = TreeNode(1, b1)

    a2 = TreeNode(2)
    b2 = TreeNode(1)
    c2 = TreeNode(4, a2)
    r2 = TreeNode(3, b2, c2)
    print('Before recovering')
    print(list_tree(r1))
    print(list_tree(r2))
    recover_tree(r1)
    recover_tree(r2)
    print('\nAfter recovering')
    print(list_tree(r1))
    print(list_tree(r2))

