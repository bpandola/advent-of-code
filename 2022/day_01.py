def parse_input(filename):
    data = open(filename).read().split('\n\n')
    data = [[int(item) for item in items.split('\n')] for items in data]
    return data


def get_top_calorie_counts(data, num_elves=1):
    counts_sorted = sorted([sum(calories) for calories in data], reverse=True)
    total = 0
    for i in range(num_elves):
        total += counts_sorted[i]
    return total


if __name__ == '__main__':
    puzzle_input = parse_input('day_01.in')
    sample_input = parse_input('day_01.in.sample_01')

    # Part 1
    assert get_top_calorie_counts(sample_input) == 24000
    print(get_top_calorie_counts(puzzle_input))

    # Part 2
    assert get_top_calorie_counts(sample_input, 3) == 45000
    print(get_top_calorie_counts(puzzle_input, 3))
