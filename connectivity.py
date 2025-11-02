def connected(nodes, edges):
    graph = {node: [] for node in nodes}
    for e in edges:
        graph[e[0]].append(e[1])
        graph[e[1]].append(e[0])

    def visit(components, counter, graph, node):
        if node in components:
            return
        components[node] = counter

        for next_node in graph[node]:
            visit(components, counter, graph, next_node)

    counter = 0
    components = {}

    for node in nodes:
        if node not in components:
            counter += 1
            if counter > 1:
                return False
            visit(components, counter, graph, node)

    return True


if __name__ == "__main__":
    nodes = [1, 2, 3, 4, 5]
    edges = [(1, 2), (1, 3), (1, 4), (2, 4), (2, 5), (3, 4), (4, 5)]
    print(connected(nodes, edges))  # True

    nodes = [1, 2, 3, 4, 5, 6, 7, 8]
    edges = [(1, 2), (1, 3), (2, 3), (4, 5), (4, 6), (5, 7), (6, 7)]
    print(connected(nodes, edges))  # False

    nodes = [1, 2, 3, 4, 5]
    edges = []
    print(connected(nodes, edges))  # False

    nodes = [1, 2, 3, 4, 5]
    edges = [(1, 2), (1, 3), (1, 4), (1, 5)]
    print(connected(nodes, edges))  # True
