'''
Qn: Given a reference of a node in a connected undirected graph.
Return a deep copy (clone) of the graph.
Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.

# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

Link: https://leetcode.com/problems/clone-graph/
Notes: 
- memoization 
'''
class Solution:
    def clone_graph(self, node: 'Node') -> 'Node':
        old_new = {}

        def clone(node):
            if node in old_new:
                return old_new[node]

            copy = Node(node.val)
            old_new[node] = copy

            for neighbor in node.neighbors:
                copy.neighbors.append(clone(neighbor))
            return copy
        return clone(node) if node else None
