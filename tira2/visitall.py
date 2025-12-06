from itertools import permutations

def find_route(distances):
    cities = list(range(len(distances)))

    routes = permutations(cities[1:])
    routes = map(lambda r: [0] + list(r) + [0], routes)
    shortest_len = float('inf')
    shortest_route = []

    for route in routes:
        route_len = 0
        for curr, next in zip(route, route[1:]):
            route_len += distances[curr][next]
            if route_len > shortest_len:
                break
        else:
            if route_len < shortest_len:
                shortest_len = route_len
                shortest_route = route
            elif route_len == shortest_len:
                shortest_route = min(shortest_route, route)

    shortest_route = list(map(lambda c: c+1, shortest_route))
    return (shortest_len, shortest_route)

if __name__ == "__main__":
    distances = [[0, 2, 2, 1, 8],
                 [2, 0, 9, 1, 2],
                 [2, 9, 0, 8, 3],
                 [1, 1, 8, 0, 3],
                 [8, 2, 3, 3, 0]]

    length, route = find_route(distances)
    print(length) # 9
    print(route) # [1, 3, 5, 2, 4, 1]

    distances = [[0, 7, 5, 9, 6, 3, 1, 3],
                 [7, 0, 3, 2, 3, 3, 7, 8],
                 [5, 3, 0, 4, 2, 7, 7, 1],
                 [9, 2, 4, 0, 2, 3, 2, 4],
                 [6, 3, 2, 2, 0, 9, 5, 9],
                 [3, 3, 7, 3, 9, 0, 4, 5],
                 [1, 7, 7, 2, 5, 4, 0, 7],
                 [3, 8, 1, 4, 9, 5, 7, 0]]

    length, route = find_route(distances)
    print(length) # 18
    print(route) # [1, 7, 4, 6, 2, 5, 3, 8, 1]
