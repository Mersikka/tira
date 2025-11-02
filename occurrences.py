class OccurrenceTracker:
    def __init__(self):
        self.num_occs = {}
        self.occs = {}

    def append(self, number):
        if number not in self.num_occs:
            self.num_occs[number] = 0
        self.num_occs[number] += 1

        if self.num_occs[number] not in self.occs:
            self.occs[self.num_occs[number]] = 0
        self.occs[self.num_occs[number]] += 1

        if self.num_occs[number] - 1 in self.occs:
            self.occs[self.num_occs[number] - 1] -= 1
            if self.occs[self.num_occs[number] - 1] == 0:
                del self.occs[self.num_occs[number] - 1]
        else:
            self.occs[self.num_occs[number] - 1] = 1

    def count(self):
        if 0 in self.occs:
            del self.occs[0]
        return len(self.occs)


if __name__ == "__main__":
    tracker = OccurrenceTracker()

    tracker.append(1)
    tracker.append(2)
    tracker.append(1)
    tracker.append(3)
    print(tracker.count())  # 2

    tracker.append(2)
    tracker.append(3)
    print(tracker.count())  # 1

    tracker.append(2)
    tracker.append(3)
    tracker.append(3)
    print(tracker.count())  # 3
