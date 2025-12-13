import collections

def find_first(size, steps):
    nums = collections.deque()
    for i in range(1, size+1):
        nums.append(i)
    for _ in range(steps):
        first = nums.popleft()
        second = nums.popleft()

        nums.append(second)
        nums.append(first)

    return nums[0]

if __name__ == "__main__":
    print(find_first(4, 3)) # 4
    print(find_first(12, 5)) # 11
    print(find_first(2, 1000)) # 1
    print(find_first(99, 555)) # 11
    print(find_first(12345, 10**6)) # 12295
