'''
Created Date: 2023-08-20
Qn: There are n items each belonging to zero or one of m groups where group[i]
    is the group that the i-th item belongs to and it's equal to -1 if the i-th
    item belongs to no group. The items and the groups are zero indexed. A
    group can have no item belonging to it.

    Return a sorted list of the items such that:

        The items that belong to the same group are next to each other in the
        sorted list. There are some relations between these items where
        beforeItems[i] is a list containing all the items that should come
        before the i-th item in the sorted array (to the left of the i-th
        item).

    Return any solution if there is more than one solution and return an empty
    list if there is no solution.
Link: https://leetcode.com/problems/sort-items-by-groups-respecting-dependencies/
Notes:
    - use topological sort
'''
def sortItems(n: int, m: int, group: list[int], beforeItems: list[list[int]]) -> list[int]:
    group_id = m
    for i in range(n):
        if group[i] == -1:
            group[i] = group_id
            group_id += 1

    item_graph = [[] for _ in range(n)]
    item_indegree = [0] * n

    group_graph = [[] for _ in range(group_id)]
    group_indegree = [0] * group_id

    for cur in range(n):
        for prev in beforeItems[cur]:
            item_graph[prev].append(cur)
            item_indegree[cur] += 1

            if group[prev] != group[cur]:
                group_graph[group[prev]].append(group[cur])
                group_indegree[group[cur]] += 1

    def topological_sort(graph: list[list[int]], indegree: list[int]) -> list[int]:
        visited = []
        stack = [node for node in range(len(graph)) if indegree[node] == 0]
        while stack:
            cur = stack.pop()
            visited.append(cur)
            for nei in graph[cur]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    stack.append(nei)
        return visited if len(visited) == len(graph) else []

    item_order = topological_sort(item_graph, item_indegree)
    group_order = topological_sort(group_graph, group_indegree)

    if not item_order or not group_order: return []

    ordered_groups = [[] for _ in range(group_id)]
    for item in item_order:
        ordered_groups[group[item]].append(item)

    res = []
    for group_index in group_order:
        res.extend(ordered_groups[group_index])
    return res

if __name__ == '__main__':
    n1, m1, g1, b1 = 8, 2, [-1,-1,1,0,0,1,0,-1], [[],[6],[5],[6],[3,6],[],[],[]]
    n2, m2, g2, b2 = 8, 2, [-1,-1,1,0,0,1,0,-1], [[],[6],[5],[6],[3],[],[4],[]]

    print(sortItems(n1, m1, g1, b1))
    print(sortItems(n2, m2, g2, b2))
    
