from functools import reduce
from itertools import combinations


def solver(numbers, sum_to_find, num_addends):
    for combo in combinations(numbers, num_addends):
        if sum(combo) == sum_to_find:
            return reduce((lambda x, y: x * y), combo)


if __name__ == '__main__':
    puzzle_input = [int(i) for i in open('day_01.in').read().split('\n')]
    sample_input = [1721, 979, 366, 299, 675, 1456]

    # Part 1
    assert solver(sample_input, 2020, 2) == 514579
    print(solver(puzzle_input, 2020, 2))

    # Part 2
    assert solver(sample_input, 2020, 3) == 241861950
    print(solver(puzzle_input, 2020, 3))
