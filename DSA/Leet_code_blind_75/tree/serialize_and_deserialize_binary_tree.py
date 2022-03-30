'''
Qn: Design an alogrithm to serialize and deserialize a binary tree. 
There is no restriction on how your serialization and deserialization algorithm should work.
You just need to ensure that binary string can be serialized to a string and this string can be deserialized to the original tree structure
Link: https://leetcode.com/problems/serialize-and-deserialize-binary-tree/
Notes:
- appending each node to a list and returning it in string format following dfs approach
- splitting the string data to a list and using a variable to iterate through it while in dfs to reconstruct binary tree
'''
class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Codec:
    def serialize(self, root: TreeNode) -> str:
        res = []

        def dfs(root):
            if not root:
                res.append('N')
                return 
            res.append(str(root.val))
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        return ','.join(res)

    def deserialize(self, data: str) -> TreeNode:
        vals = data.split(',')
        self.i = 0

        def dfs():
            if vals[self.i] == 'N':
                self.i += 1
                return None
            node = TreeNode(int(vals[self.i]))
            self.i += 1
            node.left = dfs()
            node.right = dfs()
            return node
        return dfs()

if __name__ == '__main__':
    a1 = TreeNode(2)
    b1 = TreeNode(4)
    c1 = TreeNode(5)
    d1 = TreeNode(3, b1, c1)
    r1 = TreeNode(1, a1, d1)

    def depth_first_values_rec(root):
        if root == None: return []
        left_values = depth_first_values_rec(root.left)
        right_values = depth_first_values_rec(root.right)
        return [root.val, *left_values, *right_values]

    code = Codec()
    data = code.serialize(r1)
    print(data)
    print(depth_first_values_rec((code.deserialize(data))))
