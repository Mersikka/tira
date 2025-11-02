def count_rooms(grid):

    counter = 0
    rooms = {}

    def explore(grid, y, x):
        if (grid[y][x]) != "." or (y, x) in rooms:
            return

        rooms[(y, x)] = counter

        explore(grid, y - 1, x)
        explore(grid, y + 1, x)
        explore(grid, y, x - 1)
        explore(grid, y, x + 1)

    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if (y, x) not in rooms and grid[y][x] == ".":
                counter += 1
                explore(grid, y, x)
    return counter


if __name__ == "__main__":
    grid = ["########", "#.#..#.#", "#####..#", "#...#..#", "########"]
    print(count_rooms(grid))  # 4

    grid = ["########", "#......#", "#.####.#", "#......#", "########"]
    print(count_rooms(grid))  # 1

    grid = ["########", "######.#", "##.#####", "########", "########"]
    print(count_rooms(grid))  # 2
