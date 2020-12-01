import sys
from itertools import permutations


def min_max_checksum(lines):
    accumulator = 0
    for sequence in lines:
        sequence_min = sys.maxsize
        sequence_max = -sys.maxsize
        for number in sequence:
            if number > sequence_max:
                sequence_max = number
            if number < sequence_min:
                sequence_min = number
        accumulator += sequence_max - sequence_min
    return accumulator


def quotient_checksum(lines):
    accumulator = 0
    for sequence in lines:
        for divisor, dividend in permutations(sequence, 2):
            quotient = float(dividend / divisor)
            if quotient.is_integer():
                accumulator += quotient
                break
    return accumulator


if __name__ == '__main__':
    puzzle_input = [[int(x.strip()) for x in line.split('\t')] for line in open('day_02.in').read().split('\n')]

    # Part 1
    sample_data_1 = [
        [5, 1, 9, 5],
        [7, 5, 3],
        [2, 4, 6, 8],
    ]
    assert min_max_checksum(sample_data_1) == 18
    print(min_max_checksum(puzzle_input))

    # Part 2
    sample_data_2 = [
        [5, 9, 2, 8],
        [9, 4, 7, 3],
        [3, 8, 6, 5],
    ]
    assert quotient_checksum(sample_data_2) == 9
    print(quotient_checksum(puzzle_input))
