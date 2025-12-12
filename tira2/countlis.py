def count_sequences(numbers):
    seq_len = {}
    seq = {}
    seqs = {}

    max_len = 0
    best = 0
    for i in range(len(numbers)):
        seq_len[i] = 1
        seq[i] = [numbers[i]]
        seqs[i] = []
        best = 0
        for j in range(i):
            if numbers[j] < numbers[i]:
                seq_len[i] = max(seq_len[i], seq_len[j] + 1)
                if seq_len[j] >= seq_len[best] or (seq_len[j] == seq_len[best] and numbers[j] < numbers[best]):
                    best = j
                seq[i] = seq[best].copy() + [numbers[i]]
                seqs[i].append(seq[i])
        max_len = max(max_len, seq_len[i])

    longest = sorted(seq.items(), key=lambda s: len(s[1])).pop()
    return seqs[longest[0]]

if __name__ == "__main__":
    print(count_sequences([1, 2, 3])) # 1
    print(count_sequences([3, 2, 1])) # 3
    print(count_sequences([1, 1, 1, 1, 1])) # 5

    print(count_sequences([1, 8, 2, 7, 3, 6])) # 1
    print(count_sequences([1, 1, 2, 2, 3, 3])) # 8
    print(count_sequences([4, 1, 5, 6, 3, 4, 3, 8])) # 3
