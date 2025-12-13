import heapq

def find_smallest(steps):
    nums = set()
    num_heap = []

    heapq.heappush(num_heap, 1)
    nums.add(1)

    for _ in range(steps):
        n = heapq.heappop(num_heap)
        nums.remove(n)

        if n*2 not in nums:
            nums.add(n*2)
            heapq.heappush(num_heap, n*2)
        if n*3 not in nums:
            nums.add(n*3)
            heapq.heappush(num_heap, n*3)
    return num_heap[0]
            

if __name__ == "__main__":
    print(find_smallest(0)) # 1
    print(find_smallest(1)) # 2
    print(find_smallest(2)) # 3
    print(find_smallest(3)) # 4
    print(find_smallest(4)) # 6
    print(find_smallest(5)) # 8

    print(find_smallest(42)) # 1296
    print(find_smallest(1337)) # 16210220612075905068
    print(find_smallest(123123)) # 47241633171870338440585357243035120029747450090811731814934867117962334088709324512562801224664331563355142646399182644605958987116029586018592281978123083613432358051028210559768563023872
