def solver(sequence, match_offset):
    accumulator = 0
    for i in range(len(sequence)):
        if sequence[i] == sequence[(i + match_offset) % len(sequence)]:
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
        assert solver(inp, 1) == out
    print(solver(puzzle_input, 1))

    # Part 2
    sample_data_2 = [
        ([1, 2, 1, 2], 6),
        ([1, 2, 2, 1], 0),
        ([1, 2, 3, 4, 2, 5], 4),
        ([1, 2, 3, 1, 2, 3], 12),
        ([1, 2, 1, 3, 1, 4, 1, 5], 4),
    ]
    for inp, out in sample_data_2:
        assert solver(inp, len(inp) // 2) == out
    print(solver(puzzle_input, len(puzzle_input) // 2))
