import math


class Comparer:
    def __init__(self, numbers):
        self.numbers = numbers
        self.counter = 0
        n = len(self.numbers)
        self.bound = n * math.floor(math.log2(n))

    def list_size(self):
        return len(self.numbers)

    def smaller(self, a, b):
        self.counter += 1
        if self.counter > self.bound:
            raise RuntimeError("too many comparisons")
        return self.numbers[a] < self.numbers[b]


def find_list(comp: Comparer):
    size = comp.list_size()
    nums = list(range(1, size + 1))
    if size == 1:
        return 1


if __name__ == "__main__":
    comparer = Comparer([3, 1, 2, 4])
    numbers = find_list(comparer)
    print(numbers)  # [3, 1, 2, 4]

    comparer = Comparer([1, 6, 2, 5, 3, 4])
    numbers = find_list(comparer)
    print(numbers)  # [1, 6, 2, 5, 3, 4]
