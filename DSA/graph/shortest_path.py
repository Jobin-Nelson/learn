def shortest_path(edges, nodeA, nodeB):
    graph = build_graph(edges)
    visited = set(nodeA)
    queue = [[nodeA, 0]]
    while len(queue) > 0:
        node, distance = queue.pop(0)
        if node == nodeB:
            return distance
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append([neighbor, distance+1])
    return -1

def build_graph(edges):
    graph = dict()
    for a, b in edges:
        if a not in graph:
            graph[a] = []
        if b not in graph:
            graph[b] = []
        graph[a].append(b)
        graph[b].append(a)
    return graph

edges = [
	['w', 'x'],
	['x', 'y'],
	['z', 'y'],
	['z', 'v'],
	['w', 'v'],
]

if __name__ == '__main__':
    print(shortest_path(edges, 'w', 'z'))
