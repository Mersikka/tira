from time import perf_counter_ns
import heapq
from random import sample

num_list = sample(list(range(1, (10**9)+1)), 10**7)


def tapa1(nums):
    how_many = len(nums)/10
    how_many = round(how_many)

    return sum(nums[:how_many+1])

def tapa2(nums):
    how_many = len(nums)/10
    how_many = round(how_many)

    num_heap = []

    for n in nums:
        heapq.heappush(num_heap, n)

    
