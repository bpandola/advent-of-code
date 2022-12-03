import string


def parse_input(filename):
    lines = open(filename).read().split('\n')
    return lines


PRIORITIES = {}
for priority, key in enumerate(string.ascii_lowercase + string.ascii_uppercase, start=1):
    PRIORITIES[key] = priority
    priority += 1


def find_compartment_priority_sum(rucksacks):
    total = 0
    for rucksack in rucksacks:
        sack_split = int(len(rucksack) / 2)
        compartment_1 = set(rucksack[:sack_split])
        compartment_2 = set(rucksack[sack_split:])
        duplicates = compartment_1.intersection(compartment_2)
        assert len(duplicates) == 1
        for d in duplicates:
            total += PRIORITIES[d]
    return total


def find_group_priority_sum(lines):
    total = 0
    for index, line in enumerate(lines, start=1):
        if index % 3 == 0:
            s1, s2, s3 = set(lines[index - 3]), set(lines[index - 2]), set(lines[index - 1])
            duplicates = s1.intersection(s2.intersection(s3))
            assert len(duplicates) == 1
            for d in duplicates:
                total += PRIORITIES[d]
    return total


if __name__ == '__main__':
    puzzle_input = parse_input('day_03.in')
    sample_input = parse_input('day_03.in.sample_01')

    # Part 1
    assert find_compartment_priority_sum(sample_input) == 157
    print(find_compartment_priority_sum(puzzle_input))

    # Part 2
    assert find_group_priority_sum(sample_input) == 70
    print(find_group_priority_sum(puzzle_input))
