from random import choices
from time import time


# toteutus 1
def count_even1(numbers):
    result = 0
    for x in numbers:
        if x % 2 == 0:
            result += 1
    return result


# toteutus 2
def count_even2(numbers):
    return sum(x % 2 == 0 for x in numbers)


if __name__ == "__main__":
    nums = list(range(10))
    numbers = choices(nums, k=(10**7))

    start_time = time()
    count_even1(numbers)
    end_time = time()

    print(f"Testi 1: {round(end_time - start_time, 7)}s")

    start_time = time()
    count_even2(numbers)
    end_time = time()

    print(f"Testi 2: {round(end_time - start_time, 7)}s")
