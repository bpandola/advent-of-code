def part_1(numbers):
    accumulator = 0
    sequence = numbers[:] + [numbers[0]]
    for i in range(len(sequence) - 1):
        if sequence[i] == sequence[i + 1]:
            accumulator += sequence[i]
    return accumulator


def part_2(numbers):
    accumulator = 0
    sequence = numbers[:]
    seq_len = len(sequence)
    for i in range(seq_len):
        if sequence[i] == sequence[(i + seq_len // 2) % seq_len]:
            accumulator += sequence[i]
    return accumulator


if __name__ == '__main__':
    puzzle_input = [int(x) for x in open('day_01.in').read()]

    # Part 1
    sample_data_1 = [
        ([1, 1, 2, 2], 3),
        ([1, 1, 1, 1], 4),
        ([1, 2, 3, 4], 0),
        ([9, 1, 2, 1, 2, 1, 2, 9], 9),

    ]
    for inp, out in sample_data_1:
        assert part_1(inp) == out
    print(part_1(puzzle_input))

    # Part 2
    sample_data_2 = [
        ([1, 2, 1, 2], 6),
        ([1, 2, 2, 1], 0),
        ([1, 2, 3, 4, 2, 5], 4),
        ([1, 2, 3, 1, 2, 3], 12),
        ([1, 2, 1, 3, 1, 4, 1, 5], 4),
    ]
    for inp, out in sample_data_2:
        assert part_2(inp) == out
    print(part_2(puzzle_input))
