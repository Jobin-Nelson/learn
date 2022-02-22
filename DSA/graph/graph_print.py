def depth_first_print(graph, source):
    print(source)
    for neighbor in graph[source]:
        depth_first_print(graph, neighbor)

def breadth_first_print(graph, source):
    queue = [source]

    while len(queue) > 0:
        current = queue.pop(0)
        print(current)
        for neighbor in graph[current]:
            queue.append(neighbor)


if __name__ == '__main__':
    graph = {
        'a': ['b', 'c'],
        'b': ['d'],
        'c': ['e'],
        'd': ['f'],
        'e': [],
        'f': [],
    }
    print('Depth first print')
    depth_first_print(graph, 'a')
    print('Breadth first print')
    breadth_first_print(graph, 'a')
