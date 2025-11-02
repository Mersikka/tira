def find_order(n):
    circle_map = {}
    for key in range(n):
        if key + 2 > n:
            circle_map[key + 1] = 1
        else:
            circle_map[key + 1] = key + 2
    print(circle_map)


if __name__ == "__main__":
    print(find_order(1))  # [1]
    print(find_order(2))  # [2, 1]
    print(find_order(3))  # [2, 1, 3]
    print(find_order(7))  # [2, 4, 6, 1, 5, 3, 7]

    # order = find_order(10**5)
    # print(order[-5:])  # [52545, 85313, 36161, 3393, 68929]
