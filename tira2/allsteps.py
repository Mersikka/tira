def count_steps(x):
    result = {1: 1}
    for i in range(1, x+1):
        if (i-2) % 3 != 0 and (i-4) % 3 != 0:
            result[i] = 0
        elif (i-2) % 3 != 0 and (i-4) % 3 != 0:
            result[i] = 0
        else:
            result[i+3] = result.get(i+3, 0) + result[i]
            result[i*2] = result.get(i*2, 0) + result[i]
    return result[x]
        


if __name__ == "__main__":
    print(count_steps(1)) # 1
    print(count_steps(2)) # 1
    print(count_steps(3)) # 0
    print(count_steps(4)) # 2
    print(count_steps(5)) # 1
    print(count_steps(17)) # 5
    print(count_steps(42)) # 0
    print(count_steps(100)) # 242
    print(count_steps(1000)) # 2948311
