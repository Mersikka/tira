def count_numbers(a, b):
    numlist = [0]
    current_nums = [0]
    templist = []
    while current_nums[-1] <= b:
        for num in current_nums:
            print(current_nums)
            numlist.append(num * 10 + 2)
            templist.append(num * 10 + 2)
            numlist.append(num * 10 + 5)
            templist.append(num * 10 + 5)
        current_nums = templist.copy()
        templist = []
        


if __name__ == "__main__":
    print(count_numbers(1, 100)) # 6
#    print(count_numbers(60, 70)) # 0
#    print(count_numbers(25, 25)) # 1
#    print(count_numbers(1, 10**9)) # 1022
#    print(count_numbers(123456789, 987654321)) # 512
