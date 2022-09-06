graph = {
    '1': ['2', '3'],
    '2': ['4', '5'],
    '3': ['6'],
    '4': [],
    '5': ['6'],
    '6': [],
}

# LISTS
# TO KEEP TRACK OF VISITED NODES
visited = []

# INITIALIZE A QUEUE
queue = []

def bfs(visited, graph, node):
    visited.append(node)
    queue.append(node)

    while queue:
        s = queue.pop(0)
        print(s, end = ' ')

        for neighbour in graph[s]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)

bfs(visited, graph, '2')

