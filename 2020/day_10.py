from itertools import combinations
from functools import reduce


def parse_input(filename):
    joltages = list(map(int, open(filename).read().split('\n')))
    joltages.append(0)  # Add outlet joltage.
    joltages.append(max(joltages) + 3)  # Add device joltage.
    return sorted(joltages)


def calculate_joltage_differences(joltages):
    differences = []
    for i in range(1, len(joltages)):
        differences.append(joltages[i] - joltages[i - 1])
    assert all([diff in [1, 3] for diff in differences])
    return differences.count(1) * differences.count(3)


def calculate_num_adapter_arrangements(adapters):
    # For any adapter that is required, we store it as a single item list.
    # For any adapter sequences that can be rearranged, we store them as
    # an array of all possible arrangements.
    # Total arrangements can then be calculated by multiplying the lengths
    # of all the lists together.
    chains = [[adapters[0]]]
    index = 1
    while index < len(adapters):
        potential_adapters = [a for a in adapters[index:] if a - adapters[index - 1] <= 3]
        if len(potential_adapters) > 1:
            index += len(potential_adapters)
            combos = []
            for i in range(1, len(potential_adapters) + 1):
                possibilities = list(combinations(potential_adapters, i))
                for p in possibilities:
                    # We have to make sure that the first adapter in this
                    # combination is within range of the previous adapter
                    # and the last adapter in this combination is within
                    # range of the next adapter in our list.
                    if p[0] - adapters[index - 1] <= 3:
                        if adapters[index] - p[-1] <= 3:
                            combos.append(p)
            chains.append(combos)
        else:
            chains.append(potential_adapters)
            index += 1

    return reduce(lambda x, y: x * y, [len(c) for c in chains])


if __name__ == '__main__':
    puzzle_input = parse_input('day_10.in')
    sample_small = parse_input('day_10.in.sample_small')
    sample_large = parse_input('day_10.in.sample_large')

    # Part 1
    assert calculate_joltage_differences(sample_small) == 35
    assert calculate_joltage_differences(sample_large) == 220
    print(calculate_joltage_differences(puzzle_input))

    # Part 2
    assert calculate_num_adapter_arrangements(sample_small) == 8
    assert calculate_num_adapter_arrangements(sample_large) == 19208
    print(calculate_num_adapter_arrangements(puzzle_input))
