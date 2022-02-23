def undirected_path(edges, nodeA, nodeB):
    graph = build_graph(edges)
    print(graph)
    return has_path_depth(graph, nodeA, nodeB, visited=set())

def has_path_depth(graph, src, dst, visited):
    if src == dst:
        return True
    if src in visited:
        return False
    visited.add(src)
    for neighbor in graph[src]:
        if has_path_depth(graph, neighbor, dst, visited):
            return True
    return False

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
	['i', 'j'], 
	['k', 'i'],
	['m', 'k'],
	['k', 'l'],
	['o', 'n']
]

print(undirected_path(edges, 'j', 'm'))
