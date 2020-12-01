def part_1(numbers, sum_to_find):
    for i in range(len(numbers)):
        num_1 = numbers[i]
        for j in range(len(numbers)):
            num_2 = numbers[j]
            if num_1 + num_2 == sum_to_find:
                return num_1 * num_2


def part_2(numbers, sum_to_find):
    for i in range(len(numbers)):
        num_1 = numbers[i]
        for j in range(len(numbers)):
            num_2 = numbers[j]
            for k in range(len(numbers)):
                num_3 = numbers[k]
                if num_1 + num_2 + num_3 == sum_to_find:
                    return num_1 * num_2 * num_3


if __name__ == '__main__':
    puzzle_input = [int(i) for i in open('day_01.in').read().split('\n')]
    sample_input = [1721, 979, 366, 299, 675, 1456]

    # Part 1
    assert part_1(sample_input, 2020) == 514579
    print(part_1(puzzle_input, 2020))

    # Part 2
    assert part_2(sample_input, 2020) == 241861950
    print(part_2(puzzle_input, 2020))
