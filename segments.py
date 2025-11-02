def find_segments(data):
    segments = []
    count = 0
    current_letter = ""
    last_letter = data[0]

    for letter in data:
        current_letter = letter
        if current_letter != last_letter:
            segments.append((count, last_letter))
            count = 0
        count += 1
        last_letter = current_letter
    segments.append((count, last_letter))

    return segments


if __name__ == "__main__":
    print(find_segments("aaabbccdddd"))
    # [(3, 'a'), (2, 'b'), (2, 'c'), (4, 'd')]

    print(find_segments("aaaaaaaaaaaaaaaaaaaa"))
    # [(20, 'a')]

    print(find_segments("abcabc"))
    # [(1, 'a'), (1, 'b'), (1, 'c'), (1, 'a'), (1, 'b'), (1, 'c')]

    print(find_segments("kissa"))
    # [(1, 'k'), (1, 'i'), (2, 's'), (1, 'a')]
