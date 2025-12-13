from time import perf_counter_ns
import heapq
from random import sample

num_list = sample(range(1, (10**9)+1), k=10**7)
print("Syöte sekoitettu.\n")

def tapa1(nums):
    how_many = len(nums)/10
    how_many = round(how_many)
    ns = nums.copy()

    res = sum(sorted(ns)[:how_many])
    print(res)
    return res

def tapa2(nums):
    how_many = len(nums)/10
    how_many = round(how_many)
    ns = nums.copy()

    num_heap = []

    for n in ns:
        heapq.heappush(num_heap, n)

    res = sum([heapq.heappop(num_heap) for _ in range(how_many)])
    print(res)
    return res

def tapa3(nums):
    how_many = len(nums)/10
    how_many = round(how_many)
    ns = nums.copy()

    heapq.heapify(ns)

    res = sum([heapq.heappop(ns) for _ in range(how_many)])
    print(res)
    return res

start = perf_counter_ns()
tapa1(num_list)
end = perf_counter_ns()
print(f"Ensimmäisessä tavassa kesti {(end-start)/10**9} sekuntia")

start = perf_counter_ns()
tapa2(num_list)
end = perf_counter_ns()
print(f"Toisessa tavassa kesti {(end-start)/10**9} sekuntia")

start = perf_counter_ns()
tapa3(num_list)
end = perf_counter_ns()
print(f"Kolmannessa tavassa kesti {(end-start)/10**9} sekuntia")
