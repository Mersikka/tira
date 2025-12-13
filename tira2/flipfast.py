
def find_first(size, steps):
    if size == 1:
        return 1
    if size == 2:
        if steps % 2 == 0:
            return 1
        return 2

    

if __name__ == "__main__":
    print(find_first(4, 3)) # 4
    print(find_first(12, 5)) # 11
    print(find_first(2, 1000)) # 1
    print(find_first(99, 555)) # 11
    print(find_first(12345, 10**6)) # 12295
    print(find_first(123456789, 1337**42)) # 111766959
