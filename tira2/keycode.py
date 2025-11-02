from itertools import permutations

def find_codes(pattern):
    if "?" not in pattern:
        return [pattern]
    pattern = list(pattern)
    empty_spots = []
    for i, n in enumerate(pattern):
        if n == "?":
            empty_spots.append(i)
    digits = set("123456789")
    for n in pattern:
        digits.discard(n)
    digits = sorted(list(digits))
    perms = permutations(digits, len(empty_spots))
    result = []
    
    for perm in perms:
        pattern_copy = pattern.copy()
        for i, spot in enumerate(empty_spots):
            pattern_copy[spot] = perm[i]
        result.append("".join(pattern_copy))

    return result
            
    


if __name__ == "__main__":
    codes = find_codes("24?5")
    print(codes) # ['2415', '2435', '2465', '2475', '2485', '2495']
    print()

    codes = find_codes("1?2?")
    print(codes[:5]) # ['1324', '1325', '1326', '1327', '1328']
    print(len(codes)) # 42
    print()

    codes = find_codes("????")
    print(codes[:5]) # ['1234', '1235', '1236', '1237', '1238']
    print(len(codes)) # 3024
