
def first_wins(numbers):
    p1 = 0
    p2 = 0
    lp = 0
    rp = len(numbers)-1
    while lp <= rp:
        if lp == rp:
            p1 += numbers[lp]
        else:
            p1 += max(numbers[lp], numbers[rp])
            p2 += min(numbers[lp], numbers[rp])
        lp += 1
        rp -= 1
    return p1 > p2

if __name__ == "__main__":
    print(first_wins([2, 1, 3])) # True
    print(first_wins([1, 3, 1])) # False

    print(first_wins([1])) # True
    print(first_wins([1, 1])) # False
    print(first_wins([1, 5])) # True
    print(first_wins([1, 1, 1])) # True
    print(first_wins([1, 2, 3, 4])) # True
    print(first_wins([1, 3, 3, 7, 4, 2, 1])) # False

    print(first_wins([1] * 50)) # False
    print(first_wins([1, 2] * 25)) # True
