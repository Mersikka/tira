def find_sequence(numbers):
    seq_len = {}
    seq = {}

    max_len = 0
    best = 0
    for i in range(len(numbers)):
        seq_len[i] = 1
        seq[i] = [numbers[i]]
        best = 0
        for j in range(i):
            if numbers[j] < numbers[i]:
                seq_len[i] = max(seq_len[i], seq_len[j] + 1)
                if seq_len[j] >= seq_len[best] or (seq_len[j] == seq_len[best] and numbers[j] < numbers[best]):
                    best = j
                seq[i] = seq[best].copy() + [numbers[i]]
        max_len = max(max_len, seq_len[i])

    longest = sorted(seq.values(), key=lambda s: len(s)).pop()
    return longest

if __name__ == "__main__":
    print(find_sequence([1, 2, 3])) # [1, 2, 3]
    print(find_sequence([3, 2, 1])) # [1]
    print(find_sequence([1, 1, 1, 1, 1])) # [1]

    print(find_sequence([1, 8, 2, 7, 3, 6])) # [1, 2, 3, 6]
    print(find_sequence([1, 1, 2, 2, 3, 3])) # [1, 2, 3]
    print(find_sequence([4, 1, 5, 6, 3, 4, 3, 8])) # [1, 3, 4, 8]
