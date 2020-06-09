from django.test import TestCase

# graph = {
#     'A': ['B', 'C'],
#     'B': ['D', 'E'],
#     'C': ['F'],
#     'D': [],
#     'E': ['F'],
#     'F': []
# }


grafo = {
    'P1': ['P2'],
    'P2': ['P1', 'P4'],
    'P3': ['P4', 'P5'],
    'P4': ['P2', 'P3'],
    'P5': ['P3', 'P6'],
    'P6': ['P7'],
    'P7': ['P6'],
}


def bfs(graph_to_search, start, end):
    queue = [[start]]
    visited = set()

    while queue:
        path = queue.pop(0)

        vertex = path[-1]

        if vertex == end:
            return path
        elif vertex not in visited:
            for current_neighbour in graph_to_search.get(vertex, []):
                new_path = list(path)
                new_path.append(current_neighbour)
                queue.append(new_path)

            visited.add(vertex)


print(bfs(grafo, 'P1', 'P7'))
