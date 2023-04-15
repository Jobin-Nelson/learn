'''
Created Date: 2023-04-08
Qn: Given a reference of a node in a connected undirected graph.

    Return a deep copy (clone) of the graph.

    Each node in the graph contains a value (int) and a list (List[Node]) of
    its neighbors.

    Test case format:

    For simplicity, each node's value is the same as the node's index
    (1-indexed). For example, the first node with val == 1, the second node
    with val == 2, and so on. The graph is represented in the test case using
    an adjacency list.

    An adjacency list is a collection of unordered lists used to represent a
    finite graph. Each list describes the set of neighbors of a node in the
    graph.

    The given node will always be the first node with val = 1. You must return
    the copy of the given node as a reference to the cloned graph.
Link: https://leetcode.com/problems/clone-graph/
Notes:
'''
from collections import deque

class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

def cloneGraph(node: Node) -> Node:
    if not node: return node

    q, clones = deque([node]), { node.val: Node(node.val, []) }

    while q:
        cur = q.popleft()
        cur_clone = clones[cur.val]

        for nei in cur.neighbors:
            if nei.val not in clones:
                clones[nei.val] = Node(nei.val, [])
                q.append(nei)
            cur_clone.neighbors.append(clones[nei.val])
    return clones[node.val]

if __name__ == '__main__':
    adj1 = Node.from_list([[2,4],[1,3],[2,4],[1,3]])
    adj2 = Node.from_list([[]])
    adj3 = Node.from_list([])

    print(cloneGraph(adj1))
    print(cloneGraph(adj2))
    print(cloneGraph(adj3))
