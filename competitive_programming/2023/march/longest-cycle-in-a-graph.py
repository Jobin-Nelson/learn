'''
Created Date: 2023-03-26
Qn: You are given a directed graph of n nodes numbered from 0 to n - 1, where
    each node has at most one outgoing edge.

    The graph is represented with a given 0-indexed array edges of size n,
    indicating that there is a directed edge from node i to node edges[i]. If
    there is no outgoing edge from node i, then edges[i] == -1.

    Return the length of the longest cycle in the graph. If no cycle exists,
    return -1.

    A cycle is a path that starts and ends at the same node.
Link: https://leetcode.com/problems/longest-cycle-in-a-graph/
Notes:
    - store the number of steps it took to reach that node
    - when encountering a visited node get steps - visited[cur_node]
'''
def longestCycle(edges: list[int]) -> int:
    N = len(edges)
    res = -1
    step = 1
    visited = [0]* N
    for i in range(N):
        if visited[i]: continue
        cur_step = step
        cur_node = i
        while cur_node != -1 and not visited[cur_node]:
            visited[cur_node] = step
            step += 1
            cur_node = edges[cur_node]
        if cur_node != -1 and visited[cur_node] >= cur_step:
            res = max(res, step - visited[cur_node])
        
    return res

if __name__ == '__main__':
    e1 = [3, 3, 4, 2, 3]
    e2 = [2, -1, 3, 1]

    print(longestCycle(e1))
    print(longestCycle(e2))
