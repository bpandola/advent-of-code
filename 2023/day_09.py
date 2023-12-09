def parse_input(filename):
    data = []
    lines = open(filename).read().split('\n')
    for line in lines:
        data.append([int(i) for i in line.split()])
    return data

def find_next_value(sequence):
    sequences = []
    sequences.append(sequence[:])
    n = 0
    while True:
        new_seq = []
        seq = sequences[n]
        for i in range(len(seq)-1):
            new_seq.append(seq[i+1]-seq[i])
        sequences.append(new_seq)
        if sum(new_seq) == 0:
            break
        n+=1
    # Walk sequences backward to get next
    for i in range(len(sequences)-1, 0, -1):
        s = sequences[i]
        t = sequences[i-1]
        t.append(t[-1]+s[-1])
    return sequences[0][-1]

def find_next_values(sequences):
    next_nums = []
    for sequence in sequences:
        next_num = find_next_value(sequence)
        next_nums.append(next_num)
    return sum(next_nums)


def find_prev_value(sequence):
    sequences = []
    sequences.append(sequence[:])
    n = 0
    while True:
        new_seq = []
        seq = sequences[n]
        for i in range(len(seq)-1):
            new_seq.append(seq[i+1]-seq[i])
        sequences.append(new_seq)
        if sum(new_seq) == 0:
            break
        n+=1
    # Walk sequences backward to get prev
    for i in range(len(sequences)-1, 0, -1):
        s = sequences[i]
        t = sequences[i-1]
        t.insert(0, t[0]-s[0])
    return sequences[0][0]

def find_prev_values(sequences):
    next_nums = []
    for sequence in sequences:
        next_num = find_prev_value(sequence)
        next_nums.append(next_num)
    return sum(next_nums)


if __name__ == '__main__':
    puzzle_input = parse_input('day_09.in')

    # Part 1
    sample_input = parse_input('day_09.in.sample')
    assert find_next_values(sample_input) == 114
    print(find_next_values(puzzle_input))

    # Part 2
    assert find_prev_values(sample_input) == 2
    print(find_prev_values(puzzle_input))
