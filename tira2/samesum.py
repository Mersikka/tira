from itertools import combinations

def check_sum(numbers):
    if len(numbers) == 1:
        if numbers[0] == 0:
            return True
        else:
            return False

    for i in range(int(len(numbers)/2)+1):
        combs = set(combinations(numbers, i))
        for comb in combs:
            comb = list(comb)
            if sum(comb) == sum([n for n in numbers if not n in comb or comb.remove(n)]):
                return True
    return False

if __name__ == "__main__":
    print(check_sum([1, 2, 3, 4])) # True
    print(check_sum([1, 2, 3, 5])) # False
    print(check_sum([0])) # True
    print(check_sum([2, 2])) # True
    print(check_sum([2, 4])) # False
    print(check_sum([1, 5, 6, 3, 5])) # True
    print(check_sum([1, 5, 5, 3, 5])) # False
    print(check_sum([10**9, 2*10**9, 10**9])) # True
    print(check_sum([1, 1, 1, 1, 1, 1, 1, 1, 1, 123])) # False
