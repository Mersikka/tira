def can_create(coins, target):
    has_one = 1 in coins
    if has_one:
        return True
    coins.append(1)

    no_ones = {0: True}
    for s in range(1, target + 1):
        no_ones[s] = False
        for c in coins:
            if s-c>=0:
                if c != 1:
                    if no_ones[s-c]:
                        no_ones[s] = True
    return no_ones[target]

if __name__ == "__main__":
    print(can_create([1, 2, 5], 13)) # True
    print(can_create([2, 4, 6], 13)) # False
    
    print(can_create([1], 42)) # True
    print(can_create([2, 4, 6], 42)) # True
    print(can_create([3], 1337)) # False
    print(can_create([3, 4], 1337)) # True
    print(can_create([8, 13], 49)) # False
    print(can_create([3, 7], 23)) # True
