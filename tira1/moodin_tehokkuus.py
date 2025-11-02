from random import choices
from time import perf_counter_ns


def dict_find_mode(numbers):
    count = {}
    mode = numbers[0]

    for x in numbers:
        if x not in count:
            count[x] = 0
        count[x] += 1

        if count[x] > count[mode]:
            mode = x

    return mode


def list_find_mode(numbers):
    sorted_nums = sorted(numbers)
    mode = sorted_nums[0]
    mode_count = 0
    cur_count = 0
    last = sorted_nums[0]

    for n in sorted_nums:
        if last != n:
            if cur_count > mode_count:
                mode = last
                mode_count = cur_count
            cur_count = 1
            last = n
        else:
            cur_count += 1
    if cur_count > mode_count:
        mode = last
        mode_count = cur_count

    return mode


if __name__ == "__main__":

    print("Randomizing input...")
    numbers = choices(list(range(1, 1001)), k=10**7)
    print("Done!\n")

    print("Running dict implementation...")
    start = perf_counter_ns()
    print(f"Dict mode: {dict_find_mode(numbers)}\n")
    end = perf_counter_ns()
    dict_time = end - start
    dict_time = dict_time * 10**-9

    print("Running list implementation...")
    start = perf_counter_ns()
    print(f"List mode: {dict_find_mode(numbers)}\n")
    end = perf_counter_ns()
    list_time = end - start
    list_time = list_time * 10**-9

    print("Timing results:")
    print(f"Dict running time: {dict_time:.10f}s")
    print(f"List running time: {list_time:.10f}s")
