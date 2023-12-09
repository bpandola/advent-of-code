def parse_input(filename):
    lines = open(filename).read().split('\n')
    data = [[int(i) for i in line.split()] for line in lines]
    return data


def extrapolate_history(history):
    sequences = [history[:]]
    n = 0
    while True:
        sequence_new = []
        sequence_cur = sequences[n]
        for i in range(len(sequence_cur) - 1):
            sequence_new.append(sequence_cur[i + 1] - sequence_cur[i])
        sequences.append(sequence_new)
        if sum(sequence_new) == 0:  # All zeroes, we out.
            break
        n += 1
    # Walk sequences in reverse to extrapolate previous/next values.
    for i in range(len(sequences) - 1, 0, -1):
        sequence_prev = sequences[i]
        sequence = sequences[i - 1]
        # Extrapolate next value.
        sequence.append(sequence[-1] + sequence_prev[-1])
        # Extrapolate previous value.
        sequence.insert(0, sequence[0] - sequence_prev[0])
    return sequences[0]


def find_next_values(histories):
    next_values = []
    for history in histories:
        new_sequence = extrapolate_history(history)
        next_values.append(new_sequence[-1])
    return sum(next_values)


def find_prev_values(histories):
    next_values = []
    for history in histories:
        new_sequence = extrapolate_history(history)
        next_values.append(new_sequence[0])
    return sum(next_values)


if __name__ == '__main__':
    sample_input = parse_input('day_09.in.sample')
    puzzle_input = parse_input('day_09.in')

    # Part 1
    assert find_next_values(sample_input) == 114
    print(find_next_values(puzzle_input))

    # Part 2
    assert find_prev_values(sample_input) == 2
    print(find_prev_values(puzzle_input))
