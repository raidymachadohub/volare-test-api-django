def bfs(graph_pesquisar, origem, destino):
    queue = [[origem]]
    visited = set()
    array = []
    while queue:

        path = queue.pop(0)

        vertex = path[-1]

        if vertex == destino:
            return array

        elif vertex not in visited:

            for current_neighbour in graph_pesquisar.get(vertex, []):
                new_path = list(path)
                new_path.append(current_neighbour)
                queue.append(new_path)
                array.append(vertex + ' - ' + current_neighbour)
            visited.add(vertex)
