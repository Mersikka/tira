import collections
from time import perf_counter_ns

n = 10**5

nums = collections.deque()

start = perf_counter_ns()
for i in range(1, n+1):
    nums.append(i)
end = perf_counter_ns()
print(f"Lisääminen kesti {(end-start)/10**9} sekuntia")

start = perf_counter_ns()
for _ in range(n):
    nums.popleft()
end = perf_counter_ns()
print(f"Poistaminen kesti {(end-start)/10**9} sekuntia")
