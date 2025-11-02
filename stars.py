def count_patterns(grid):

    counter = 0
    patterns = {}

    def explore(grid, y, x):
        if (grid[y][x]) != "*" or (y, x) in patterns:
            return

        patterns[(y, x)] = counter

        if y > 0:
            explore(grid, y - 1, x)
            if x > 0:
                explore(grid, y - 1, x - 1)
        if y < len(grid) - 1:
            explore(grid, y + 1, x)
            if x < len(grid[0]) - 1:
                explore(grid, y + 1, x + 1)
        if x > 0:
            explore(grid, y, x - 1)
            if y < len(grid) - 1:
                explore(grid, y + 1, x - 1)
        if x < len(grid[0]) - 1:
            explore(grid, y, x + 1)
            if y > 0:
                explore(grid, y - 1, x + 1)

    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if (y, x) not in patterns and grid[y][x] == "*":
                counter += 1
                explore(grid, y, x)

    if counter == 1:
        return counter

    pattern_to_stars = {}

    for point in patterns:
        if patterns[point] not in pattern_to_stars:
            pattern_to_stars[patterns[point]] = []
        pattern_to_stars[patterns[point]].append(point)

    point_diffs = []

    for pattern in pattern_to_stars:
        point_diffs_helper = []
        for point in sorted(pattern_to_stars[pattern]):
            for another_point in sorted(pattern_to_stars[pattern]):
                if another_point == point:
                    continue
                point_diffs_helper.append(
                    (point[0] - another_point[0], point[1] - another_point[1])
                )
        if point_diffs_helper in point_diffs:
            counter -= 1
        point_diffs.append(point_diffs_helper)

    return counter


if __name__ == "__main__":
    grid = [
        "..*..*..",
        "**.....*",
        ".....**.",
        "...*....",
        ".**....*",
    ]
    print(count_patterns(grid))  # 2

    grid = [
        "....*..*",
        "*.......",
        "......*.",
        "..*.....",
        "......*.",
    ]
    print(count_patterns(grid))  # 1

    grid = [
        "***.*.**",
        ".*..*..*",
        ".*.***..",
        ".......*",
        "......**",
    ]
    print(count_patterns(grid))  # 4

    grid = [
        "***.***.",
        "..*...*.",
        "**..**..",
        "..*...*.",
        "**..**..",
    ]
    print(count_patterns(grid))  # 1
