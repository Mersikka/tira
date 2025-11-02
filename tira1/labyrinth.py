def find_route(grid):
    start = (0, 0)
    end = (0, 0)
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == "A":
                start = (y, x)
            if grid[y][x] == "B":
                end = (y, x)

    distances = {}
    previous = {}

    queue = [start]
    distances[start] = 0
    previous[start] = None

    def edges(grid, tile):
        edge_list = []
        if grid[tile[0] + 1][tile[1]] != "#":
            edge_list.append((tile[0] + 1, tile[1]))
        if grid[tile[0] - 1][tile[1]] != "#":
            edge_list.append((tile[0] - 1, tile[1]))
        if grid[tile[0]][tile[1] + 1] != "#":
            edge_list.append((tile[0], tile[1] + 1))
        if grid[tile[0]][tile[1] - 1] != "#":
            edge_list.append((tile[0], tile[1] - 1))
        return edge_list

    for tile in queue:
        distance = distances[tile]
        for next_tile in edges(grid, tile):
            if next_tile not in distances:
                queue.append(next_tile)
                distances[next_tile] = distance + 1
                previous[next_tile] = tile

    if end not in distances:
        return None

    tile = end
    path = []
    while tile:
        path.append(tile)
        tile = previous[tile]

    return len(path) - 1


if __name__ == "__main__":
    grid = [
        "########",
        "#.#.B..#",
        "#A#.##.#",
        "#......#",
        "########",
    ]
    print(find_route(grid))  # 6

    grid = [
        "########",
        "#B#...A#",
        "#.#.##.#",
        "#......#",
        "########",
    ]
    print(find_route(grid))  # 9

    grid = [
        "########",
        "####..B#",
        "#.A#.#.#",
        "#..#...#",
        "########",
    ]
    print(find_route(grid))  # None
