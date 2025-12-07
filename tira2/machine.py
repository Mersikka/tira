def min_steps(x):
    if (x-2) % 3 != 0 and (x-4) % 3 != 0:
        return -1

    steps = 0
    while x > 1:
        if x % 2 == 0 and x != 4:
            x /= 2
        else:
            x -= 3
        steps += 1
    return steps

if __name__ == "__main__":
    print(min_steps(1)) # 0
    print(min_steps(2)) # 1
    print(min_steps(3)) # -1
    print(min_steps(4)) # 1
    print(min_steps(5)) # 2
    print(min_steps(17)) # 4
    print(min_steps(42)) # -1
    print(min_steps(100)) # 7
    print(min_steps(1000)) # 13
