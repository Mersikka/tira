def check_year(year):
    left = int(str(year)[:2])
    right = int(str(year)[2:])
    return (left + right) ** 2 == year


if __name__ == "__main__":
    print(check_year(1995))  # False
    print(check_year(2024))  # False
    print(check_year(2025))  # True
    print(check_year(2026))  # False
    print(check_year(3025))  # True
    print(check_year(5555))  # False
