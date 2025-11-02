def find_components(nodes, edges):
    graph = {node: [] for node in nodes}
    for e in edges:
        graph[e[0]].append(e[1])
        graph[e[1]].append(e[0])

    def visit(node, components, counter, graph):
        if node in components:
            return
        components[node] = counter

        for next_node in graph[node]:
            visit(next_node, components, counter, graph)

    counter = 0
    node_to_comp = {}

    for node in nodes:
        if node not in node_to_comp:
            counter += 1
            visit(node, node_to_comp, counter, graph)

    components = {v: [] for v in node_to_comp.values()}

    for node in node_to_comp:
        components[node_to_comp[node]].append(node)

    return sorted(map(lambda x: sorted(x), components.values()), key=lambda c: min(c))


if __name__ == "__main__":
    nodes = [1, 2, 3, 4, 5, 6, 7, 8]
    edges = [(1, 2), (1, 3), (2, 3), (4, 5), (4, 6), (5, 7), (6, 7)]
    print(find_components(nodes, edges))  # [[1, 2, 3], [4, 5, 6, 7], [8]]

    nodes = [1, 2, 3, 4, 5]
    edges = []
    print(find_components(nodes, edges))  # [[1], [2], [3], [4], [5]]

    nodes = [1, 2, 3, 4, 5]
    edges = [(1, 2), (1, 3), (1, 4), (1, 5)]
    print(find_components(nodes, edges))  # [[1, 2, 3, 4, 5]]
