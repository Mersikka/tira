class PermutationTracker:
    def __init__(self):
        self.not_found = 0
        self.max_num = 0
        self.nums = set()
        self.repeats = False

    def append(self, number):
        if number in self.nums:
            self.repeats = True
        if number > self.max_num:
            self.not_found += number - self.max_num
            self.max_num = number

        self.nums.add(number)
        self.not_found -= 1

    def check(self):
        if self.repeats == True:
            return False
        return self.not_found == 0


if __name__ == "__main__":
    tracker = PermutationTracker()

    tracker.append(1)
    print(tracker.check())  # True

    tracker.append(4)
    print(tracker.check())  # False

    tracker.append(2)
    print(tracker.check())  # False

    tracker.append(3)
    print(tracker.check())  # True

    tracker.append(2)
    print(tracker.check())  # False

    tracker.append(5)
    print(tracker.check())  # False

    tracker = PermutationTracker()
    total = 0
    for i in range(10**5):
        if i % 2 == 0:
            tracker.append(i + 2)
        else:
            tracker.append(i)
        if tracker.check():
            total += 1
    print(total)  # 50000
