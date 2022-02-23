def has_path_depth(graph, src, dst):
    if src == dst:
        return True
    for neighbor in graph[src]:
        if has_path_depth(graph, neighbor, dst):
            return True
    return False

def has_path_breadth(graph, src, dst):
    queue = [src]

    while len(queue) > 0:
        current = queue.pop(0)
        if current == dst:
            return True
        for neighbor in graph[current]:
            queue.append(neighbor)
    return False

graph = {
	'f': ['g', 'i'],
	'g': ['h'],
	'h': [],
	'i': ['g', 'k'],
	'j': ['i'],
	'k': []
}

print(has_path_depth(graph, 'f', 'k'))
print(has_path_breadth(graph, 'f', 'k'))
